from pub_sub.configure import init as topic_init

import json


def main():
    topic = topic_init()

    image_list = [
        'https://images.unsplash.com/photo-1428940253195-53483a1de2e6?dpr=1&auto=format&fit=crop&w=1500&h=1033&q=80&cs=tinysrgb&crop=&bg=',
        'https://images.unsplash.com/photo-1476297820623-03984cf5cdbb?dpr=1&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=&bg=',
        'https://images.unsplash.com/photo-1470163395405-d2b80e7450ed?dpr=1&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=&bg=',

    ]
    for image in image_list:
        message = {'url': image}
        data = json.dumps(message).encode('utf-8')
        message_id = topic.publish(data)

        print('Message {m_id} published.'.format(m_id=message_id))


if __name__ == '__main__':
    print('Started')
    main()
