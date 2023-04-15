# Elevator Simulation

This project implements the business logic for a simplified elevator model in Python using Django Rest Framework. The elevator system can be initialized with N elevators and maintains the elevator states.

## Getting Started
To run the elevator simulation, you need to have Python and Django installed on your machine. If you don't have them installed, please download and install them from the following links:

- [ ] [Python](https://www.python.org/downloads/)
- [ ] [Django](https://www.djangoproject.com/)



Once you have installed Python and Django, clone this repository on your machine and navigate to the project directory in your terminal.

## Installation
To install the dependencies required for this project, run the following command in your terminal:

```js
pip install -r requirements.txt
```

## Usage
To start the Django server and run the elevator simulation, run the following command in your terminal:

```js
python3 manage.py runserver
```

Once the server is running, you can access the API endpoints through your web browser or a tool like Postman.

## API Endpoints

  - [ ] /api/elevator/ - GET: Retrieves the current state of all elevators
  - [ ] /api/request/ - GET: Retrieves all the requests in the system
  - [ ] /api/elevator/<int:pk>/ - GET: Retrieves the current state of a specific elevator
  - [ ] /api/elevator/request_elevator/ POST: Sends a request to schedule an elevator to the desired floor
  - [ ] /api/elevator/bulk_create_elevators/ POST : Creates N number of elevators in bulk
  - [ ] /api/elevator/<int:pk>/set_operational/<int:is_operational>/ POST : Updates the operational state of a specific elevator
  - [ ] /api/elevator/<int:pk>/set_door_status/<int:is_door_open>/ POST : Updates the door status of a specific elevator
  - [ ] /api/elevator/<int:pk>/requests/ GET : Gets requests associated with a specific elevator
  - [ ] /api/elevator/<int:pk>/get_direction/ GET : Gets the direction in which the specific elevator is moving
  - [ ] /api/schema/docs/ GET : Gets the API contracts Swagger documentation


## Acknowledgements
This project was developed as a challenge to implement the business logic for a simplified elevator model in Python using Django Rest Framework. The implementation of this project was based on the requirements provided.

## Working Demo
The working demo is available at https://www.loom.com/share/86cfd25173634b3791c59a234772ed90
