# ziphp_testing_project

This is my testing project task for ZipHP interview.

Main goal was to create api where we can input airplanes with id and passenger assumptions.
The application will calculate fuel consumption according to equations

Step to run the project(For Windows):
1. To run the project you need clone the current project instal virtual env. 
  - py -m pip install virtualenv 
  - py -m venv venv
  - .\venv\Script\activate
  - pip install -r requirements.txt
2. Before run apply migrate
  - python manage.py migrate

3. Now you can run the project
  - python mange.py runserver localhost:8000

4. Now you can access the api by using swagger. Open your browser and type
 - localhost:8000/swagger

5. Use POST /api/v1/common/airplane/ and body. To create an airplane
  {"type_id": int, "passenger_assumption": int}

6. Use GET /api/v1/common/airplane/. To get all airplanes with their calculated fuel consumption 
per minute and total flight time according to passenger assumption.

7. You can use PUT and PATCH to modify airplane by passing uuid of the airplane

Airplane presented in models.py with fields:
  - uuid(Primary Key, default=uuid4)
  - is_active(Boolean, defaulte=True)
  - created(DateTime, auto_now_add=True)
  - updated(DateTime, autonow=True)
  - type_id(Integer, default=1)
  - passenger_assumption=(Integer, defualt=0)

Serializer to get data of airplanes:
  - uuid
  - type_id
  - passenger_assumption
  - fuel_consumption_per_minute
  - total_flight_time

TestCases
  1. To check if 10 airplanes can be created and retrieved
  2. To check after creation of 10 airplanes calculated data of fuel consumption and total flight time are correct

To run test cases use
  - python manage.py test common
