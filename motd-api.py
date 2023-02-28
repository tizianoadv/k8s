# Microservice http "motd-api" 
# The microservice always return a json object {"message":MESSAGE}
# The message must be configurable 
# The service takes two environment variables for its configuration:
# - MESSAGE: is the returned message by the API
# - APP_PORT is the listened port of the API

# Request: curl http://localhost:<APP_PORT>

import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_message():
    print(os.environ.get('MESSAGE'))
    message = os.environ.get('MESSAGE', 'Welcome to the MOTD API')
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(port=os.environ.get('APP_PORT', 5222))


