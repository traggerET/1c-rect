import unittest

from classes.findimage import FindImage


class TestStringMethods(unittest.TestCase):

    def test_answer_inside_row(self):
        self.assertEqual(FindImage([[0, 1, 2],
                                    [3, 2, 5],
                                    [6, 7, 8],
                                    [8, 9, 4],
                                    [0, 8, 8]],
                                   [[8, 8]]), [1, 4])

    def test_simple(self):
        self.assertEqual(FindImage([[3, 2, 5, 5],
                                    [6, 7, 8, 4],
                                    [8, 9, 4, 2],
                                    [0, 8, 8, 1]],
                                   [[7, 8],
                                    [9, 4]]), [1, 1])

    def test_single(self):
        self.assertEqual(FindImage([[3, 2, 5, 5],
                                    [6, 7, 8, 4],
                                    [8, 9, 4, 2],
                                    [0, 8, 8, 1]],
                                   [[8]]), [2, 3])


if __name__ == '__main__':
    unittest.main()
