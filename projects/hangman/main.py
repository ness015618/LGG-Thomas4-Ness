from utils.game import Hangman

game1 = Hangman()
print(game1.word_to_find, game1.lives, game1.correctly_guessed_letters, game1.wrongly_guessed_letters, game1.turn_count, game1.error_count)
