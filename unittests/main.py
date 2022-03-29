import unittest

from ImagesProcess.image_processing import FindImage


class TestStringMethods(unittest.TestCase):

    def test_answer_inside_row(self):
        self.assertEqual(FindImage([(0, 1, 2),
                                    (3, 2, 5),
                                    (6, 7, 8),
                                    (8, 9, 4),
                                    (0, 8, 8)],
                                    [(8, 8)]), [1, 4])

    def test_simple(self):
        self.assertEqual(FindImage([(3, 2, 5, 5),
                                    (6, 7, 8, 4),
                                    (8, 9, 4, 2),
                                    (0, 8, 8, 1)],
                                   [(7, 8),
                                    (9, 4)]), [1, 1])

    def test_single(self):
        self.assertEqual(FindImage([(3, 2, 5, 5),
                                    (6, 7, 2, 4),
                                    (9, 9, 4, 2),
                                    (0, 1, 8, 1)],
                                   [(8,)]), [2, 3])

    def test_not_accurate(self):
        self.assertEqual(FindImage([(3, 2, 5, 5),
                                    (6, 7, 2, 4),
                                    (9, 9, 4, 2),
                                    (0, 1, 8, 1)],
                                   [(7, 2),
                                    (9, 4),
                                    (1, 8)], inaccuracy=2), [1, 1])


if __name__ == '__main__':
    unittest.main()
