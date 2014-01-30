import unittest
import triangle_solver

sample_input = """9235"""
sample_input_2 = """9235
9096 637"""


class ParserTest(unittest.TestCase):

	def setUp(self):
		self.parser = triangle_solver.Parser()

	def test_parse_one_line(self):
		parsed = self.parser.parse(sample_input)
		self.assertEqual(parsed, [[9235]])

	def test_solve_multiline(self):
		parsed = self.parser.parse(sample_input_2)
		self.assertEqual(parsed, [[9235], [9096, 637]])


class TriangleSolverTest(unittest.TestCase):

	def solve_triangle(self, triangle):
		return triangle_solver.TriangleSolver(triangle).solve()

	def test_can_solve_on_row(self):
		triangle = [[9235]]
		result = self.solve_triangle(triangle)
		self.assertEqual(result, 9235)

	def test_can_solve_two_rows(self):
		triangle = [[50], [1, 2]]
		result = self.solve_triangle(triangle)
		self.assertEqual(result, 52)

	def test_can_solve_three_rows(self):
		triangle = [[1], [1, 2], [3, 4, 5]]
		result = self.solve_triangle(triangle)
		self.assertEqual(result, 8)


if __name__ == '__main__':
	 unittest.main()
