# Indors Navigation - test

There was not enough time to cover the entire project with tests.
The project is 93% covered by tests.

### Launch of the project

#### 1) Clone repositories
```
git clone https://github.com/Lanterman/indors.git
```
#### 2) Create and run docker-compose
```
docker-compose up -d --build
```
##### 2.1) To create a superuser, run the following instruction:
```
docker exec -it <backend_container_ID> python manage.py createsuperuser
```

#### 3) Follow the link in the browser:
 - ##### to launch the swagger openapi:
    ```
    http://127.0.0.1:8000/swagger/
    ```
 - ##### to launch the drf openapi:
    ```
    http://127.0.0.1:8000/api/v1/
    ```


P.S.
To test the functionality of the "Celery Task" and "/auth/profile/try_to_reset_password/" endpoint, you need to set the following environment variables:
1. '.env' file:
   1.1. EMAIL_HOST_USER
   1.2. EMAIL_HOST_PASSWORD
2. '.env.dev' file:
   1.1. DOC_EMAIL_HOST_USER
   1.2. DOC_EMAIL_HOST_PASSWORD

P.S.S.
Before resetting "auth/reset_password/{email}/{secret_key}/" password, you must request it from "/auth/profile/try_to_reset_password/" endpoint.
