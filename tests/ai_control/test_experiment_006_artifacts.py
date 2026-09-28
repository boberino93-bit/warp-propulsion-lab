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


class Observation006ArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.summary = json.loads((_RESULTS / "006-summary.json").read_text())
        cls.manifest = json.loads(
            (_RESULTS / "006-artifact-manifest.json").read_text()
        )
        encoded_runs = (_RESULTS / "006-runs.csv.gz.b64").read_bytes()
        cls.runs_bytes = gzip.decompress(base64.b64decode(encoded_runs))
        cls.rows = list(csv.DictReader(io.StringIO(cls.runs_bytes.decode())))
        cls.event_bytes = b"".join(
            path.read_bytes()
            for path in sorted(_RESULTS.glob("006-events.part-*.b64"))
        )
        cls.events = json.loads(gzip.decompress(base64.b64decode(cls.event_bytes)))

    def test_complete_artifact_hashes_counts_and_pairing(self):
        self.assertEqual(
            hashlib.sha256(self.runs_bytes).hexdigest(),
            self.summary["006-runs.csv_sha256"],
        )
        self.assertEqual(
            hashlib.sha256(self.event_bytes).hexdigest(),
            self.summary["006-events.json.gz.b64_sha256"],
        )
        self.assertEqual(len(self.rows), 9000)
        self.assertEqual(len(self.events), 40908)
        pairs = {(int(row["seed"]), row["condition"]) for row in self.rows}
        self.assertEqual(len(pairs), 9000)
        by_seed = defaultdict(set)
        for seed, condition in pairs:
            by_seed[seed].add(condition)
        self.assertEqual(set(by_seed), set(range(423000, 424000)))
        self.assertTrue(all(len(conditions) == 9 for conditions in by_seed.values()))

    def test_manifest_parts_are_complete_and_ordered(self):
        parts = sorted(_RESULTS.glob("006-events.part-*.b64"))
        expected = self.manifest["events_parts"]
        self.assertEqual([p.name for p in parts], [row["name"] for row in expected])
        for path, row in zip(parts, expected):
            self.assertEqual(path.stat().st_size, row["bytes"])
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), row["sha256"])
        runs = _RESULTS / self.manifest["runs_archive"]["name"]
        self.assertEqual(runs.stat().st_size, self.manifest["runs_archive"]["bytes"])
        self.assertEqual(
            hashlib.sha256(runs.read_bytes()).hexdigest(),
            self.manifest["runs_archive"]["sha256"],
        )

    def test_every_published_event_chain_recomputes(self):
        groups = defaultdict(list)
        for event in self.events:
            groups[(event["seed"], event["condition"])].append(event)
        self.assertEqual(len(groups), 9000)
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
                self.assertEqual(
                    data["source_commit"],
                    "d95b3b840b4ea347cacb6b880f3603f3ce5ee8cd",
                )
                previous = claimed

    def test_frozen_primary_counts_and_control_invariant(self):
        dropout = {"0": 0, "100": 7, "500": 30, "1000": 51, "2500": 129}
        corruption = {"0": 0, "100": 5, "500": 27, "1000": 49, "2500": 110}
        self.assertEqual(
            {k: v["completed"] for k, v in self.summary["dropout_completion_rates"].items()},
            dropout,
        )
        self.assertEqual(
            {k: v["completed"] for k, v in self.summary["corruption_completion_rates"].items()},
            corruption,
        )
        self.assertTrue(self.summary["all_integrity_gates_pass"])
        self.assertTrue(self.summary["control_invariant_pass"])
        self.assertTrue(self.summary["dropout_directional_hypothesis_pass"])
        self.assertTrue(self.summary["corruption_directional_hypothesis_pass"])
        self.assertEqual(self.summary["observed_valid_detections"], 4092)
        self.assertEqual(self.summary["benign_false_stops"], 0)


if __name__ == "__main__":
    unittest.main()
