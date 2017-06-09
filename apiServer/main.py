import json
from os import environ

from pub_sub.configure import init as topic_init

from server import app

HOST = environ.get('HOST', '127.0.0.1')
PORT = int(environ.get('PORT', '4889'))
DEBUG = True


if __name__ == '__main__':
    print('Started')
    app.run(host=HOST, debug=DEBUG, port=PORT)
