from app import create_app
import os
SECRET_KEY = os.urandom(32)

app = create_app()
app.config['SECRET_KEY'] = SECRET_KEY

if __name__ == '__main__':
    from waitress import serve
    serve(app)
