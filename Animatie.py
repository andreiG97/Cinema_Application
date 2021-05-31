from Movie import Movie

class Animatie(Movie):
    def __init__(self, title='', time='', subtitle=''):
        super().__init__(title, time)
        self.subtitle = subtitle

    # def add_movie(self, movie_list=[]):
    #     self.title = input('Insert movie name: ')
    #     self.time = int(input('Insert movie length in minutes, only integers: '))
    #     self.subtitle = input('Tell me what language do you need: ')
    #     if self.time <= 180:
    #         new_movie = {'Name': self.title, 'Time': self.time, 'Subtitle': self.subtitle}
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

# movie = Animatie()
# print(movie.add_movie())