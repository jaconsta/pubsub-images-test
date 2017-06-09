# Image processing subscriber

This application connects to a Pub/Sub topic, subscribe to it and
listens to events to create image thumbnails and store them in a gCloud
storage bucket.

## Installation

1. Works with [python](https://www.python.org/)
 [**3.5**](https://www.python.org/downloads/release/python-353/)

Ensure you are in this folder
```
cd /route/to/imageReceiver
```

2. Create a virtual environment.

```sh
$ python -m venv venv/apiServer_p35
$ source venv/apiServer_p35/bin/activate #For Unix
$ venv\api\apiServer_p35\Scripts\activate # For windows
```

3. Install the dependencies (From this folder)

```sh
$ pip install -r requirements.txt
```

4. Start the server.

```sh
$ python main.py
```
