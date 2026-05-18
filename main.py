import string
from collections import Counter

# ---------- Шаг 1: загрузка текста ----------
print("=== Инструмент анализа стиля текста ===\n")
print("Введите ваш текст (для завершения ввода оставьте пустую строку и нажмите Enter):")

lines = []
while True:
    line = input()
    if line == "":
        if len(lines) > 0:
            break
        else:
            print("Вы ещё не ввели ни одной строки. Введите текст:")
            continue
    lines.append(line)

text = "\n".join(lines)

# ---------- Шаг 2: очистка ----------
def clean_text(raw_text):
    raw_text = raw_text.lower()
    # Удаляем всё, кроме букв, цифр, пробелов и апострофа
    punctuation_without_apostrophe = string.punctuation.replace("'", "")
    translator = str.maketrans(punctuation_without_apostrophe, ' ' * len(punctuation_without_apostrophe))
    cleaned = raw_text.translate(translator)
    words = cleaned.split()
    return words

words = clean_text(text)

# ---------- Шаг 3: подсчёт частот ----------
counter = Counter(words)

# ---------- Вывод топ-10 ----------
print("\n--- Результаты анализа ---")
if not words:
    print("Текст не содержит слов.")
else:
    print(f"Всего уникальных слов: {len(counter)}")
    print(f"Всего слов (с повторениями): {len(words)}")
    print("\nТоп-10 самых частых слов:")
    print("Слово".ljust(15) + "Частота")
    print("-" * 25)
    for word, count in counter.most_common(10):
        print(f"{word.ljust(15)} {count}")