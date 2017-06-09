"""
Connects and create to a Google Cloud Pub/Sub topic

https://cloud.google.com/pubsub/docs/reference/libraries#client-libraries-install-python


https://cloud.google.com/pubsub/docs/quickstart-cli#pubsub-publish-message-python 
"""
from google.cloud import pubsub

# Topic Name
TOPIC_NAME = 'imageThumbnails'


def init():
    # Instantiate client
    pubsub_client = pubsub.Client()

    # Prepare and create the Topic.
    topic = pubsub_client.topic(TOPIC_NAME)
    if not topic.exists():
        topic.create()
    return topic

