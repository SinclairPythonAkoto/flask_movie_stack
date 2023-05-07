from flask import Flask, jsonify, url_for, request
from movie_stack.utils import Solution

app = Flask(__name__)


@app.route('/')
def index():
    solution = Solution()
    movies_array = solution.run(3, 3, [3,1,1])
    return f"python akoto hello world: {movies_array}"


if '__main__' == __name__:
    app.run(debug=True)