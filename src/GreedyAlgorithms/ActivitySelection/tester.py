from activity_selection import activity_selection

def test_activity_selection():
    test_cases = [
        # Test Case 1: Normal case with multiple activities (Fixed expected output)
        ([(1, 3), (2, 5), (3, 9), (6, 8), (5, 7)], [(1, 3), (5, 7)]),

        # Test Case 2: Non-overlapping activities (All can be selected)
        ([(1, 2), (3, 4), (5, 6), (7, 8)], [(1, 2), (3, 4), (5, 6), (7, 8)]),

        # Test Case 3: Completely overlapping activities (Only one can be selected)
        ([(1, 10), (2, 9), (3, 8), (4, 7)], [(4, 7)]),

        # Test Case 4: Activities with the same end time (Pick the first one)
        ([(1, 4), (2, 4), (3, 4)], [(1, 4)]),

        # Test Case 5: Only one activity
        ([(1, 5)], [(1, 5)]),

        # Test Case 6: No activities (Edge case)
        ([], []),

        # Test Case 7: Large gaps between activities
        ([(1, 2), (10, 11), (20, 21)], [(1, 2), (10, 11), (20, 21)]),

        # Test Case 8: Unsorted input (Algorithm should still work)
        ([(3, 5), (1, 2), (6, 8), (4, 7)], [(1, 2), (3, 5), (6, 8)]),

        # Test Case 9: Multiple optimal solutions (Algorithm picks the first valid one)
        ([(1, 3), (2, 5), (4, 6), (5, 8), (6, 9)], [(1, 3), (4, 6), (6, 9)])
    ]

    for i, (activities, expected) in enumerate(test_cases, 1):
        result = activity_selection(activities)
        assert result == expected, f"Test Case {i} Failed: Expected {expected}, Got {result}"
        print(f"Test Case {i} Passed ✅")


# Run tests
test_activity_selection()
