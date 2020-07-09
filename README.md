# news
проект выполнен на Python 3.7.

эндпоинт на список категории: http://localhost:8000/api/category/ .

эндпоинт на список новостей: http://localhost:8000/api/news/.

загрузка в базу юзеров: ./manage.py loaddata fixtures/auth.json .
 юзеры:
      1)login: admin4, password: admin4
      2)login: admin1, password: admin1
      3)login: admin, password: admin
      4)login: admin3, password: admin3

загрузка в базу категории и новостей: ./manage.py loaddata fixtures/dump.json .
