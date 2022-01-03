'''
from flaskblog import create_app
from flask import Flask

app = Flask(__name__)

def prod():
    app.run()

if __name__ == '__main__':
    app.run(debug=False,
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 2020))
prod()
'''
from flask import Flask
from flaskblog import create_app
app = Flask(__name__)

def prod():
    app.run(debug=True, use_reloader=True)

if __name__ == '__main__':
    app.run(debug=False,
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 2020))
prod()
