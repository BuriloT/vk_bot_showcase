import os

sections_data = ['Торты', 'Хлебобулочные изделия', 'Шоколад']


products_data = [
    {
        'name': 'Королевское угощение',
        'description': 'Торт "Королевское угощение" 500 г.',
        'photo': os.path.join('static', 'Cake1.jpg'),
        'section_id': 1
     },
    {
        'name': 'Сказочная страна',
        'description': 'Торт "Сказочная страна" 1 кг.',
        'photo': os.path.join('static', 'Cake2.jpg'),
        'section_id': 1
    },
    {
        'name': 'Эстерхази',
        'description': 'Торт "Эстерхази" 800 г.',
        'photo': os.path.join('static', 'Cake3.jpg'),
        'section_id': 1
    },
    {
        'name': 'Хачапури',
        'description': 'Изделие булочное "Хачапури" 400 г.',
        'photo': os.path.join('static', 'Bakery1.jpg'),
        'section_id': 2
    },
    {
        'name': 'Столица',
        'description': 'Ватрушка «Столица» В/С 90 г.',
        'photo': os.path.join('static', 'Bakery2.jpg'),
        'section_id': 2
    },
    {
        'name': 'Сладкий снег',
        'description': 'Булочка "Сладкий снег" в/с 100 г.',
        'photo': os.path.join('static', 'Bakery3.png'),
        'section_id': 2
    },
    {
        'name': 'Горький (Черный)',
        'description': 'Самый полезный шоколад.',
        'photo': os.path.join('static', 'Chocolate1.jpg'),
        'section_id': 3
    },
    {
        'name': 'Молочный',
        'description': 'В молочном шоколаде какао-массы от 35 до 45%.',
        'photo': os.path.join('static', 'Chocolate2.jpg'),
        'section_id': 3
    },
    {
        'name': 'Белый',
        'description': 'Основу белого шоколада составляют молочные продукты.',
        'photo': os.path.join('static', 'Chocolate3.jpg'),
        'section_id': 3
    },
]
