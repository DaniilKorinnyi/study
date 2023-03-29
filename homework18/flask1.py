from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/hello')
def hello():
    app.logger.info('Request received for hello endpoint.')
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()
