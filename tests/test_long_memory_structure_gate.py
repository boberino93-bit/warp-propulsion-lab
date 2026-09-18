import unittest

from src.long_memory_structure_gate import (
    _long_memory,
    evaluate_long_memory_structure,
)


class LongMemoryStructureGateTests(unittest.TestCase):
    def test_preregistered_slice_is_deterministic(self):
        a = evaluate_long_memory_structure(trials=100)
        b = evaluate_long_memory_structure(trials=100)
        self.assertEqual(a, b)

    def test_generated_trace_is_centered_and_scaled(self):
        import random
        trace = _long_memory(64, 5e-6, random.Random(1), 0.5)
        mean = sum(trace) / len(trace)
        variance = sum((x - mean) ** 2 for x in trace) / len(trace)
        self.assertAlmostEqual(mean, 0.0, places=18)
        self.assertAlmostEqual(variance ** 0.5, 5e-6, places=18)

    def test_validation(self):
        with self.assertRaises(ValueError):
            evaluate_long_memory_structure(persistence_power=0)
        with self.assertRaises(ValueError):
            evaluate_long_memory_structure(trials=0)
        with self.assertRaises(ValueError):
            evaluate_long_memory_structure(threshold_n=0)


if __name__ == '__main__':
    unittest.main()
