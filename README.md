* # Cricbuzz API
* 
* This is a API for a platform similar to Cricbuzz, where guest users can browse matches and view details, while admin users can perform operations like adding matches, players, updating stats, and scores.
* 
* ## Tech Stack:-
*
* - FastAPI
* - Python
* - MySQL
* - SQLAlchemy
* - OAuth2 for Authentication
* 
* ## Setup Instructions:-
* 
* ### Prerequisites:-
* 
* - Python 3.7+
* - MySQL server
* 
* ### Install Dependencies:-
* 
* 1. Create and activate a virtual environment (optional but recommended):
* 
*     ```
*     python -m venv env
*     source env/bin/activate  # On Windows use `env\Scripts\activate`
*     ```
* 
* 2. Install required packages:-
* 
*     ```
*     pip install fastapi uvicorn sqlalchemy mysql-connector-python passlib python-jose
*     ```
* 
* ### Database Setup:-
* 
* 1. Install MySQL server if not already installed.
* 
* 2. Create the database:
* 
*     ```
*     CREATE DATABASE cricket;
*     ```
* 
* 3. Create the necessary tables:
* 
*     ```
*     USE cricket;
* 
*     CREATE TABLE users (
*         id INT AUTO_INCREMENT PRIMARY KEY,
*         username VARCHAR(50) UNIQUE NOT NULL,
*         password VARCHAR(100) NOT NULL,
*         role ENUM('admin', 'guest') NOT NULL
*     );
* 
*     CREATE TABLE matches (
*         id INT AUTO_INCREMENT PRIMARY KEY,
*         title VARCHAR(100) NOT NULL,
*         schedule DATETIME NOT NULL,
*         details TEXT
*     );
* 
*     CREATE TABLE teams (
*         id INT AUTO_INCREMENT PRIMARY KEY,
*         name VARCHAR(50) NOT NULL,
*         match_id INT,
*         FOREIGN KEY (match_id) REFERENCES matches(id)
*     );
* 
*     CREATE TABLE players (
*         id INT AUTO_INCREMENT PRIMARY KEY,
*         name VARCHAR(50) NOT NULL,
*         stats TEXT,
*         team_id INT,
*         FOREIGN KEY (team_id) REFERENCES teams(id)
*     );
*     ```
* ### Application Setup:-
* 
* 1. Clone the repository or copy the project files to your local machine.
* 
* 2. Create a `.env` file in the root directory and add your database connection details:
* 
*     ```
*     DATABASE_URL=mysql+mysqlconnector://<username>:<password>@<host>/<database>
*     ```
* 
* 3. Run the FastAPI application:-
* 
*     ```
*     uvicorn main:app --reload
*     ```
* 
* ### API Endpoints:-
* 
* #### Register a User:-
* 
* - **Endpoint:** `POST /register/`
* - **Request Body:**
* 
*     ```
*     {
*         "username": "admin_user",
*         "password": "admin_password",
*         "role": "admin"
*     }
*     ```
* 
* #### Login for Access Token:-
* 
* - **Endpoint:** `POST /token`
* - **Request Body:**
* 
*     ```
*     username=admin_user&password=admin_password
*     ```
* 
* - **Response:**
* 
*     ```
*     {
*         "access_token": "<token>",
*         "token_type": "bearer"
*     }
*     ```
* 
* #### Create a Match (Admin Only):-
* 
* - **Endpoint:** `POST /matches/`
* - **Request Header:** `Authorization: Bearer <token>`
* - **Request Body:**
* 
*     ```
*     {
*         "title": "Match 1",
*         "schedule": "2024-06-01T15:30:00Z",
*         "details": "This is a test match."
*     }
*     ```
* 
* #### Read Matches:-
* 
* - **Endpoint:** `GET /matches/`
* - **Response:**
* 
*     ```
*     [
*         {
*             "id": 1,
*             "title": "Match 1",
*             "schedule": "2024-06-01T15:30:00Z",
*             "details": "This is a test match."
*         }
*     ]
*     ```
* 
* #### Read a Specific Match:-
* 
* - **Endpoint:** `GET /matches/{match_id}`
* - **Response:**
* 
*     ```
*     {
*         "id": 1,
*         "title": "Match 1",
*         "schedule": "2024-06-01T15:30:00Z",
*         "details": "This is a test match."
*     }
*     ```
* 
* #### Add Player to a Team (Admin Only):-
* 
* - **Endpoint:** `POST /teams/{team_id}/players/`
* - **Request Header:** `Authorization: Bearer <token>`
* - **Request Body:**
* 
*     ```
*     {
*         "name": "John Doe",
*         "stats": "Batsman"
*     }
*     ```
* 
* #### Get Player Stats:-
* 
* - **Endpoint:** `GET /players/{player_id}/stats/`
* - **Response:**
* 
*     ```
*     {
*         "id": 1,
*         "name": "John Doe",
*         "stats": "Batsman",
*         "team_id": 1
*     }
*     ```
* 
* ### Register an Admin User:-
* 
* ```
* curl -X POST "http://127.0.0.1:8000/register/" -H "Content-Type: application/json" -d '{
*   "username": "admin_user",
*   "password": "admin_password",
*   "role": "admin"
* }'**********

* 
* 
* ### Assumptions:-
* Passwords are not hashed for simplicity. In a real-world application, always hash passwords before storing them.
* The application is running on localhost with port 8000.
* Dummy data can be used for matches, teams, and players as required.
* License
* This project is licensed under the MIT License.
* 
* This `README.md` file includes all the necessary information for setting up, running, and using the Cricbuz