from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Облачное приложение</title>
        <style>
            body { font-family: Arial; text-align: center; padding-top: 50px; }
            h1 { color: #0078d4; }
        </style>
    </head>
    <body>
        <h1>Приложение работает в облаке Azure!</h1>
        <p>Python Flask + Docker на Linux</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)