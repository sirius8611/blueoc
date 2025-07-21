import unittest
def string_length_frequency(arr):
    frequency = {}
    max_frequency = 0
    result = -1
    for item in arr:
        n = len(item)
        if n in frequency:
            frequency[n] += 1
        else:
            frequency[n] = 1
        if frequency[n] > max_frequency:
            max_frequency = frequency[n]
            result = n
    result_arr = []
    for item in arr:
        if len(item) == result:
            result_arr.append(item)
    return result_arr



class TestStringLengthFrequency(unittest.TestCase):
    def test_basic(self):
        arr = ["a", "bb", "ccc", "dd", "ee", "f"]
        self.assertEqual(string_length_frequency(arr), ["bb", "dd", "ee"])

    def test_all_same_length(self):
        arr = ["aa", "bb", "cc"]
        self.assertEqual(sorted(string_length_frequency(arr)), sorted(["aa", "bb", "cc"]))

    def test_unique_lengths(self):
        arr = ["a", "bb", "ccc", "dddd"]
        self.assertEqual(sorted(string_length_frequency(arr)), ["a"])

    def test_empty_array(self):
        arr = []
        self.assertEqual(string_length_frequency(arr), [])

    def test_tie_for_max_frequency(self):
        arr = ["a", "b", "cc", "dd"]
        self.assertEqual(sorted(string_length_frequency(arr)), sorted(["a", "b"]))

    def test_single_element(self):
        arr = ["hello"]
        self.assertEqual(string_length_frequency(arr), ['hello'])

    def test_mixed(self):
        arr = ["a", "bb", "c", "dd", "e", "ff"]
        self.assertEqual(sorted(string_length_frequency(arr)), sorted(["a", "c", "e"]))

if __name__ == "__main__":
    unittest.main()
