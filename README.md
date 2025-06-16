🍕 Pizza Restaurant API (Flask + SQLAlchemy)
This project is a RESTful API for managing restaurants, pizzas, and the relationships between them. It follows the MVC pattern using Flask, SQLAlchemy, and Flask-Migrate.

📁 Project Structure
bash
Copy
Edit
.
├── server/
│   ├── app.py                  # App factory
│   ├── config.py               # Configs (DB URI)
│   ├── seed.py                 # Seed script
│   ├── models/
│   │   ├── __init__.py
│   │   ├── restaurant.py
│   │   ├── pizza.py
│   │   └── restaurant_pizza.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   └── restaurant_pizza_controller.py
├── migrations/
├── challenge-1-pizzas.postman_collection.json
└── README.md
🧰 Setup Instructions
1. Clone & Install Dependencies
bash
Copy
Edit
git clone <repo-url>
cd <project-folder>
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
2. Initialize Database
bash
Copy
Edit
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
3. Seed the Database
bash
Copy
Edit
python server/seed.py
