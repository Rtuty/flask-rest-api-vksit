from flask import Flask
#from classes import User, Music

app = Flask(__name__)

client = app.test_client()

test = [
    {
        'name':'Kirill'
    },
    {
        'music':'slipnot'
    }
]
@app.route('/api/test', methods=['GET'])
def GetQuery():
    return test

if __name__ == '__main__':
    app.run()