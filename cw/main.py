from classes.BasicWord import BasicWord
from classes.Player import Player
from utils import get_random_word

PATH = "https://jsonkeeper.com/b/99JK"

print("Введите имя игрока")
name = input()

player = Player(name)
basic_word = get_random_word(PATH)

print(f"Привет, {player.name}")

print(f"Составьте {basic_word.count_sub_words()} слов из слова {basic_word.original_word.upper()}")
print(f"Слова должны быть не короче 3 букв")
print(f"Поехали, ваше первое слово?")

while player.count_used_words() < basic_word.count_sub_words():
    user_input = input().lower()

    if user_input in ["stop", "стоп"]:
        break

    if not basic_word.correct_answer(user_input):
        print("Такого слова нет")
        continue

    if player.check_use(user_input):
        print("Такое слово уже использовано")
        continue
    player.add_words(user_input)
    print("Верно")

print("игра завершена!")
print(f"Вы угадали {player.count_used_words()} слов")
