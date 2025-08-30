<<<<<<< HEAD
Recipe API This is a Django REST Framework-based API for managing recipes, ingredients, categories, and user favorites. The API allows for user registration, token-based authentication, and full CRUD (Create, Read, Update, Delete) functionality for all resources. Features

User Authentication: Secure user registration and login with Django REST Framework's built-in Token Authentication.
User-Specific Favorites: Users can add and remove recipes from their personal favorites list.
Resource Management: Complete CRUD operations for recipes, ingredients, and categories.
Modular Design: The project is structured with a clean separation of concerns, using separate URL configurations for the project and the app.
Technologies Used

Python 3.10
Django
Django REST Framework
Django REST Framework Token
Gunicorn
WhiteNoise
SQLite3
API Endpoints The API is accessible at the /api/ endpoint.

Endpoint	Method	Description
api/register/	POST	Register a new user.
api/login/	POST	Authenticate and obtain a token.
api/recipes/	GET, POST	List all recipes or create a new recipe.
api/recipes/{id}/	GET, PUT, DELETE	Retrieve, update, or delete a specific recipe.
api/categories/	GET, POST	List all categories or create a new one.
api/categories/{id}/	GET, PUT, DELETE	Retrieve, update, or delete a specific category.
api/ingredients/	GET, POST	List all ingredients or create a new one.
api/ingredients/{id}/	GET, PUT, DELETE	Retrieve, update, or delete a specific ingredient.
api/favorites/	GET, POST	List user's favorite recipes or add a new favorite.
api/favorites/{id}/	DELETE	Remove a recipe from favorites.
Installation and Setup

Clone the repository: git clone https://github.com/Oladimiji/Recipe_project.git cd recipe_project

Create and activate a virtual environment:

On macOS/Linux:
python3 -m venv venv source venv/bin/activate

On Windows:
python -m venv venv venv\Scripts\activate

Install dependencies: pip install -r requirements.txt

Run database migrations: python manage.py makemigrations python manage.py migrate

Create a superuser (for admin access): python manage.py createsuperuser

Run the development server: python manage.py runserver

The API will now be running on http://127.0.0.1:8000/admin/

Deployment The API is deployed on PythonAnywhere. The following configurations were used for deployment:

Virtualenv: /home/your-username/recipe_project/venv
WSGI File: Updated to correctly point to the project's settings.py file.
Static Files: Gunicorn and WhiteNoise were used to serve static files in production. How to Use the API You can use a tool like VS Code's REST Client or curl to test the API endpoints. User Registration: POST http://127.0.0.1:8000/api/register/ HTTP/1.1 Content-Type: application/json
{ "username": "your-username", "password": "your-password" }

Login and Get Token: POST http://127.0.0.1:8000/api/login/ HTTP/1.1 Content-Type: application/json

{ "username": "your-username", "password": "your-password" }

Accessing a Protected Endpoint: GET http://127.0.0.1:8000/api/recipes/ HTTP/1.1 Authorization: Token <your_token>
=======
Recipe API
This is a Django REST Framework-based API for managing recipes, ingredients, categories, and user favorites.
The API allows for user registration, token-based authentication, and full CRUD (Create, Read, Update, Delete) functionality for all resources.
Features
 * User Authentication: Secure user registration and login with Django REST Framework's built-in Token Authentication.
 * User-Specific Favorites: Users can add and remove recipes from their personal favorites list.
 * Resource Management: Complete CRUD operations for recipes, ingredients, and categories.
 * Modular Design: The project is structured with a clean separation of concerns, using separate URL configurations for the project and the app.
 * 
Technologies Used
 * Python 3.10
 * Django
 * Django REST Framework
 * Django REST Framework Token
 * Gunicorn
 * WhiteNoise
 * SQLite3
 * 
API Endpoints
The API is accessible at the /api/ endpoint.
| Endpoint | Method | Description |
|---|---|---|
| api/register/ | POST | Register a new user. |
| api/login/ | POST | Authenticate and obtain a token. |
| api/recipes/ | GET, POST | List all recipes or create a new recipe. |
| api/recipes/{id}/ | GET, PUT, DELETE | Retrieve, update, or delete a specific recipe. |
| api/categories/ | GET, POST | List all categories or create a new one. |
| api/categories/{id}/ | GET, PUT, DELETE | Retrieve, update, or delete a specific category. |
| api/ingredients/ | GET, POST | List all ingredients or create a new one. |
| api/ingredients/{id}/ | GET, PUT, DELETE | Retrieve, update, or delete a specific ingredient. |
| api/favorites/ | GET, POST | List user's favorite recipes or add a new favorite. |
| api/favorites/{id}/ | DELETE | Remove a recipe from favorites. |

Installation and Setup
 * Clone the repository:
   git clone https://github.com/Oladimiji/Recipe_project.git
cd recipe_project

 * Create and activate a virtual environment:
   * On macOS/Linux:
   <!-- end list -->
   python3 -m venv venv
source venv/bin/activate

   * On Windows:
   <!-- end list -->
   python -m venv venv
venv\Scripts\activate

 * Install dependencies:
   pip install -r requirements.txt

 * Run database migrations:
   python manage.py makemigrations
python manage.py migrate

 * Create a superuser (for admin access):
   python manage.py createsuperuser

 * Run the development server:
   python manage.py runserver

The API will now be running on http://127.0.0.1:8000/admin/

Deployment
The API is deployed on PythonAnywhere. The following configurations were used for deployment:
 * Virtualenv: /home/your-username/recipe_project/venv
 * WSGI File: Updated to correctly point to the project's settings.py file.
 * Static Files: Gunicorn and WhiteNoise were used to serve static files in production.
How to Use the API
You can use a tool like VS Code's REST Client or curl to test the API endpoints.
User Registration:
POST http://127.0.0.1:8000/api/register/ HTTP/1.1
Content-Type: application/json

{
    "username": "your-username",
    "password": "your-password"
}

Login and Get Token:
POST http://127.0.0.1:8000/api/login/ HTTP/1.1
Content-Type: application/json

{
    "username": "your-username",
    "password": "your-password"
}

Accessing a Protected Endpoint:
GET http://127.0.0.1:8000/api/recipes/ HTTP/1.1
Authorization: Token <your_token>
>>>>>>> bf94a45a32760d4dbce9c68e11ce977e9f09b5ab
