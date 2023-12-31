import os
# name_file, __ = os.path.splitext(filename)
# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }
# print (cook_book['Омлет'])

# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }

cook_book = {}
dict_ingredients = {}
dict_data_txt = {}
with open('recipes.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
    data1 = []
    lst_book = []
    i = 2 
    for string in data:
        if string != '\n':
            data1.append(string.strip())     
        if string == '\n' or string == data[-1]:
            for item in data1[i:]:
                ingredient_name, quantity, measure = item.strip().split('|')
                lst_book.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
                i += 1 
            cook_book[data1[0]] = list(lst_book)
            i = 2 
            lst_book.clear() 
            data1.clear()
print(f'Задание №1\n {cook_book}')           

def get_shop_list_by_dishes(dishes, person_count):
    i = 0
    for di in dishes:
        splist_ingredient = (cook_book[di])
        i = 0
        for ingr in splist_ingredient:
            list_dic_ingredients=dict({'measure': splist_ingredient[i]['measure'], 'quantity': (splist_ingredient[i]['quantity']*person_count)})
            dict_ingredients[splist_ingredient[i]['ingredient_name']] = list_dic_ingredients
            i += 1 
    return dict_ingredients

dish = ['Запеченный картофель','Омлет']
print(f'Задание №2\n {get_shop_list_by_dishes(dish,2)}') 

with open('1.txt', 'r', encoding='utf-8') as file:
    path = os.path.join(os.getcwd(), '1.txt')
    tail = os.path.split(path)
    # print("Путь файла " + path)
    # print("Имя файла " + tail[1])
    row_counter = 0
    data = file.readlines()
    
    for line in data:
        row_counter += 1
    data.insert(0,tail[1] + '\n')
    data.append('\n')     
    dict_data_txt[row_counter] = data

with open('2.txt', 'r', encoding='utf-8') as file:
    path = os.path.join(os.getcwd(), '2.txt')
    tail = os.path.split(path)
    row_counter = 0
    data = file.readlines()
    for line in data:
        row_counter += 1
    data.insert(0,tail[1]+ '\n')
    data.append('\n')    
    dict_data_txt[row_counter] = data

with open('3.txt', 'r', encoding='utf-8') as file:
    path = os.path.join(os.getcwd(), '3.txt')
    tail = os.path.split(path)
    row_counter = 0
    data = file.readlines()
    for line in data:
        row_counter += 1
    data.insert(0,tail[1]+ '\n') 
    data.append('\n')       
    dict_data_txt[row_counter] = data

sorted_dict_data = dict(sorted(dict_data_txt.items()))
finish_text = str(sorted_dict_data)

def dict_to_string(data_dict):
    result = ""
    for key, value in data_dict.items():
        result += f"{''.join(value[0])}{key}\n{''.join(value[1:])}"
    return result

with open('finish.txt', 'w', encoding='utf-8') as file:
    file.write(dict_to_string(sorted_dict_data))

print(f'Задание №3\n{dict_to_string(sorted_dict_data)}')   