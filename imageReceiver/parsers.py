import json

from imageReceiver.images.images import resize_image_cloud_storage


def process_message(message):
    data = json.loads(message)
    if data.get('url'):
        resize_image_cloud_storage(data['url'], height=500, width=600, prefix='thumbnail')
