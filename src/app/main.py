from flask import Flask, jsonify, request
#from classes import User, Music

app = Flask(__name__)

client = app.test_client()

users_list = [
    {
        'name':'Kirill',
        'surname': 'Kudryavcev',
        'age':19
    },
    {
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


if __name__ == '__main__':
    app.run()