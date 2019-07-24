# django-rest-api-fun
This is a recipe app

### To execute a command inside a docker container:
```bash
docker-compose run <app-name> <commmand>

# example:
docker-compose run app sh -c "django-admin.py startproject app ."
# sh -c is not necessary but it makes clear what is a docker command
# versus what is a shell command
```

docker-compose run app sh -c "python manage.py test && flake8"
