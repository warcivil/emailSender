http://127.0.0.1:8000/api/email/ 
по GET выдает все email в базе 
![Screenshot 2021-10-27 at 01 36 50](https://user-images.githubusercontent.com/36387132/138957063-74a8325e-4f86-4bcd-9387-4ef9746a2296.png)

http://127.0.0.1:8000/api/email/<pk>
выдает инфу об конкретном email
![Screenshot 2021-10-27 at 01 37 19](https://user-images.githubusercontent.com/36387132/138957123-8801824e-dbc6-4616-8a4d-c301a19ade19.png)

http://127.0.0.1:8000/api/email/  по POST создает новую запись, на поля letter_subject / message ограниченний нет на поле destination есть ограничения (не пустое поле) так же стоит валидатор на модели (django.core.validators) валидирующий email  

![Screenshot 2021-10-27 at 01 31 32](https://user-images.githubusercontent.com/36387132/138956315-44324845-ab1f-4276-8a14-504e1bdc1e68.png)


http://127.0.0.1:8000/api/statistics/ статистика за 24 часа (GET)

