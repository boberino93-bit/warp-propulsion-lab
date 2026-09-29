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


class Experiment008ArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.summary = json.loads((_RESULTS / "008-summary.json").read_text())
        cls.manifest = json.loads((_RESULTS / "008-artifact-manifest.json").read_text())
        runs_archive = (_RESULTS / "008-runs.csv.gz.b64").read_bytes()
        cls.runs_bytes = gzip.decompress(base64.b64decode(runs_archive))
        cls.rows = list(csv.DictReader(io.StringIO(cls.runs_bytes.decode())))
        cls.event_bytes = b"".join(
            path.read_bytes()
            for path in sorted(_RESULTS.glob("008-events.part-*.b64"))
        )
        cls.events = json.loads(gzip.decompress(base64.b64decode(cls.event_bytes)))

    def test_complete_artifact_hashes_counts_and_pairing(self):
        self.assertEqual(
            hashlib.sha256(self.runs_bytes).hexdigest(),
            self.summary["008-runs.csv_sha256"],
        )
        self.assertEqual(
            hashlib.sha256(self.event_bytes).hexdigest(),
            self.summary["008-events.json.gz.b64_sha256"],
        )
        self.assertEqual(len(self.rows), 4000)
        self.assertEqual(len(self.events), 15044)
        pairs = {(int(row["seed"]), row["condition"]) for row in self.rows}
        self.assertEqual(len(pairs), 4000)
        by_seed = defaultdict(set)
        for seed, condition in pairs:
            by_seed[seed].add(condition)
        self.assertEqual(set(by_seed), set(range(425000, 426000)))
        self.assertTrue(all(len(conditions) == 4 for conditions in by_seed.values()))

    def test_manifest_parts_are_complete_and_ordered(self):
        parts = sorted(_RESULTS.glob("008-events.part-*.b64"))
        expected = self.manifest["events_parts"]
        self.assertEqual([p.name for p in parts], [row["name"] for row in expected])
        for path, row in zip(parts, expected):
            self.assertEqual(path.stat().st_size, row["bytes"])
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), row["sha256"])
        self.assertEqual(
            hashlib.sha256(self.event_bytes).hexdigest(),
            self.manifest["events_joined_sha256"],
        )
        runs = _RESULTS / self.manifest["runs_archive"]["name"]
        self.assertEqual(runs.stat().st_size, self.manifest["runs_archive"]["bytes"])
        self.assertEqual(
            hashlib.sha256(runs.read_bytes()).hexdigest(),
            self.manifest["runs_archive"]["sha256"],
        )
        self.assertEqual(
            hashlib.sha256(self.runs_bytes).hexdigest(),
            self.manifest["runs_archive"]["decoded_sha256"],
        )

    def test_every_published_event_chain_recomputes(self):
        groups = defaultdict(list)
        for event in self.events:
            groups[(event["seed"], event["condition"])].append(event)
        self.assertEqual(len(groups), 4000)
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
                    "32f035eb047c4d4ea3a071348cea283c2fa8b225",
                )
                previous = claimed

    def test_frozen_results_and_hypotheses(self):
        rates = {
            key: value["completed"]
            for key, value in self.summary["completion_rates"].items()
        }
        self.assertEqual(
            rates,
            {
                "intact_logging": 500,
                "intact_enforced": 0,
                "dropout1000_logging": 500,
                "dropout1000_enforced": 44,
            },
        )
        contrasts = self.summary["matched_contrasts"]
        self.assertEqual(contrasts["authority_intact"]["matched_risk_difference"], -1.0)
        self.assertEqual(contrasts["authority_dropout"]["matched_risk_difference"], -0.912)
        self.assertEqual(contrasts["observation_enforced"]["matched_risk_difference"], 0.088)
        self.assertEqual(contrasts["observation_logging"]["matched_risk_difference"], 0.0)
        self.assertEqual(contrasts["interaction"]["matched_risk_difference"], 0.088)
        self.assertTrue(all(self.summary["hypotheses"].values()))

    def test_controls_resources_and_nulls(self):
        self.assertTrue(self.summary["all_integrity_gates_pass"])
        self.assertTrue(all(self.summary["control_invariants"].values()))
        self.assertEqual(self.summary["runs"], 4000)
        self.assertEqual(self.summary["agent_events"], 14088)
        self.assertEqual(self.summary["controller_events"], 956)
        self.assertEqual(self.summary["audit_events"], 15044)
        self.assertLess(self.summary["peak_traced_python_bytes"], 256 * 1024 * 1024)
        for result in self.summary["benign_false_stops"].values():
            self.assertEqual(result["stops"], 0)
            self.assertEqual(result["total"], 500)
            self.assertLess(result["wilson_95"][1], 0.02)


if __name__ == "__main__":
    unittest.main()
