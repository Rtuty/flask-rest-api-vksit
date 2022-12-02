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

musics_list = [
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
        return jsonify(users_list), 200
    if name == 'musics':
        return jsonify(musics_list), 200
    

@app.route('/api/post/<string:name>', methods=['POST'])
def PostQuery(name):
    new_one = request.json
    if name == 'users':
        users_list.append(new_one)
        return jsonify(users_list)
    if name == 'musics':
        musics_list.append(new_one)
        return jsonify(musics_list)

    


@app.route('/api/put/<int:user_list_id>', methods=['PUT'])
def update_tutorial(user_list_id):
    item = next((x for x in users_list if x['id'] == user_list_id), None)
    params = request.json
    if not item:
        return {'message': 'No users with this id'}, 400
    item.update(params)
    return item


@app.route('/api/delete/<int:user_list_id>', methods=['DELETE'])
def delete_tutorial(user_list_id):
    idx, _ = next((x for x in enumerate(users_list)
                   if x[1]['id'] == user_list_id), (None, None))

    users_list.pop(idx)
    return '', 204




if __name__ == '__main__':
    app.run()