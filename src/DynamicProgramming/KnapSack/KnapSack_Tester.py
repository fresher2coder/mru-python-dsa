from KnapSack import knapsack_01

def test_knapsack():
    test_cases = [
        # Test Case 1: Basic small case
        (4, [2, 1, 3], [4, 2, 7], 3, 9),  # Expected output: 9 (items 2 and 3)

        # Test Case 2: Single item, fits in the knapsack
        (10, [5], [10], 1, 10),  # Expected output: 10 (only one item, and it fits)

        # Test Case 3: Single item, doesn't fit
        (3, [5], [10], 1, 0),  # Expected output: 0 (only one item, but too heavy)

        # Test Case 4: Multiple items, choosing best combination (corrected expected value)
        (8, [2, 3, 4, 5], [3, 4, 5, 8], 4, 12),  # Expected output: 12

        # Test Case 5: Large capacity, many items (corrected expected value)
        (15, [2, 3, 5, 7, 1, 4], [10, 5, 15, 7, 6, 18], 6, 54),  # Expected output: 54

        # Test Case 6: Edge case, zero weight capacity
        (0, [1, 2, 3], [10, 20, 30], 3, 0),  # Expected output: 0 (knapsack cannot carry anything)

        # Test Case 7: Edge case, zero items
        (10, [], [], 0, 0),  # Expected output: 0 (no items to pick)

        # Test Case 8: Items with the same weight but different values
        (5, [1, 1, 1, 1, 1], [10, 20, 30, 40, 50], 5, 150),  # Expected output: 150 (best 5)

        # Test Case 9: Large values and weights
        (50, [10, 20, 30], [60, 100, 120], 3, 220),  # Expected output: 220 (classic case)

        # Test Case 10: Large input with optimal selection needed (corrected expected value)
        (10, [3, 4, 5, 6], [30, 50, 60, 70], 4, 120),  # Expected output: 120
    ]

    for i, (W, wt, val, N, expected) in enumerate(test_cases):
        result = knapsack_01(W, wt, val, N)
        print(f"Test Case {i+1}: {'PASS' if result == expected else 'FAIL'} (Expected {expected}, Got {result})")

# Run tests
test_knapsack()
