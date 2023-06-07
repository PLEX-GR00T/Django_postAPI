# postAPI_Harness (Assessment Task for Founding  Engineer role.)

## Functional Requirements
- [x] Once signed up, enrich the User with geolocation data of the IP that the signup originated from 
- [x] based on the geolocation of the IP, check if the signup date coincides with a holiday in the User’s country, and save that info 

## Technical Requirements
- [x] use JWT for user authentication 
- [x] data enrichment must be performed asynchronously, i.e. independently of the signup route API request processing 
- [x] API endpoints functionality must be suitably covered with tests ● use Django-rest-framework library for API 
- [x] implement retries for requests towards 3rd party API 
- [x] user signup 
- [x] user login 
- [x] get user data 
- [x] post CRUD 
- [x] post like/unlike 

## How to Run Locally
- Create a virtual environment if you prefer so (Optional).
- Install all the requirements given for this project:

    ```Bash
    pip install -r requirement.txt
    ```
- Migrate:

    ```Bash
    python manage.py migrate
    ```
- Run the Servers:

    ```Bash
    python manage.py runserver
    ```
- Change your own API_KEY in the .env file manually. 

  ```Bash
  GEO_KEY= Geolocation key from abstactapi.com
  TZ_KEY= Timezone key  from abstractapi.com
  HLD_KEY= Holiday key from abstactapi.com
  ```
  
## Work Evaluation.
- Please use the below methods for API Testing.
```Bash
+--------------------------+------------------------------------------+-------------------+
| HTTP Method              | Path                                     | Endpoint Name     |
+--------------------------+------------------------------------------+-------------------+
| GET                      | /posts/                                  | posts_list        |
| POST                     | /posts/                                  | posts_create      |
| GET                      | /posts/<int:pk>/                         | posts_rud         |
| POST                     | /posts/<int:pk>/like-toggle/             | posts_like_unlike |
| GET                      | /user/details/                           | user_details      |
| POST                     | /user/login/                             | token_obtain_pair |
| POST                     | /user/login/refresh/                     | token_refresh     |
| POST                     | /user/login/verify/                      | token_verify      |
| POST                     | /user/logout/                            | token_blacklist   |
| POST                     | /user/register/                          | register          |
+--------------------------+------------------------------------------+-------------------+
```

