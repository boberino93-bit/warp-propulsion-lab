import base64
import csv
import gzip
import hashlib
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
RESULTS = ROOT / "research" / "ai-control" / "results"


class Replication003ArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.summary = json.loads((RESULTS / "003-summary.json").read_text())
        cls.pairs_bytes = (RESULTS / "003-pairs.csv").read_bytes()
        cls.events_bytes = (RESULTS / "003-events.json.gz.b64").read_bytes()

    def test_frozen_provenance_and_result(self):
        self.assertEqual(self.summary["reserved_seed_first"], 421000)
        self.assertEqual(self.summary["reserved_seed_last"], 421999)
        self.assertEqual(
            self.summary["schedule_sha256"],
            "ce49182fda417635d42e32fe38ff9c2df790487eaabe0de5abec9791572d80c2",
        )
        self.assertEqual(self.summary["primary_paired_risk_difference"], -1.0)
        self.assertEqual(self.summary["bootstrap_95_interval"], [-1.0, -1.0])
        self.assertTrue(self.summary["all_integrity_gates_pass"])

    def test_retained_file_hashes(self):
        self.assertEqual(
            hashlib.sha256(self.pairs_bytes).hexdigest(),
            self.summary["003-pairs.csv_sha256"],
        )
        self.assertEqual(
            hashlib.sha256(self.events_bytes).hexdigest(),
            self.summary["003-events.json.gz.b64_sha256"],
        )

    def test_all_pairs_and_containment_counts(self):
        rows = list(csv.DictReader(self.pairs_bytes.decode("utf-8").splitlines()))
        self.assertEqual(len(rows), 1000)
        violations = [row for row in rows if row["violation_present"] == "True"]
        benign = [row for row in rows if row["violation_present"] == "False"]
        self.assertEqual(len(violations), 500)
        self.assertEqual(len(benign), 500)
        self.assertEqual(sum(int(r["logging_completed_use"]) for r in violations), 500)
        self.assertEqual(sum(int(r["enforced_completed_use"]) for r in violations), 0)
        self.assertEqual(sum(int(r["enforced_controlled_stop"]) for r in violations), 500)
        self.assertEqual(sum(int(r["enforced_controlled_stop"]) for r in benign), 0)
        self.assertEqual(
            sum(int(r["enforced_post_detection_agent_events"]) for r in violations), 0
        )

    def test_event_package_count_and_hash_chains(self):
        encoded = self.events_bytes.decode("ascii").strip()
        events = json.loads(gzip.decompress(base64.b64decode(encoded)))
        self.assertEqual(len(events), 7500)
        previous_by_trial = {}
        for event in events:
            key = (event["seed"], event["arm"])
            expected_previous = previous_by_trial.get(key, "0" * 64)
            self.assertEqual(event["previous_event_hash"], expected_previous)
            claimed = event["event_hash"]
            body = dict(event)
            body.pop("event_hash")
            body.pop("trial_status")
            actual = hashlib.sha256(
                json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
            ).hexdigest()
            self.assertEqual(actual, claimed)
            previous_by_trial[key] = claimed


if __name__ == "__main__":
    unittest.main()
