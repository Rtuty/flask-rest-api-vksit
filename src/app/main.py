from flask import Flask, request
from lib.classes import User, Music


app = Flask(__name__)

client = app.test_client()

users = []
musics = []

@app.route('/', methods=['GET'])
def MainPageGet():
    return (
            'Method=POST   ' + 'http://127.0.0.1/api/create/*user or music*      - Добавить новый объект' + '<br>' +
            'Method=GET    ' + 'http://127.0.0.1/api/get/*users or music*        - Получить список объектов' + '<br>' +
            'Method=PUT    ' + 'http://127.0.0.1/api/put/*user or music*/*ID*    - Обновить значение по ID у объекта' + '<br>' + 
            'Method=DELETE ' + 'http://127.0.0.1/api/delete/*user or music*/*ID* - Удалить объект по ID'
            )



@app.route('/api/create/<string:name>', methods=['POST'])
def PostMethodHandler(name):

    req = request.get_json()
    
    if req != None and name == 'user':
        if ('id' and 'name' and 'surname' and 'age') in req:
            id      = req['id']
            name    = req['name']
            surname = req['surname']
            age     = req['age']
        else:
            return 'Ошибка! Недостаточно данных для заполнения объекта пользователь', 400

        users.append(User(id, name, surname, age))
        return  'Новый пользователь успешно добавлен', 200

    elif req != None and  name == 'music':
        if ('id' and 'name' and 'author' and 'raiting') in req:
            id      = req['id']
            name    = req['name']
            author  = req['author']
            raiting = req['raiting']
        else:
            return 'Ошибка! Недостаточно данных для заполнения объекта музыка'
        musics.append(Music(id, name, author, raiting))
        return 'Новая музыкальная композиция успешно добавлена', 200

    else: 
        return 'Ошибка! Сервер не может обработать Ваш запрос', 500



@app.route('/api/get/<string:name>', methods=['GET'])
def GetQueryHandler(name):
    if name == 'users':
        for us in users:
            user = us.id + ", " + us.name + ", " +us.surname + ", " + us.age
        return user, 200
    if name == 'musics':
        for ms in musics:
            music = ms.id + ", " +ms.name + ", " + ms.author + ", " + ms.raiting
        return music, 200
    if name in (None or ''):
        return 'Ошбика! Укажите в URL имя объекта, который собираетесь получить', 404
    else:
        return 'Ошибка! Указан неверный путь в URL'



@app.route('/api/put/<string:name_list>/<int:put_id>', methods=['PUT'])
def PutMethodHandler(name_list, put_id):
    
    req = request.get_json()

    if name_list != ('user' or 'music') or name_list == None:
        return 'Ошибка! Укажите тип объекта для обновления'
    if put_id == None:
        return 'Ошибка! Укажите ID объекта для обновления'
    
    if name_list == 'user':
        
        list = users[put_id]

        if 'id' in req:
            list.id = req['id']
        if 'name' in req:
            list.name = req['name']
        if 'surname' in req:
            list.surname = req['surname']
        if 'age' in req:
            list.age = req['age']
    
    if name_list == 'music':

        list = musics[put_id]

        if 'id' in req:
            list.id = req['id']
        if 'name' in req:
            list.name = req['name']
        if 'author' in req:
            list.author = req['author']
        if 'raiting' in req:
            list.raiting = req['raiting']

    return 'Данные успешно изменены', 200



@app.route('/api/delete/<string:name_list>/<int:delete_id>', methods=['DELETE'])
def DeleteMethodHandler(name_list, delete_id):
    if name_list == 'user':
        users.pop(delete_id)
        return 'Пользователь успешно удален', 200
    if name_list == 'music':
        musics.pop(delete_id)
        return 'Композиция успешно удалена', 200
    return 'Ошибка! ID объекта не найден, удаление не выполнено', 400



if __name__ == '__main__':
    app.run(port='3005')