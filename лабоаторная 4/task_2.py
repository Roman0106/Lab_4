# TODO импортировать необходимые молули

import csv

import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(csv_file_path) -> None:

      # TODO считать содержимое csv файла
    with open(csv_file_path,mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)

        data = [row for row in reader]
    json_data = json.dumps(data, indent=4) # Запись в JSON файл с отступами
     # TODO Сериализовать в файл с отступами равными 4

    print(json_data, end="")

csv_file_path = 'input.csv'

if __name__ == '__main__':
    # Нужно для проверки
    task(csv_file_path)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
