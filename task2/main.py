from math import inf


def large_sum(arr):
    max_1 = -inf
    max_2 = -inf 
    for num in arr:
        if num > max_1:
            max_2 = max_1
            max_1 = num
        elif num > max_2:
            max_2 = num
    return max_1 + max_2


def test_large_sum():
    # Test with positive numbers
    assert large_sum([1, 2, 3, 4, 5]) == 9  
    # Test with negative numbers
    assert large_sum([-10, -20, -30, -1, -2]) == -3  
    # Test with mix of positive and negative
    assert large_sum([10, -5, 7, 3]) == 17 
    # Test with zeros
    assert large_sum([0, 0, 0, 1]) == 1  
    # Test with duplicate largest values
    assert large_sum([5, 5, 1, 2]) == 10  
    # Test with only two elements
    assert large_sum([100, 200]) == 300
    # Test with large numbers
    assert large_sum([1000000, 999999, 1]) == 1999999

# Run tests
if __name__ == "__main__":
    test_large_sum()
    print("All test cases passed!")
