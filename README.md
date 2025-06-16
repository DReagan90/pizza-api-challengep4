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

🛠 Models Summary
🏪 Restaurant
id: Integer, Primary Key

name: String

address: String

➕ Has many RestaurantPizzas

🍕 Pizza
id: Integer, Primary Key

name: String

ingredients: String

➕ Has many RestaurantPizzas

🔗 RestaurantPizza
id: Integer, Primary Key

price: Integer (must be between 1 and 30 ✅)

restaurant_id: FK → Restaurant

pizza_id: FK → Pizza

➕ Belongs to Restaurant and Pizza

🔌 API Endpoints
GET /restaurants
Returns a list of all restaurants.

✅ Example Response:

json
Copy
Edit
[
  { "id": 1, "name": "Mario's Pizza", "address": "123 Pepperoni Lane" },
  { "id": 2, "name": "Kiki's Pizza", "address": "456 Cheese Blvd" }
]
GET /restaurants/<id>
Returns a single restaurant and its pizzas.

✅ Example Response:

json
Copy
Edit
{
  "id": 1,
  "name": "Mario's Pizza",
  "address": "123 Pepperoni Lane",
  "pizzas": [
    { "id": 1, "name": "Margherita", "ingredients": "Tomato, Mozzarella, Basil" },
    { "id": 2, "name": "Pepperoni", "ingredients": "Tomato, Mozzarella, Pepperoni" }
  ]
}
❌ If not found:

json
Copy
Edit
{ "error": "Restaurant not found" }
DELETE /restaurants/<id>
Deletes a restaurant and all related RestaurantPizzas.

✅ If successful:

204 No Content

❌ If not found:

json
Copy
Edit
{ "error": "Restaurant not found" }
GET /pizzas
Returns a list of all pizzas.

✅ Example Response:

json
Copy
Edit
[
  { "id": 1, "name": "Margherita", "ingredients": "Tomato, Mozzarella, Basil" },
  { "id": 2, "name": "Pepperoni", "ingredients": "Tomato, Mozzarella, Pepperoni" }
]
POST /restaurant_pizzas
Creates a new pizza-restaurant link.

📥 Request:

json
Copy
Edit
{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2
}
✅ Success Response:

json
Copy
Edit
{
  "id": 4,
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato, Mozzarella, Basil"
  },
  "restaurant": {
    "id": 2,
    "name": "Kiki's Pizza",
    "address": "456 Cheese Blvd"
  }
}
❌ Error (Validation):

json
Copy
Edit
{ "errors": ["Price must be between 1 and 30"] }
🔍 Postman Testing
🧪 Import & Test
Open Postman

Click Import

Upload challenge-1-pizzas.postman_collection.json

Run each route and validate responses

✅ Validation Rules
RestaurantPizza.price must be between 1 and 30

All fields are required

Returns proper 404 or 400 for bad input