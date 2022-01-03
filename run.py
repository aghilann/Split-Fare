from flaskblog import create_app

def prod():
    app.run()

if __name__ == '__main__':
    app.run(debug=False,
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 2020))
prod()
