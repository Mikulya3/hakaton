import datetime
  
data = [
    {
        'id': 1,
        'name': 'product1',
        'price': 100,
        'created_at': datetime.datetime(2022, 10, 4),
        'update':datetime.datetime.now(),
        'description':'product for home',
        'is_active': 'active'
    },
    {   'id': 2,
        'name': 'product2',
        'price': 50,
        'created_at': datetime.datetime(2022, 10, 4),
        'update':datetime.datetime.now(),
        'description':'product for home',
        'is_active': 'not active'
        
    },
    {
        'id': 3,
        'name': 'product3',
        'price': 60,
        'created_at': datetime.datetime(2022, 10, 4),
        'update':datetime.datetime.now(),
        'description':'product for home',
        'is_active': 'active'
    }
]

def get_products():
    return data

def get_one_product(id): # 
    product = [i for i in data if id == i['id']]
    if product:
        return product[0]
    return 'Нет такого продукта!'


def post_product():
    max_id = max([i['id'] for i in data]) 
    new_data = {
        'id': max_id + 1,
        'name': input('Введите имя товара: '),
        'price': int(input('Введите цену: ')),
        'created_at': datetime.datetime.now(),
        'is_active': True
    }
    data.append(new_data)
    
    return f'Вы добавли новый товар:\n {new_data}'

def delete_product(id): 
    delete_product = [i for i in data if i['id'] == id] 
    if delete_product:
        data.remove(delete_product[0]) 
        return 'Успешно удален!'
    return 'Нет такого продукта!'


def update_product(id): 
    update_product = [i for i in data if i['id'] == id] 
    
    if update_product:
        index_item = data.index(update_product[0]) 
        if input('Хотите обновить имя?: ') == 'Да':
            data[index_item]['name'] = input('Введите новое имя: ')
        if input('Хотите обновить цену?: ') == 'Да':
            data[index_item]['price'] = int(input('Введите новую цену: ')) 
        return 'Удачно обновили!'   
    return 'Нет такого продукта!'

def sort_pricelow():
    sort_pricelow=[i for i in data if i['price']<60]
    if input('Хотите посмотреть товары ниже 60 сом?: ')=="Да":
        return sort_pricelow    


def sort_pricehign():
    sort_pricehign=[i for i in data if i['price']>60]
    if input('Хотите посмотреть товары выше 60 сом?: ')=="Да":
        return sort_pricehign


def sort_status():
    sort_status=[True if i['is_active']=='active' else False  for i in data ] 
    if input('Хотите узнать есть ли товар в наличии?: ')=="Да":
            return sort_status
    return 'В наличии нет'

def sort_time():
    sort_time=[i if i['created_at']==input() else 'этот товар пришел позже' for i in data ]
    if input('Хотите узнать дату создания товара?: ')=="Да":
        return sort_time
    return 'Такого товара нет!'


def main():
    while True:
        print('Привет вот функцонал: \n1 - получить все товары \n2 - получить определенный товар \n3 - создать товар \n4 - удалить товар \n5 - обновить товар \n6 - товары ниже 60 сом \n7 - товары выше 60 сом \n8 - товар в наличии \n9-товары по дате создания')
        method = input('Введи число: ')
        if method == '1':
            print(get_products())
        elif method == '2':
            id = int(input('Введи id товара: '))
            print(get_one_product(id))
        elif method == '3':
            print(post_product())
        elif method == '4':
            id = int(input('Введите id товара который хотите удалить: '))
            print(delete_product(id))
        elif method == '5':
            id = int(input('Введите id товара который хотите обновить: '))
            print(update_product(id))
        elif method == '6':
            print(sort_pricelow())
        elif method == '7':
            print(sort_pricehign())
        elif method == '8':
            print(sort_status())
        elif method == '9':
            print(sort_time())
        else:
            print('Нет такого функционала!')

if __name__== '__main__':
    main()


import json
with open('testik.py') as my_file:  
    with open('example.json','w') as file:
        data=json.dump(my_file) 
        print(data)
