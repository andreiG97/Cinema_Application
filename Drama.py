from Movie import Movie


class Drama(Movie):
    def __init__(self, title='', time='', age=''):
        super().__init__(title, time)
        self.age = age

    # def add_movie(self, movie_list=[]):
    #     self.title = input('Insert movie name: ')
    #     self.time = int(input('Insert movie length in minutes, only integers: '))
    #     self.age = int(input('Age restrict: '))
    #     if self.time <= 180:
    #         new_movie = {'Name': self.title, 'Time': self.time, 'Age restriction:': self.age}
    #         movie_list.append(new_movie)
    #     else:
    #         raise ValueError('Durata nu trebuie sa depaseasca 180 min')
    #     return movie_list
    #
    # def save_movie(self, movie_list):
    #     with open("MovieList.txt", 'at') as my_movies:
    #         for movie in movie_list:
    #             for key, value in movie.items():
    #                 my_movies.write('%s:%s\n' % (key, value))

# movie = Drama()
# print(movie.add_movie())