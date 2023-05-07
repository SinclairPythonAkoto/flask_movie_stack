from flask import Flask, jsonify, url_for, request, render_template
from movie_stack.utils.solution import Solution

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calculate_movies_array():
    if request.method == 'GET':
        return render_template('calculate_movies.html')
    n = int(request.form['n'])
    m = int(request.form['m'])
    movies = [int(movie) for movie in request.form.getlist('movies[]')]
    solution = Solution()
    movies_array = solution.run(n, m, movies)
    return movies_array


if '__main__' == __name__:
    app.run(debug=True)