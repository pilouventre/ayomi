# ayomi

1. clone project : 
	
	git clone https://github.com/pilouventre/ayomi.git
	
2. change directory :
	
	cd ayomi/mysite


3. build web container:
	
	docker-compose build
	
5. create db:

	docker-compose up
	
6. Open new terminal :

	. docker ps ( to get container_id of app:myiste image )
	
	. docker exec -it <container_id> bash
	
	. python manage.py makemigrations
	
	.python manage.py migrate
	
	.python manage.py createsuperuser
	
	leave container

7. start container et database :
	
	docker-compose up
	
8. open web window :
	
	127.0.0.8001/admin/ : login with superuser identifers and create user to test website
	
	login page: 127.0.0.8001/login/
