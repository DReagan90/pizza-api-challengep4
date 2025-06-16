from server.app import db, create_app
from .models.restraunt import Restaurant
from .models.pizza import Pizza
from .models.restraunt_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Mario's Pizza", address="123 Pepperoni Lane")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Cheese Blvd")

    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=15, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=8, restaurant_id=r2.id, pizza_id=p1.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("Database seeded!")
