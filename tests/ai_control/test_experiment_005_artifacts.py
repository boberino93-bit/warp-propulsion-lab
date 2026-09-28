from collections import defaultdict
import base64
import csv
import gzip
import hashlib
import io
import json
from pathlib import Path
import unittest

_ROOT = Path(__file__).resolve().parents[2]
_RESULTS = _ROOT / "research" / "ai-control" / "results"


class Dropout005ArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.summary_bytes = (_RESULTS / "005-summary.json").read_bytes()
        cls.summary = json.loads(cls.summary_bytes)
        cls.manifest = json.loads((_RESULTS / "005-artifact-manifest.json").read_text())
        encoded_runs = (_RESULTS / "005-runs.csv.gz.b64").read_bytes()
        cls.runs_bytes = gzip.decompress(base64.b64decode(encoded_runs))
        cls.rows = list(csv.DictReader(io.StringIO(cls.runs_bytes.decode("utf-8"))))
        cls.event_bytes = b"".join(
            path.read_bytes()
            for path in sorted(_RESULTS.glob("005-events.part-*.b64"))
        )
        cls.events = json.loads(gzip.decompress(base64.b64decode(cls.event_bytes)))

    def test_complete_artifact_hashes_and_counts(self):
        self.assertEqual(
            hashlib.sha256(self.runs_bytes).hexdigest(),
            self.summary["005-runs.csv_sha256"],
        )
        self.assertEqual(
            hashlib.sha256(self.event_bytes).hexdigest(),
            self.summary["005-events.json.gz.b64_sha256"],
        )
        self.assertEqual(len(self.rows), 5000)
        self.assertEqual(len(self.events), 17714)
        self.assertEqual(len({(r["seed"], r["condition"]) for r in self.rows}), 5000)

    def test_manifest_parts_are_complete_and_ordered(self):
        parts = sorted(_RESULTS.glob("005-events.part-*.b64"))
        self.assertEqual(len(parts), 14)
        self.assertEqual(
            [p.name for p in parts],
            [row["name"] for row in self.manifest["events_parts"]],
        )
        for path, expected in zip(parts, self.manifest["events_parts"]):
            self.assertEqual(path.stat().st_size, expected["bytes"])
            self.assertEqual(
                hashlib.sha256(path.read_bytes()).hexdigest(),
                expected["sha256"],
            )

    def test_every_published_event_chain_recomputes(self):
        groups = defaultdict(list)
        for event in self.events:
            groups[(event["seed"], event["condition"])].append(event)
        self.assertEqual(len(groups), 5000)
        for events in groups.values():
            previous = "0" * 64
            for event in events:
                data = dict(event)
                data.pop("trial_status")
                claimed = data.pop("event_hash")
                self.assertEqual(data["previous_event_hash"], previous)
                actual = hashlib.sha256(
                    json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
                ).hexdigest()
                self.assertEqual(actual, claimed)
                previous = claimed

    def test_frozen_primary_counts_and_control_invariant(self):
        expected = {"0": 0, "100": 6, "500": 25, "1000": 58, "2500": 125}
        self.assertEqual(
            {k: v["completed"] for k, v in self.summary["completion_rates"].items()},
            expected,
        )
        self.assertTrue(self.summary["all_integrity_gates_pass"])
        self.assertTrue(self.summary["control_invariant_pass"])
        self.assertTrue(self.summary["directional_hypothesis_pass"])
        self.assertEqual(self.summary["benign_false_stops"], 0)
        self.assertEqual(self.summary["observed_valid_detections"], 2286)


if __name__ == "__main__":
    unittest.main()
