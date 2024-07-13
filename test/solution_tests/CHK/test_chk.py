from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        # Test two integers
        assert sum_solution.compute(1, 2) == 3
        # Test first param over 100
        assert sum_solution.compute(101, 1) == ValueError("Both values must be between 0 and 100")
        # Test second param over 100
        assert sum_solution.compute(1, 101) == ValueError("Both values must be between 0 and 100")
        # Test first param under 0
        assert sum_solution.compute(-1, 1) == ValueError("Both values must be between 0 and 100")
        # Test second param under 0
        assert sum_solution.compute(1, -1) == ValueError("Both values must be between 0 and 100")
        # Test first param not an integer
        assert sum_solution.compute("a", 1) == ValueError("Both values must be integers")
        # Test second param not an integer
        assert sum_solution.compute(1, "a") == ValueError("Both values must be integers")
        # Test first param not an integer
        assert sum_solution.compute(1.1, 1) == ValueError("Both values must be integers")
        # Test second param not an integer
        assert sum_solution.compute(1, 1.1) == ValueError("Both values must be integers")

