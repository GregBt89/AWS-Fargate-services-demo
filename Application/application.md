# **Demo Application**

The demo Application consists of one or more [Rest APIs](https://www.geeksforgeeks.org/rest-api-introduction/) and a [nginx](https://nginx.org/en/) server configured to act as a reverse proxy redirecting requests to the different APIs.

## **Backend**

### **API design**

Since the focus is not on the application it self, a skeleton API is designed to be abstract enough such that more than one APIs can be spawned fast and easy in order to showcase the functionallity of a reverse proxy and a docker/container network.Each API will respond to requests with a signature message of the following structure:

```json
{
    "API": "API title/description"
}
```

The code snippet below is taken from the [main.py](./backend/app/main.py) file and it shows the two available paths. The API_PATH is of the form "/someapi" where *someapi* is a parameter passed on as an environment variable. Same is the case for the api title or desctiopn which is passed on as an environment variable ***s.display_name***. To prove that an API can reach some other API a request is made from the current API to a target API from the path "/someapi/someotherapi".

```python
@app.get(API_PATH, response_model=Response)
def display_API_name():
    return {"API": s.display_name}

@app.get(API_PATH + "/{target}", response_model=GetFromResponse)
def reach_target(target):
    r = requests.get(f"{s.nginx_server}/{target}")
    return {"API":{s.display_name:r.json()}}
```

Here the *someotherapi* is a path parameter, so if the path exists the response will have the following form.

```json
{
    "API": {
        "someapi title/description":{
            "API" : "someotherapi title/description"
        }
    }
}
```

Note that the validation of settings ([config.py](./backend/app/config.py)) and API response ([schemas.py](./backend/app/schemas.py)) is acheived with the python library [pydantic](https://pydantic-docs.helpmanual.io/). If needed validation can be performed for the incoming requests as well.

### **Dockerfile**

THe backend image is based on the [python3.9](https://hub.docker.com/layers/library/python/3.9/images/sha256-d0228a84a4ed50a620d1dc5d38aae226db6608d6bd2c9816592823cd73bf4ad9?context=explore) image. The default values of the API enviroment varaibles are:

- URL_PARAM=api
- DISPLAY_NAME=API

- NGINX_SERVER=http://localhost:8000

- UVICORN_HOST=0.0.0.0
- UVICORN_PORT=8000
- UVICORN_WORKERS=2

The first two are related to the direcotry of the API and the API's title or discreption. For the communication with other APIs the nginx server is passed on as an enviroment varaible. Uvicorn looks for enviroment variables with the prefix UVICORN_ for setting its parameters, for more information see [here](https://www.uvicorn.org/settings/).

## **Frontend**

The frontend is a nginx server acitng as a reverse proxy for the APIs. Its configuration is defined in the [default.conf.template](./frontend/nginx/templates/default.conf.template) file. Therein the listening port is defined as well as the redirection of requests to the appropriate locations using the proxy_pass paramter. For more information about the nginx settings consult the official [documentation](https://nginx.org/en/). 

**Important note**: Three api locations have been hardcoded in the configuration file. So, if for instance more or less APIs are needed the configuration file must be updated accordingly. 





