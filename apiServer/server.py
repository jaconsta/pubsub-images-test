import json

from flask import Flask, request

from pub_sub.configure import init as topic_init

# Initialize Flask server application.
app = Flask(__name__)
app.secret_key = 'Mg2Jzu2idrBB2KRQ096IiaBDflI6RynA'     # Set it to a random

# Initialize queue object
TOPIC = topic_init()

messageIds = []

# Routing.
@app.route("/", methods=['GET', "POST"])
def index():
    """
    Takes and process the image url.
    :return: 
    """
    # Return a list of the sent Message Id's.
    if request.method == 'GET':
        return json.dumps(messageIds)

    # Push a message to the Queue
    data = request.json

    try:
        message = {'url': data['url']}
    except KeyError or TypeError as e:
        return json.dumps({'message': 'Bad body structure.'})

    data = json.dumps(message).encode('utf-8')
    message_id = TOPIC.publish(data)
    messageIds.append(message_id)

    return json.dumps({'status': 'OK', 'message': 'Image sent to queue', 'QueueId': message_id})
