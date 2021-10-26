http://127.0.0.1:8000/api/email/ 
по GET выдает все email в базе 
![Screenshot 2021-10-27 at 01 29 36](https://user-images.githubusercontent.com/36387132/138956072-3b506e3d-ece6-4607-9ce2-47675c9c7e67.png)

http://127.0.0.1:8000/api/email/ <pk>

выдает инфу об конкретном email
![Screenshot 2021-10-27 at 01 30 21](https://user-images.githubusercontent.com/36387132/138956163-bde9441a-1eaf-4050-9803-780c1e1c859a.png)

http://127.0.0.1:8000/api/email/  по POST создает новую запись, на поля letter_subject / message ограниченний нет на поле destination есть ограничения (не пустое поле) так же стоит валидатор на модели (django.core.validators) валидирующий email  

![Screenshot 2021-10-27 at 01 31 32](https://user-images.githubusercontent.com/36387132/138956315-44324845-ab1f-4276-8a14-504e1bdc1e68.png)


http://127.0.0.1:8000/api/statistics/ статистика за 24 часа (GET)


![Screenshot 2021-10-27 at 01 33 51](https://user-images.githubusercontent.com/36387132/138956631-4fe23ec9-78f8-4077-825b-39d17644c1b7.png)

