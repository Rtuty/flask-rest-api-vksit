from flask import Flask, jsonify, request
#from flask_swagger_ui import get_swaggerui_blueprint
#from classes import User, Music

app = Flask(__name__)

client = app.test_client()

users_list = [
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

music_list = [
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

@app.route('/api/get', methods=['GET'])
def GetQuery():
    return jsonify(users_list)

@app.route('/api/post', methods=['POST'])
def PostQuery(users_list):
    new_one = request.json
    users_list.append(new_one)
    return jsonify(users_list)


# @app.route('api/put/<int:users_list_id>', methods=['PUT'])
# def PutQuery():
#     item = next((x for x in users_list if x['id'] == users_list_id), None)
#     params = request.json

#     if not item:
#         return {'message': 'Ошибка! Объект с указаным идентификатором не найден'}, 400
#     item.update(params)

#     return jsonify(item)

# @app.route('api/delete/<int:users_list_id>', methods=['DELETE'])
# def DeleteQuery(users_list_id):
#     idx, _ = next(
#         (x for x in enumerate(users_list) 
#         if x[1]['id'] == users_list_id), (None, None)
#         )
#     users_list.pop(idx)
#     return 'Пользователь с ID: ', jsonify(idx), 'удален', 204


if __name__ == '__main__':
    app.run()