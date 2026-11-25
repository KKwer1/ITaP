import json
from pathlib import Path

PLAN_FILE = "plan.txt"
BOOKS_FILE = "books.json"
OUTPUT_FILE = "filtered.json"

KEYWORD = "план"
YEAR_LIMIT = 2000


def count_plan_lines(filename):
    path = Path(filename)
    if not path.exists():
        print(f"Ошибка: файл {filename} не найден.")
        return 0, 0

    total_lines = 0
    plan_count = 0

    with open(path, encoding="utf-8") as f:
        for line in f:
            text = line.strip()
            if text == "":
                continue
            total_lines += 1
            if KEYWORD in text.lower():
                plan_count += 1

    return total_lines, plan_count


def filter_books(filename, year_limit):
    path = Path(filename)
    if not path.exists():
        print(f"Ошибка: файл {filename} не найден.")
        return []

    with open(path, encoding="utf-8") as f:
        books = json.load(f)

    filtered = []
    invalid_count = 0

    for book in books:
        year = book.get("year")
        if year is None:
            invalid_count += 1
            continue
        try:
            year = int(year)
        except (TypeError, ValueError):
            invalid_count += 1
            continue

        if year > year_limit:
            filtered.append(book)

    print(f"Пропущено книг с некорректным годом: {invalid_count}")
    return filtered


def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    total, plan_mentions = count_plan_lines(PLAN_FILE)
    print(f"Непустых строк в plan.txt: {total}")
    print(f"Строк со словом «план»: {plan_mentions}")
    filtered_books = filter_books(BOOKS_FILE, YEAR_LIMIT)
    print(f"Книг после {YEAR_LIMIT} года: {len(filtered_books)}")
    save_json(OUTPUT_FILE, filtered_books)
    print(f"Результат сохранён в {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
