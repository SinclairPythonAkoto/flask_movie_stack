class Solution:

    def run(self, n, m, movies):
        stack = list(range(1, n+1))
        movies_array = []

        for movie in range(m):
            movie_index = stack.index(movies[movie])
            movies_array.append(movie_index)
            stack.pop(movie_index)
            stack.insert(0, movies[movie])
        return ','.join(str(x) for x in movies_array)