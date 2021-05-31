class Movie:
    def __init__(self, title='', time=''):
        self.title = title
        self.time = time

    # def add_movie(self, movie_list = []):
    #     self.title = input('Insert movie name: ')
    #     self.time = int(input('Insert movie length in minutes, only integers: '))
    #     if self.time <= 180:
    #         new_movie = {'Name': self.title, 'Time': self.time}
    #         movie_list.append(new_movie)
    #     else:
    #         raise ValueError('Durata nu trebuie sa depaseasca 180 min')
    #     return movie_list
    #
    # def save_movie(self, movie_list):
    #     with open("MovieList.txt", 'wt') as my_movies:
    #         for movie in movie_list:
    #             for key, value in movie.items():
    #                 my_movies.write('%s:%s\n' % (key, value))

    # def show_movies(self, file='MovieList.txt'):
    #     with open(file) as movie_files:
    #         movie_list = movie_files.readlines()
    #
    #     return movie_list

# movie = Movie()
# movie.save_movie(movie.add_movie())
# movie2 = Movie()
# movie2.save_movie(movie2.add_movie())

