Тестовое задание:

**Django + gunicorn + nginx + docker**
1. Использовал Django: Позволяет быстро 
развернуть проект не занимая при этом много времени. 
2. СУБД Postgres: Бесплатный, шустрый, очень распространенный, 
и отлично подходит для работы с Django.


**Инструкция по установке проекта**
1. Установить docker (https://dker.ru/docs/docker-engine/install/) и 
docker-copmose (https://dker.ru/docs/docker-compose/install-compose/).
2. Из командной строки перейти в папку проекта, где находится файл docker-compose.yml
3. Запустить команду для сборки контейнеров docker-compose build
4. Затем запускаем контейнеры docker-compose up -d
5. Проверяем в браузере по адресу http://localhost:8000


**Функционал**
1. При создании заказа, автоматически заполняется номер заказа 
(для избежания дубликатов) и дата. Дополнительно можно было завести поле даты изменения заказа, 
но в задании это не указано.
2. На основной странице отображаются все заказы (по убыванию), 
форма даты поиска для выбора периода (с - левое поле, по - правое поле). 
- просмотреть за определеную дату, указываем в левом поле.
3. Кнопка "Все заказы" (отображает весь список заказов, в бд)
4. "Новый заказ" соответственно создает новый заказ (указываем сумму, контрагента и текст). 
5. При создании или при нажатии на номер заказа переходит на страницу detail 
(Просмотреть заказ, либо изменить либо удалить)
