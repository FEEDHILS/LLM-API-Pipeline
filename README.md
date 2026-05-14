# LLM-API-Pipeline
Аналитика Данных 5 семестр. 2 Лаб. работа - работа с API LLM (OpenAI SDK). Использовалась модель Xiaomi MiMo.

Позволяет анализировать отзывы с помощью LLM и выводить результат в удобном формате.
Скрипт поддерживает логирование (может быть полезно если, например, используется функция мышления).

## Инструкция
Рассмотрим основные файлы:
  - input.csv - csv файл с рецензиями (я взял лишь малую часть от большого датасета с Kaggle). Считывает соответствующий столбец.
  - output_struct.json - файл в котором вы напрямую можете повлиять на ответ LLM, указав в каком формате (и вообще какие) вам удобно получать данные.
  - output.json - выходной файл со списком элементов согласно структуре выше
  - config.py - позволяет указать столбец .csv который будет использован, вид модели, и макс. кол-во токенов на ответ.



Перед запуском скрипта следует создать .env файл в котором нужно ввести ваш ключ модели Xiaomi MiMo в переменнную `API_KEY`. В случае пользования другой моделью вы также можете указать переменную `API_URL`.

Запустите скрипт командой `python main.py` - по завершению работы проверьте output.json. По желанию можете проверить логи в папке logs.

## Пример
*Input:*

> "Probably my all-time favorite movie, a story of selflessness, sacrifice and dedication to a noble cause, but it's not preachy or boring.
> It just never gets old, despite my having seen it some 15 or more times in the last 25 years. Paul Lukas' performance brings tears to my eyes, and Bette Davis, in one of her very few truly sympathetic roles, is a delight.
> The kids are, as grandma says, more like dressed-up midgets than children, but that only makes them more fun to watch.
> And the mother's slow awakening to what's happening in the world and under her own roof is believable and startling. If I had a dozen thumbs, they'd all be up for this movie."

*Output:*
```
{
      "Тон": "Положительный",
      "Тема": "Восхищение фильмом, актерской игрой и сюжетом",
      "Название": "---"
},
```
