# Парсер статей с Pedsovet.org

Это парсер, который получает HTML главной страницы сайта https://pedsovet.org/ и извлекает карточки статей:
- название статьи;
- ссылку на полную статью.

Результат выводится в формате JSON.

---

## Функционал

- Загружает HTML главной страницы с помощью `requests`.
- Находит карточки статей через CSS-селекторы.
- Корректно собирает текст и абсолютные ссылки.
- Убирает дубликаты.
- Выводит результат в консоль или сохраняет в JSON.

---

## Установка и запуск

# 1. Клонировать репозиторий

``` bash
git clone https://github.com/stasnav/project_ranepa.git
cd project_ranepa
```

# 2. Создать виртуальное окружение

``` bash
python3 -m venv venv
source venv/bin/activate       # macOS / Linux
# или
venv\Scripts\activate        # Windows
```

# 3. Установить зависимости

``` bash
pip install -r requirements.txt
```

# 4. Запустить парсер

``` bash
python3 parse_pedagogy.py
```

Результат появится в консоли в виде JSON.

## Пример результата

```json
[
  {
    "title": "5 растений, которые можно сажать в феврале",
    "url": "https://pedsovet.org/article/5-rastenij-kotorye-mozno-sazat-v-fevrale"
  }
]
