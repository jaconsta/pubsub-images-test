"""
Listens to the Push/pull subscription queue to read the images files and creates thumbnails files for them.


"""
from google.cloud import pubsub

TOPIC_NAME = 'imageThumbnails'
SUBSCRIPTION_NAME = 'thumbnails_subs'


def createSubscription(subscription):
    """
    Subscribe the client to a pub/sub topic.
    :return: 
    """
    if not subscription.exists():
        subscription.create()
        print('Subscription `{}` created on topic {}.'.format(subscription.name, TOPIC_NAME))


def init_subs():
    """
    
    :return: 
    """
    pubsub_client = pubsub.Client()
    topic = pubsub_client.topic(TOPIC_NAME)
    subscription = topic.subscription(SUBSCRIPTION_NAME)
    createSubscription(subscription)
    return subscription


def subscription_listener(subscription):
    """
    Listens for new messages
    :return: 
    """
    # Return immediately to avoid code block.
    results = subscription.pull(return_immediately=True)

    for ack_id, message in results:
        print('Message {}: {}, {}'.format(message.message_id, message.data.decode(), message.attributes))

    # Acknowledge message to confirm received and processing.
    if results:
        subscription.acknowledge([ack_id for ack_id, message in results])


def main():
    subcriber =init_subs()
    while True:
        subscription_listener(subcriber)


if __name__ == '__main__':
    print('Started.')
    main()
