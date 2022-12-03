from flask import Flask, jsonify, request
from lib.classes import User


app = Flask(__name__)

client = app.test_client()

users = [
    {   
        'id': 1,
        'name':'Kirill',
        'surname': 'Kudryavcev',
        'age':19,
    },
    {   
        'id': 2,
        'name':'Bob',
        'surname': 'Brown',
        'age':33,
    }
]

musics = [
    {
        'name': 'smells like teen spirit',
        'author': 'nirvana',
        'raiting': 80,
    },
    {
        'name': 'walk',
        'author': 'panter',
        'raiting': 100,
    }
]

@app.route('/api/get/<string:name>', methods=['GET'])
def GetQuery(name):
    if name == 'users':
        return jsonify(users), 200
    if name == 'musics':
        return jsonify(musics), 200

#todo
# @app.route('/api/get/id/<string:name>/<int:id>', methods=['GET'])
# def GetQuery(name, id):
#     if name == 'users':
#         return jsonify(users[id]), 200
#     if name == 'musics':
#         return jsonify(users[id]), 200


@app.route('/api/createuser', methods=['POST'])
def PostQuery():
    if request.method == 'POST':
        req = request.get_json()

        id = None
        name = None
        surname = None
        age = None
    
        if req:
            if 'id' in req:
                id = req['id']
            else:
                return 'Ошибка! id пользователя отсутствует', 400
            if 'name' in req:
                name = req['name']
            else:
                return 'Ошибка! имя пользователя отсутствует', 400
            if 'surname' in req:
                surname = req['surname']
            else:
                return 'Ошибка! фамилия пользователя отсутствует', 400
            if 'age' in req:
                age = req['age']
            else:
                return 'Ошибка! возраст пользователя отсутствует', 400
        else: return 'Вы не ввели никаких данных', 404

        user = User(id, name, surname, age)
        users.append(user)
        return 'Новый пользователь добавлен', 200

    return 'Неизвестная ошибка', 404

    


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