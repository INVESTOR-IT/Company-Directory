<h1 align="center"> 
    Company-Directory
</h1>

<div align="center">
    <img src="https://img.shields.io/badge/Python-3.11-blue">
    <img src="https://img.shields.io/badge/Version-v1.0_(Alpha)-green">
    <img src="https://img.shields.io/badge/License-MIT-red">
</div>

</br>

## Описание
Сервис реализован для записи и хранение в PostgreSQL данные в виде оргеназиций,
которые имеют вид деятельности и здание, в котором они находятся
Сервис позволяет создать организацию и присвоить ей вид деятельности и здание

</br>

## Документация 
### Структура проекта
```
├── app
│   ├── api
│   │   ├── organizations.py         # Эндпоинты авторизации
│   │   ├── request_model.py         # Эндпоинты авторизации
│   │   └── response_model.py        # Логика сервиса авторизации
│   ├── database
│   │   ├── database.py              # Инициализация БД
│   │   └── model.py                 # Модель БД
│   ├── services
│   │   └── organizations.py         # Логика сервиса
│   ├── config.py                    # Settings для приложения
│   └── main.py                      # Главный файл
├── .env.example                     # Пример файла переменных окружения
├── .gitignore                       # Игнорирование для git
├── .dockerignore                    # Игнорирование для Docker
├── Dockerfile                       # Dockerfile для API сервиса
├── requirements.txt                 # Зависимости Python
└── README.md                        # Документация проекта
```

</br>

### Deploy
Перед запуском в .env копируем `URL_DATABSE` из .env.example<br>
```
docker-compose up --build
```
Для проверки БД пополняется тестовыми данными благодаря `seed_data.py`, 
`docker-entrypoint.sh` и `Dockerfile`, если тестовые данные не требуются, то в 
`Dockerfile` можно убрать 7-11 строчку, 16 и 17, тогда `docker-entrypoint.sh` 
не будет вызываться при развертывание

</br>

### Эндпоинты
#### Root
- GET `http://localhost:8000` - Документация OpenAPI
#### Organizations
- GET `http://localhost:8000/organizations_using_house` - Список организаций в здании
- GET `http://localhost:8000/organizations_using_activity` - Список организаций с определенным вид деятельности
- GET `http://localhost:8000/organizations_using_id` - Организации с определенным индификатором
- GET `http://localhost:8000/organizations_using_name` - Список организаций по название организиции
- GET `http://localhost:8000/organizations_using_coordinate` - Список организации в области поиска
Поиск осуществляется квадратом (1 вариант) или кругом (2 вариант), параметры передаем Json теле
```
{
    "longitude": 50,
    "latitude": 50,
    "height": 5,
    "width": 5
}
```
или
```
{
    "longitude": 50,
    "latitude": 50,
    "radius": 5
}
```

</br>

Визуальная часть тестовых данных в БД</br>
**Organizations**
| id | names         | phones                    | hauses_id | activites_id |
| -  | -             | -                         | -         | -            |
| 1  | Мясная        | +71234567890;+73243432421 | 1         | 3            |
| 2  | Столовая      | +73132125412;+71231414132 | 2         | 1            |
| 3  | Рено          | +71432214132              | 4         | 5            |
| 4  | Все для машин | +71234567890;+73243432421 | 3         | 8            |

<br>

**Houses**
| id | address                       | londgitude  | latitude |
| -  | -                             | -           | -        |
| 1  | г. Москва, Верхняя улица, д 1 | 55          | 40       | 
| 2  | г. Москва, Нижняя улица, д 2  | 50          | 45       |
| 3  | г. Москва, Правая улица, д 3  | 40          | 50       |
| 4  | г. Москва, Левая улица, д 4   | 50          | 40       |

<br>

**Activities**
| id | names              | paren_id |
| -  | -                  | -        |
| 1  | Еда                | null     |
| 2  | Автомобили         | null     |
| 3  | Мясная продукция   | 1        |
| 4  | Молочная продукция | 1        |
| 5  | Легковые           | 2        |
| 6  | Грузовые           | 2        |
| 7  | Запчасти           | 5        |
| 8  | Аксесуары          | 5        |

</br>

## Лицензия 
Проект распростроняется под лецензией MIT