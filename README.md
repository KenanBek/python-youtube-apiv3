Python YouTube APIv3
====================

It is wrapper over Google API Python Client for retrieving YouTube data.

### Setup

    git clone https://github.com/KenanBek/python-youtube-apiv3
    cd python-youtube-apiv3
    virtualenv env
    source env/bin/activate (or .\env\Scripts\activate)
    pip install -r requirements.txt

### Run

To run quick start demo you need API Key. Please visit https://developers.google.com/youtube/v3/getting-started for 
more information. When you have your own API Key please replace following code in **quickstart.py**:

    API_SERVICE_NAME = 'youtube'
    API_VERSION = 'v3'
    API_KEY = 'YOUR_API_KEY'

And then run following command:

    python quickstart.py

### Related Links

- [Google API Python Client](https://github.com/google/google-api-python-client)
- [API Samples](https://github.com/youtube/api-samples/tree/master/python)
- [API PyDoc ref](https://developers.google.com/resources/api-libraries/documentation/youtube/v3/python/latest/)
- [API explorer](https://developers.google.com/apis-explorer/#p/youtube/v3/)

Other links:

- [Home page for Google Youtube API v3](https://developers.google.com/youtube/v3/)
- [YouTube Data API Client Library for Python](https://developers.google.com/api-client-library/python/apis/youtube/v3)
- [Full list of APIs supported by Google API Client for Python](https://developers.google.com/api-client-library/python/apis/)
