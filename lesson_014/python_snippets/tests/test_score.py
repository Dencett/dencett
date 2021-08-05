import unittest

from bowling import Bowling


class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.bowling = Bowling('12-/XXXXX---9X')

    def test_gets_score(self):
        self.total_score = 147
        result = self.bowling.gets_score()
        self.assertEqual(result, self.total_score)


if __name__ == '__main__':
    unittest.main()
