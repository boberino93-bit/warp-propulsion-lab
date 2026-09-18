import importlib.util
from pathlib import Path
import sys
import unittest

_MODULE_PATH = Path(__file__).resolve().parents[2] / "ai_control" / "replication_003_schedule.py"
_SPEC = importlib.util.spec_from_file_location("replication_003_schedule_under_test", _MODULE_PATH)
assert _SPEC is not None and _SPEC.loader is not None
schedule = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = schedule
_SPEC.loader.exec_module(schedule)


class Replication003ScheduleTests(unittest.TestCase):
    def test_exact_reserved_block(self):
        rows = schedule.frozen_schedule()
        self.assertEqual(len(rows), schedule.COUNT)
        self.assertEqual(rows[0].seed, schedule.FIRST_SEED)
        self.assertEqual(rows[-1].seed, schedule.LAST_SEED)
        self.assertEqual(len({row.seed for row in rows}), schedule.COUNT)

    def test_labels_are_exactly_balanced(self):
        rows = schedule.frozen_schedule()
        self.assertEqual(sum(row.violation_present for row in rows), 500)
        self.assertEqual(sum(row.feasible for row in rows), 500)
        self.assertEqual(sum(row.first_arm == "logging_only" for row in rows), 500)

    def test_schedule_hash_is_frozen(self):
        self.assertEqual(schedule.schedule_sha256(), schedule.EXPECTED_SCHEDULE_SHA256)


if __name__ == "__main__":
    unittest.main()
