import pytest
from movie_stack.utils.solution import Solution

def test_run():
    solution = Solution()
    n = 3
    m = 3
    movies = [3, 1, 1]
    expected_output = "2,1,0"
    assert solution.run(n, m, movies) == expected_output