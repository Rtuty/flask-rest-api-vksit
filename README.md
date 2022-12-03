### Метод POST:
##### Тестирование запроса на добавление
##### 1)Пользователя
Входные данные вида JSON (JavaScript Object Notation):
```json
{
	"id": "1",
	"name": "Kirill",
	"surname": "Kudryavcev",
	"age": "19"
}
```

Результат запроса:
![Pasted image 20221203210544](https://user-images.githubusercontent.com/45632342/205458758-7e161308-7336-4b4a-9b8f-cf33cf5f0e6c.png)

##### 2) Музыкальной композиции
Входные данные типа JSON:
```json
{	
	"id": "1",
	"name": "Walk",
	"author": "Pantera",
	"raiting": "100"
}
```

Результат запроса:
![Pasted image 20221203220920](https://user-images.githubusercontent.com/45632342/205458766-571b530f-5db3-40e7-b1a3-038dcf5e5026.png)


### Метод GET:
##### Тестирование запроса на получения списка объектов:
##### 1) Пользователей

![Pasted image 20221203211316](https://user-images.githubusercontent.com/45632342/205458778-879b81a4-c70b-46d6-ae75-c46da53f6694.png)

##### 2) Музыкальных композиций:
![Pasted image 20221203220940](https://user-images.githubusercontent.com/45632342/205458802-edf6dcdb-607f-4c00-99cb-c0202e4b5d21.png)

### Метод PUT:
##### Тестирование запроса на обновление значений объекта:
##### 1) Пользователь
Обновляем данные:
![Pasted image 20221203222317](https://user-images.githubusercontent.com/45632342/205458834-2c50c4c5-b8d5-406b-aecd-014142d4ddc1.png)
Получаем обновленные данные:
![Pasted image 20221203222355](https://user-images.githubusercontent.com/45632342/205458844-e6667f35-5295-4428-afbb-c0f11380f9a1.png)

##### 2) Музыкальная композиция:

Обновляем данные:
![Pasted image 20221203222605](https://user-images.githubusercontent.com/45632342/205458849-d14c4f7e-386d-49e6-b3d0-14a4c7182d49.png)

Получаем обновленные данные:
![Pasted image 20221203222645](https://user-images.githubusercontent.com/45632342/205458855-443b3b48-90ef-43a8-9729-72a5cb2b353d.png)
### Метод DELETE:
##### Тестирование запроса на удаления конкретного объекта:
##### 1) Пользователь

![Pasted image 20221203220031](https://user-images.githubusercontent.com/45632342/205458863-53d1c2ed-2284-46d1-a9d7-583f06d4a935.png)

##### 2) Музыкальная композиция:
![Pasted image 20221203220724](https://user-images.githubusercontent.com/45632342/205458866-5a1cc1bd-ac52-4d3a-9054-981747426c69.png)
