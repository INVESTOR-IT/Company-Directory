<h1 align="center"> Company-Directory </h1>

**Deploy:**
Перед запуском в .env копируем `URL_DATABSE` из .env.example
`docker-compose up --build`

---

**Docker-compose**
В `docker-compose.yaml` установлен порт 5433 для предотвращения конфликта с БД на машине

---
**Для пополнения БД тест данными**
`http://localhost:8000/start` - временный эндпоинт

<br>

**Для проверки эндпоинтов**
`http://localhost:8000/organizations_using_house/1`
`http://localhost:8000/organizations_using_activity/1`
`http://localhost:8000/organizations_using_id/1`
`http://localhost:8000/organizations_using_name/Рено`

Для эндпоинта `http://localhost:8000/organizations_using_coordinate` используем JSON тело
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

---

Визуальная часть тестовых данных в БД 

**Organizations**
id | names         | phones                    | hauses_id | activites_id
-  | -             | -                         | -         | - 
1  | Мясная        | +71234567890;+73243432421 | 1         | 3
2  | Столовая      | +73132125412;+71231414132 | 2         | 1
3  | Рено          | +71432214132              | 4         | 5
4  | Все для машин | +71234567890;+73243432421 | 3         | 8

<br>

**Houses**
id | address                       | londgitude  | latitude
-  | -                             | -           | - 
1  | г. Москва, Верхняя улица, д 1 | 55          | 40   
2  | г. Москва, Нижняя улица, д 2  | 50          | 45    
3  | г. Москва, Правая улица, д 3  | 40          | 50    
4  | г. Москва, Левая улица, д 4   | 50          | 40    

<br>

**Activities**
id | names              | paren_id
-  | -                  | - 
1  | Еда                | null
2  | Автомобили         | null
3  | Мясная продукция   | 1
4  | Молочная продукция | 1
5  | Легковые           | 2
6  | Грузовые           | 2
7  | Запчасти           | 5
8  | Аксесуары          | 5
