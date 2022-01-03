from flaskblog import create_app

def prod():
    app.run()

if __name__ == '__main__':
    app.run(debug=False)

prod()
