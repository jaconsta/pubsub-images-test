# Initialization Steps

## Gcloud

Initial configuration of the gCloud Pub/Sub solution.

Reference: [Quickstart-cli](https://cloud.google.com/pubsub/docs/quickstart-cli)

Create a new Project.

Start a new cloud console. (web or cloud-SDK. (I'm doing it in web.))


``` sh
$ gcloudl init
```


```sh
$ gcloud components install beta # Not required on web
```

### Create the Queue Topic.

If you want to create the topics manually, but the code can handle the
topics creation.

```sh
gcloud beta pubsub topics create imageThumbnails.
```

## Application usage.

### Using gCloud sdk to handle the login session.

Local basic usage is with by logging first into cloud SDK

```sh
gcloud auth application-default login
```

For usage outside a PC or env with SDK use [Auth](https://cloud.google.com/docs/authentication#getting_credentials_for_server-centric_flow):

### Auth credentials method.

In IAM & ADMIN -> Service accounts. Click on *Create Service Account*.

Set the parameters as:
 - **Name:** *Any*
 - **Role:**  Project -> Owner. You can try a more specific one,
        depending on the services you require.

Click create. In the account list, click Options (Three vertical dots) ->
  Create key -> ( select *Key type*=JSON) Create

Keep the Downloaded file, remember it's name and location.

For each virtual environment, set the GOOGLE_APPLICATION_CREDENTIALS
environment to the file location

```sh
# On Unix
export GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>
# On Windows
set GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>
```

## Enable gCloud API access

**NOTE** For the PUB / SUB API access to work, a paid account is required.

If you haven't enabled the api access to PUB SUB you need to start it.

Go the API Manager -> Library -> GoogleCloud APIs -> [Cloud Pub/Sub API](https://console.developers.google.com/apis/api/pubsub.googleapis.com/overview?project=pubsub-datatest).

And click ENABLE
