from flask import Flask, request
from classes import *

app = Flask(__name__)

# Получить список пользователей
@app.route('api/users')
def GetUsers():
    result = ''
    users = []
    for us in users:
        user = us.name + ", " + us.age + ", " + us.gender + ", " +us.job + ", " +us.hobby
        result = result + user
    return result, 200


if __name__ == '__main__':
    app.run()