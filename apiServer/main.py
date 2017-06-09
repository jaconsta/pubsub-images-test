from pub_sub.configure import init as topic_init

import json


def main():
    topic = topic_init()

    for a in range(5):
        message = {'number': 'message {}'.format(a)}
        data = json.dumps(message).encode('utf-8')
        message_id = topic.publish(data)

        print('Message {m_id} published.'.format(m_id=message_id))


if __name__ == '__main__':
    print('Started')
    main()
