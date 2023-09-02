# Microservices with FastAPI
- This repo (forked from https://github.com/baranbartu/microservices-with-fastapi)
  is composed of a bunch of small microservices.
- Original number of microservices were two, I added suppliers as the third one.
  Now we have 4 including microservices.
- Requirements in the original repo was updated. 
- Only gateway can access internal microservices through the internal network (users, orders, suppliers)
- For more details please visit my Medium story here --> 

## Running
- check ./gateway/.env => 3 services url are defined
- docker-compose up --build
- visit => http://localhost:8001/docs

# Example requests
- There are already created 2 users in users db
- get api token with admin user
  ```
  curl --header "Content-Type: application/json" \
       --request POST \
       --data '{"username":"admin","password":"a"}' \
       http://localhost:8001/api/login
  ```
- You'll see something similar to below
  ```
  {"access_token":"***","token_type":"bearer"}
  ```
- use this token to make administrative level requests
  ```
  curl --header "Content-Type: application/json" \
       --header "Authorization: Bearer ***" \
       --request GET \
       http://localhost:8001/api/users
  ```
- Similar trials can be also done with default user to create & view orders
