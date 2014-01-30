class Parser(object):

	def parse(self, raw_triangle):
		parsed_triangle = []

		for raw_row in self._strip_and_split(raw_triangle, '\n'):
			row = []
			for raw_number in self._strip_and_split(raw_row, ' '):
				row.append(int(raw_number))
			parsed_triangle.append(row)

		return parsed_triangle

	def _strip_and_split(self, string, split_on_string):
		return string.strip().split(split_on_string)


class TriangleSolver(object):

	def __init__(self, triangle):
		self._triangle = triangle
		self._current_sums = []

	def solve(self):
		self._initialize_current_sums_with_first_row()
		self._step_through_triangle_and_update_current_sums()
		return max(self._current_sums)

	def _initialize_current_sums_with_first_row(self):
		first_row = self._triangle[0]
		for value in first_row:
			self._current_sums.append(value)

	def _step_through_triangle_and_update_current_sums(self):
		for row in self._triangle[1:]:
			new_current_sums = []
			for position, value in enumerate(row):
				max_sum_for_position_above = self._get_new_max_sum_for_position(position)
				new_current_sums.append(max_sum_for_position_above + value)
			self._current_sums = new_current_sums

	def _get_new_max_sum_for_position(self, position):
		if position == len(self._current_sums):
			max_sum_for_position_above = self._current_sums[position - 1]
		elif position == 0:
			max_sum_for_position_above = self._current_sums[position]
		else:
			max_sum_for_position_above = max((
				self._current_sums[position],
				self._current_sums[position - 1]
			))
		return max_sum_for_position_above


if __name__ == '__main__':
	with open('triangle.txt') as triangle_file:
		raw_triangle = triangle_file.read()
	triangle = Parser().parse(raw_triangle)
	solver = TriangleSolver(triangle)
	print solver.solve()
