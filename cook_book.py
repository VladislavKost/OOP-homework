def get_ingredients_from_file():
    "Функция открывает файл и считывает данные из него"
    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as f:
        while True:
            first_line = f.readline().strip()
            if first_line != '':
                ingredients = []
                cook_book[first_line] = ingredients
                for ing in range(int(f.readline().strip())):
                    ingredient_name, quantity, measure = f.readline().strip().split(' | ')
                    amount = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                    ingredients.append(amount)
                f.readline().strip()
            else:
                break
    return cook_book


# print(get_ingredients_from_file())


def get_shop_list_dishes(dishes, person_count=1):
    "Функция создает список покупок на основе введеных данных"
    cook_book = get_ingredients_from_file()
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                amount = {}
                ingredient_name, quantity, measure = ingredients.values()
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += int(quantity) * person_count
                else:
                    amount = {'measure': measure, 'quantity': (int(quantity) * person_count)}
                    shop_list[ingredient_name] = amount
        else:
            print(f'Блюда под названием {dish} нет в списке блюд')
    return shop_list


# print(get_shop_list_dishes(['Омлет', 'Фахитос', 'Мясо по-французски', 'Запеченный картофель'], 5))


def merging_files():
    "Функция открывает 3 файла, сортирует их и создает конечный результат в отдельном файле"
    files = []
    for file in ['1.txt', '2.txt', '3.txt']:
        data = {}
        with open(file, encoding='utf-8') as f:
            text = f.read()
            lines = text.count('\n') + 1
            data = {'name': file, 'lines': lines, 'text': text}
        files.append(data)
    sorted_files = sorted(files, key=lambda length: length['lines'])

    with open('result.txt', 'w', encoding='utf-8') as result:
        for file in sorted_files:
            result.write(f'{file["name"]}\n')
            result.write(str(f'{file["lines"]}\n'))
            result.write(f'{file["text"]}\n')

# merging_files()