from fractional_knapsack import fractional_knapsack

import math

def test_fractional_knapsack():
    test_cases = [
        # Test Case 1: Basic example
        ((50, [(10, 60), (20, 100), (30, 120)]), math.ceil(240.0)),

        # Test Case 2: Knapsack can hold all items (Take everything)
        ((60, [(10, 60), (20, 100), (30, 120)]), math.ceil(280.0)),

        # Test Case 3: Knapsack can hold only the most valuable item fully
        ((10, [(10, 60), (20, 100), (30, 120)]), math.ceil(60.0)),

        # Test Case 4: Taking a fractional item
        ((40, [(10, 60), (20, 100), (30, 120)]), math.ceil(200.0)),

        # Test Case 5: Knapsack capacity is 0 (Can't take anything)
        ((0, [(10, 60), (20, 100), (30, 120)]), math.ceil(0.0)),

        # Test Case 6: Only one item, but it's heavier than capacity (Take fraction)
        ((5, [(10, 100)]), math.ceil(50.0)),

        # Test Case 7: Items with the same value-to-weight ratio (Order shouldn't matter)
        ((50, [(10, 20), (20, 40), (30, 60)]), math.ceil(100.0)),

        # Test Case 8: Single item fits exactly
        ((20, [(20, 50)]), math.ceil(50.0)),

        # Test Case 9: Knapsack is very large (Take everything)
        ((100, [(10, 60), (20, 100), (30, 120)]), math.ceil(280.0)),

        # Test Case 10: Items with decimal values
        ((50, [(10.5, 60.2), (20.3, 100.8), (30.7, 120.4)]), math.ceil(236.3))  # Adjusted expected value
    ]

    for i, ((capacity, items), expected) in enumerate(test_cases, 1):
        result = fractional_knapsack(capacity, items)
        assert result == expected, f"Test Case {i} Failed: Expected {expected}, Got {result}"
        print(f"Test Case {i} Passed ✅")

# Run tests
test_fractional_knapsack()

