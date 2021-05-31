from Cinema import Cinema

cinema = Cinema()


def show_menu():
    print('1. Adauga drama')
    print('2. Adauga animatie')
    print('3. Afiseaza lista filme')
    print('4. Afiseaza desene animate')
    print('5. Shuffle')
    print('6. Exit')


show_menu()
select_option = int(input("Enter option: "))

while select_option != 6:
    if select_option == 1:
        cinema.save_movie(cinema.add_movie_drama())
    elif select_option == 2:
        cinema.save_movie(cinema.add_movie_animation())
    elif select_option == 3:
        print(cinema.show_movies())
    elif select_option == 4:
        print(cinema.show_animations())
    elif select_option == 5:
        print(cinema.random_movie(cinema.show_movies()))

    show_menu()
    select_option = int(input("Enter option: "))

