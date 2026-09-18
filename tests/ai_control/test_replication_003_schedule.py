import unittest

from ai_control.replication_003_schedule import (
    COUNT,
    EXPECTED_SCHEDULE_SHA256,
    FIRST_SEED,
    LAST_SEED,
    frozen_schedule,
    schedule_sha256,
)


class Replication003ScheduleTests(unittest.TestCase):
    def test_exact_reserved_block(self):
        rows = frozen_schedule()
        self.assertEqual(len(rows), COUNT)
        self.assertEqual(rows[0].seed, FIRST_SEED)
        self.assertEqual(rows[-1].seed, LAST_SEED)
        self.assertEqual(len({row.seed for row in rows}), COUNT)

    def test_labels_are_exactly_balanced(self):
        rows = frozen_schedule()
        self.assertEqual(sum(row.violation_present for row in rows), 500)
        self.assertEqual(sum(row.feasible for row in rows), 500)
        self.assertEqual(sum(row.first_arm == "logging_only" for row in rows), 500)

    def test_schedule_hash_is_frozen(self):
        self.assertEqual(schedule_sha256(), EXPECTED_SCHEDULE_SHA256)


if __name__ == "__main__":
    unittest.main()
