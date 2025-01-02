from Solution import Solution
from timeout_decorator import timeout
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {1: (["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]], [2,3,0]),
                            2: (["a","e","i"], [[0,2],[0,1],[2,2]], [3,2,1])}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_1(self):
        words, queries, outputs = self.__testcases[1]
        results = self.__obj.vowelStrings(words = words, queries = queries)
        self.assertIsInstance(results, list)
        self.assertTrue(all(r == o for r, o in zip(results, outputs)))

    @timeout(0.5)
    def test_case_2(self):
        words, queries, outputs = self.__testcases[2]
        results = self.__obj.vowelStrings(words = words, queries = queries)
        self.assertIsInstance(results, list)
        self.assertTrue(all(r == o for r, o in zip(results, outputs)))

if __name__ == '__main__': unittest.main()