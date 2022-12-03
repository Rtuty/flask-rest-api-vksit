from flask import Flask, jsonify, request
from lib.classes import User, Music


app = Flask(__name__)

client = app.test_client()


users = []
musics = []

@app.route('/api/get/<string:name>', methods=['GET'])
def GetQueryHandler(name):
    if name == 'users':
        for us in users:
            user = us.id + ", " + us.name + ", " +us.surname + ", " + us.age
        return user, 200
    if name == 'musics':
        for ms in musics:
            music = ms.name + ", " + ms.author + ", " + ms.raiting
        return music, 200
    if name == None:
        return 'Ошбика! Укажите в URL имя объекта, который собираетесь получить', 404
    else:
        return 'Ошибка! Указан неверный путь в URL'


@app.route('/api/create/<string:name>', methods=['POST'])
def PostMethodHandler(name):
    req = request.get_json()
    if req != None and name == 'user':
        if ('id' and 'name' and 'surname' and 'age') in req:
            id = req['id']
            name = req['name']
            surname = req['surname']
            age = req['age']
        else:
            return 'Ошибка! Недостаточно данных для заполнения объекта пользователь', 500

        user = User(id, name, surname, age)
        users.append(user)
        return  'Новый пользователь успешно добавлен', 200

    elif req != None and  name == 'music':
        if ('name' and 'author' and 'raiting') in req:
            name = req['name']
            author = req['author']
            raiting = req['raiting']
        else:
            return 'Ошибка! Недостаточно данных для заполнения объекта музыка'
        music = Music(name, author, raiting)
        musics.append(music)
        return 'Новая музыкальная композиция успешно добавлена', 200

    else: 
        return 'Ошибка! Сервер не может обработать Ваш запрос', 500


    


@app.route('/api/put/users/<int:user_list_id>', methods=['PUT'])
def update_tutorial(user_list_id):
    item = next((x for x in users if x['id'] == user_list_id), None)
    params = request.json
    if not item:
        return {'message': 'No users with this id'}, 400
    item.update(params)
    return item


@app.route('/api/delete/<int:user_list_id>', methods=['DELETE'])
def delete_tutorial(user_list_id):
    idx, _ = next((x for x in enumerate(users)
                   if x[1]['id'] == user_list_id), (None, None))

    users.pop(idx)
    return '', 204




if __name__ == '__main__':
    app.run(port='3005')