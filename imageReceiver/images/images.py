from datetime import datetime
from io import BytesIO

import requests
from google.cloud import storage
from PIL import Image

import os
UPLOAD_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/static/assets"
IMAGE_ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
PROJECT_ID = os.environ.get('GOOGLE_PROJECT_ID', 'build-156611')
CLOUD_STORAGE_BUCKET = os.environ.get('GOOGLE_BUCKET_NAME', 'pubsubtest-bucket')


def create_client(project_id=PROJECT_ID):
    return storage.Client(project=project_id)


def storage_connection(filename):
    """Cloud storage connection."""
    client = create_client()
    bucket = client.bucket(CLOUD_STORAGE_BUCKET)
    blob = bucket.blob(filename)
    return blob


def resize_image_cloud_storage(url, height=None, width=None, prefix=None):
    """
    Takes the source image and resize it to create a thumbnail of it.

    It currently stores every file as JPG.

    :param url: Original image url.
    :param height:
    :param width:
    :param prefix: Prefix to add to name (ex. small, medium)
    :return: Thumbnail Cloud storage file URL
    """
    thumbnailImage = Image.open(BytesIO(requests.get(url).content))
    size = height, width
    thumbnailImage.thumbnail(size)
    # Adjust the image name and convert to jpeg
    thumbnailName = url.split('/')[-1]  #
    thumbnailFilename = '{}.jpg'.format(int(datetime.now().timestamp()))   # '{prefix}_{filename}.{ext}'.format(prefix=prefix, filename=thumbnailName.split('.')[0], ext='jpg')
    # Instead of physical save the file, store it as Stream.
    output = BytesIO()
    thumbnailImage.save(output, 'JPEG')
    # Cloud storage connection.
    blob = storage_connection(thumbnailFilename)
    # And upload it to Cloud Storage
    output.seek(0)  # Needs to be rewind after save.
    blob.upload_from_string(output.read(), content_type='image/jpeg')

    url = blob.public_url

    if isinstance(url, bytes):
        url = url.decode('utf-8')

    return thumbnailFilename, 'image/jpeg', url
