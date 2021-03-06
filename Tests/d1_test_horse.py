import unittest
import Tasks.d1_horse as horse


class MyTestCase(unittest.TestCase):
	def test_1(self):
		self.assertEqual(horse.calculate_paths((8, 8), (7, 7)), 14,
						 msg="Something gonna wrong...")

	def test_2(self):
		self.assertEqual(horse.calculate_paths((9, 9), (8, 8)), 27,
						 msg="Just because...")

	def test_3(self):
		self.assertEqual(horse.calculate_paths((17, 12), (16, 9)), 64137,
						 msg="Oo")

	def test_4(self):
		self.assertEqual(horse.calculate_paths((12, 10), (11, 9)), 324,
						 msg=":)")


if __name__ == '__main__':
	unittest.main()
