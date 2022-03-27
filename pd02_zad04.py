# # Zadanie 4*
# Stwórz klasę Game, która będzie klasą bazową, z metodą z play, która ma w nazwie wskazywać,
# że nie należy jej modyfikować (metoda chroniona), oraz która wyświetla informację o rozpoczęciu gry.
# Dodatkowo ma zawierać liczbę graczy.
# Stwórz drugą klasę Hangman, która dziedziczy po klasie Game i pozwoli zagrać w grę wisielec,
# gdzie gracz musi odgadnąć słowo, podając pojedyncze litery.
# Gra ma umożliwiać wybór poziomu trudności (beginner, intermediate, advanced)
# i w zależności od wybranego poziomu, dostępna liczba błędnie odgadniętych liter ma być mniejsza.
# Np. dla poziomu beginner gracz może pomylić się 8 razy, intermediate 5 razy, a advanced 3 razy.
# W grze mamy też mieć możliwość wyboru liczby graczy,
# jeżeli jest jeden to słowo losowane jest z listy,
# a jeżeli dwóch graczy, to jeden wpisuje słowo do odgadnięcia, a drugi je zgaduje.
# Gra może być stworzona dla dowolnego języka, ale jeden język na grę (np. angielski).
# Zadanie 4 należy oddać w formacie .py, tak, żeby była możliwość uruchomienia i grania w terminalu.
# Do pobierania słów/znaków od użytkownika skorzystaj z metody gotowej metody input().
# Dodatkowo pamiętaj o obsłudze wyjątków, jeżeli np. to co wpisał w terminalu gracz jest spoza dopuszczalnej listy znaków.

import os
import time
import re

cls = lambda: os.system('cls' if os.name=='nt' else 'clear')


class Game():

    def __init__(self):
        pass

    def _play(self):
        print(f"LET'S PLAY")
        number_of_players = input('First things first, how many players are there? [1/2] ')
        while number_of_players not in ["1", "2"]:
            number_of_players = input('This game was designed for either 1 or 2 players, try again! [1/2] ')
        difficulty_level = input(
            '''Great! What difficulty level do you prefer?
            1 - easy (8 wrong guesses allowed)
            2 - medium (5 wrong guesses allowed)
            3 - hard (3 wrong guesses allowed)'''
        )
        while difficulty_level not in ["1", "2", "3"]:
            difficulty_level = input('You have to choose your difficulty level, try again! [1/2/3] ')
        print('Thank you!')
        print('Loading, please wait...')

        if difficulty_level == "1":
            self.mistakes_allowed = 8
        elif difficulty_level == "2":
            self.mistakes_allowed = 5
        else:
            self.mistakes_allowed = 3

        self.number_of_players = int(number_of_players)

class Hangman(Game):

    def __init__(self):
        self.words = ['welcome', 'peaceful', 'sixtieth', 'positively', 'hemorrhoid',\
                      'elephant', 'chemicals', 'envelope', 'impression', 'television']

    def run_game(self):
        self.main_play()
        play_again = input('Do you want to play again? [y/n]')
        while play_again not in ['y', 'n']:
            play_again = input('Do you want to play again? [y/n]')
        while play_again == 'y':
            self.main_play()
            play_again = input('Do you want to play again? [y/n]')
        print('Thank you for playing Hangman, goodbye!')

    def main_play(self):
        Game._play(self)
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        cls()
        if self.number_of_players == 1:
            print(f'Remember you can only play in one player mode {len(self.words)} times!')
            self.one_player_mode()
        else:
            self.two_player_mode()
        print('That was fun!')

    def letter_guessing(self):
        self.players_guess = ['_'] * len(self.target_word)
        while (self.mistakes_allowed > 0) and ('_' in self.players_guess):
            guessed_character = input("Guess a letter! ")
            while not guessed_character.isalpha():
                guessed_character = input("Guess a letter! ")
            guessed_character = guessed_character.lower()
            if guessed_character in self.target_word:
                indexes = [x.start() for x in re.finditer(guessed_character, self.target_word)]
                for x in indexes:
                    self.players_guess[x] = guessed_character
                print(
                    f'''YES! Good guess!
                    You have guessed these letters so far:
                    {' '.join(self.players_guess)}
                    '''
                )

            else:
                self.mistakes_allowed -= 1
                print(
                    f'''NO! You did not guess correctly!
                    You have guessed these letters so far:
                    {' '.join(self.players_guess)}
                    '''
                )
        if self.mistakes_allowed == 0:
            print("OH NO! You made too many mistakes, GAME OVER!")
        else:
            print("CONGRATULATIONS! You won!")

    def one_player_mode(self):
        self.target_word = self.words.pop()
        print(
            f'''You have to guess a word I chose for you!
            The word is {len(self.target_word)} letters long.
            You will be asked to guess one letter at a time,
            you are allowed to guess wrong {self.mistakes_allowed} times
            Let's play!'''
        )
        self.letter_guessing()

    def two_player_mode(self):
        print('Player one!')
        self.target_word = input('What word do you want player two to guess? ')
        while not self.target_word.isalpha():
            self.target_word = input('Remember only letters are allowed ')
        self.target_word = self.target_word.lower()
        print('Thank you, now I will hide your input from player one in')
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        cls()
        print('Player two! Your turn!')
        self.letter_guessing()

if __name__ == "__main__":
    Hangman = Hangman()
    Hangman.run_game()