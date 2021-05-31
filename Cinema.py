from Animatie import Animatie
from Drama import Drama
import random


class Cinema(Animatie, Drama):

    def __init__(self):
        super(Drama, self).__init__()
        super(Animatie, self).__init__()

    def add_movie_drama(self, movie_list=[]):
        self.title = input('Insert movie name: ')
        self.time = int(input('Insert movie length in minutes, only integers: '))
        self.age = int(input('Age restrict: '))
        if self.time <= 180:
            new_movie = {'{} {}, age restrict {}'.format(self.title, self.time, self.age)}
            movie_list.append(new_movie)
        else:
            raise ValueError('Durata nu trebuie sa depaseasca 180 min')
        return movie_list

    def add_movie_animation(self, movie_list=[]):
        self.title = input('Insert movie name: ')
        self.time = int(input('Insert movie length in minutes, only integers: '))
        self.subtitle = input('Tell me what language do you need: ')
        if self.time <= 180:
            new_movie = {'{} {}, subtitle {}'.format(self.title, self.time, self.subtitle) }
            movie_list.append(new_movie)
        else:
            raise ValueError('Durata nu trebuie sa depaseasca 180 min')
        return movie_list

    def save_movie(self, movie_list):
        with open("MovieList.txt", 'at') as my_movies:
            for movie in movie_list:
                movie = str(movie)
                my_movies.write('{}\n'.format(movie))

    def show_movies(self, file='MovieList.txt'):
        new_list = []
        with open(file) as movie_files:
            movie_list = movie_files.readlines()
        for i in movie_list:

            new_list.append(i.strip('\n'))
        return new_list

    def show_animations(self, file='MovieList.txt'):
        new_list = []
        with open(file) as movie_files:
            movie_list = movie_files.readlines()
        for i in movie_list:
            if i.find('subtitle') == -1:
                pass
            else:
                new_list.append(i.strip('\n'))

        return new_list

    def random_movie(self, movie_list):
        random_index = random.randint(0, len(movie_list)-1)
        return movie_list[random_index]




