# App

All the requirements  in the three phases were implemented


## Run the app

Below are the steps on how to get the application up and running and a breif description for each step

* App/start.sh

`bash start.sh`

* An interactive shell that allows you to control the whole APP by providing 7 options to do so:
1. Apply migrations
2. Generate migrations (with arguments)
3. Downgrading migrations
4. Seed data
5. RUN APPLICATION...
6. Turn off APPLICATION...
7. Run tests
8. Run event subscriber

* Option 5 is most probably what are you going to use first, so it will manage building and running the below docker services:
1. database
2. broker
3. backend
4. celery
5. test

>> For development purposes I ran both Celery and Beat on the same docker service/image for production use we can have separate builds

>> dev_setup/docker-compose.yml was changed due to adding services

Also it will manage applying migrations. What you'll need to do next is from within the backend container to run option 4 to seed data.
The rest of the interactive shell list is for manually handling things. Use `docker logs` for command or Docker desktop app to manage and browse containers.


* The app runs on `localhost:8000` from which you can browse the API docs
API Docs
1. http://localhost:8000/api/docs
2. http://localhost:8000/api/redoc


* For Unit test results check the Test container/service logs with coverage.

* For subscribing to the events published by Celery task run option 8 inside the backend docker container. Events published within the Celery task are being captured and inserted into Alerts model, from which you can see what alerts/events got triggered or to to get this information from `http://localhost:8000/alert/alerts`
