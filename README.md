# Лингвистический анализатор текста
Консольный инструмент для базового анализа текстовых данных. Считает предложения, частотность слов, очищает ввод от пунктуации. Решает задачу препроцессинга и визуализации лингвистических метрик без сторонних NLP-библиотек.

## Команда и роли
| Участник | Роль | Ветка | Основные функции 
|----------|------|-------|------------------
| Чудинова В. | Тимлид | main | Архитектура, интеграция, мерж, README 
| Канашина К. | Аналитик | feature/programmer-analyst | clean_text, `get_word_frequency`, `count_sentences` 
| Брюгдикова В. | Аналитик | origin/programmer-test | clean_text, `get_word_frequency`, `count_sentences` 
| Перепада А. | UI/Тестировщик | feature/ui | print_header, get_user_input, format_results 

## Как запустить проект
1. Склонируйте репозиторий: git clone <url>
2. Создайте виртуальное окружение: python -m venv .venv
3. Активируйте: source .venv/bin/activate (Linux/macOS) или .venv\Scripts\activate (Windows)
4. Установите зависимости: pip install -r requirements.txt
5. Запустите: python main.py

## Технологии и модули
- Python 3.10+
- Стандартные модули: string, collections, datetime
- Без сторонних NLP-библиотек

## Структура репозитория
project/
├── README.md           # описание, как запустить
├── requirements.txt    # зависимости (пустой, практика работы с pip)
├── main.py                    # точка входа
└── modules/                  # собственные модули команды
    ├── text_processor.py
    └── menu_ui.py

