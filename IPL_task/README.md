IPL Task

A simple full-stack project to analyze IPL data using Django REST API for the backend and React for the frontend.

Backend

Activate the virtual environment:

./env/Scripts/Activate.ps1


Run the setup:

cd ipl_project
python manage.py migrate
python load_data.py   # loads data from ./data
python manage.py runserver


API will be at http://localhost:8000/api/

API Endpoints

/api/matches_per_year/ – matches played per year

/api/matches_won_per_team/ – matches won per team

/api/extra_runs/<season>/ – extra runs per team for a season

/api/available_years/ – list of available seasons

Frontend

Go to frontend folder and install dependencies:

cd ipl_frontend
npm install
npm start


Open http://localhost:3000 in your browser

Structure

ipl_project/ – backend and data loader

ipl_project/data/ – CSV files for matches and deliveries

ipl_frontend/ – React frontend

IPL Task

A simple full-stack project to analyze IPL data using Django REST API for the backend and React for the frontend.

Backend

Activate the virtual environment:

./env/Scripts/Activate.ps1


Run the setup:

cd ipl_project
python manage.py migrate
python load_data.py   # loads data from ./data
python manage.py runserver


API will be at http://localhost:8000/api/

API Endpoints

/api/matches_per_year/ – matches played per year

/api/matches_won_per_team/ – matches won per team

/api/extra_runs/<season>/ – extra runs per team for a season

/api/available_years/ – list of available seasons

Frontend

Go to frontend folder and install dependencies:

cd ipl_frontend
npm install
npm start


Open http://localhost:3000 in your browser

Structure

ipl_project/ – backend and data loader

ipl_project/data/ – CSV files for matches and deliveries

ipl_frontend/ – React frontend