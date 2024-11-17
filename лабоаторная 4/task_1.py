# TODO решите задачу
import json


def task() -> float:
    with open('input.json') as  file: # открытие файла для чтения в формате json
        data = json.load(file)
        total_sum = sum(item['score'] * item['weight'] for item in data if 'score' in item and 'weight' in item)
        return round(total_sum, 3)
    result = task('data.json')
    print(result)


print(task())
