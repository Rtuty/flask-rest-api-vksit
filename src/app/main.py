from flask import Flask, jsonify, request
#from classes import User, Music

app = Flask(__name__)

client = app.test_client()

users_list = [
    {   
        'id': 1,
        'name':'Kirill',
        'surname': 'Kudryavcev',
        'age':19
    },
    {   
        'id': 2,
        'name':'Bob',
        'surname': 'Brown',
        'age':33
    }
]

@app.route('/api/get', methods=['GET'])
def GetQuery():
    return jsonify(users_list)

@app.route('/api/post', methods=['POST'])
def PostQuery():
    new_one = request.json
    users_list.append(new_one)
    return jsonify(users_list)


@app.route('users/put/<int:users_list_id>', methods=['PUT'])
def PutQuery(users_list_id):
    item = next((x for x in users_list if x['id'] == users_list_id), None)
    params = request.json

    if not item:
        return {'message': 'Ошибка! Объект с указаным идентификатором не найден'}, 400
    item.update(params)

    return jsonify(item)


if __name__ == '__main__':
    app.run()