from random import choice as rc

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    fake = Faker()

# This will delete any existing rows from the Restaurant and Customer tables
# so you can run the seed file multiple times without having duplicate entries in your database
    print("Deleting Restaurant/Customer data...")
    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.query(Review).delete()

    print("Creating restaurants...")
    shack = Restaurant(name = "Karen's Lobster Shack", price = 1)
    bistro = Restaurant(name = "Sanjay's Lobster Bistro", price = 2)
    palace = Restaurant(name = "Kiki's Lobster Palace", price = 3)
    restaurants = [shack, bistro, palace]

    print("Creating customers...")
    baby_spice = Customer(first_name = "Emma", last_name = "Bunton")
    ginger_spice = Customer(first_name = "Geri", last_name = "Halliwell")
    scary_spice = Customer(first_name = "Melanie", last_name = "Brown")
    sporty_spice = Customer(first_name = "Melanie", last_name = "Chisholm")
    posh_spice = Customer(first_name = "Victoria", last_name = "Addams")
    customers = [baby_spice, ginger_spice, scary_spice, sporty_spice, posh_spice]

    print("Creating reviews...")
    # ********************************************************************
    # * TODO: create reviews! Remember, a review belongs to a restaurant *
    # * and a review belongs to a customer.                              *
    # ********************************************************************
    # Create reviews Here
    r1 = Review(restaurant = shack, customer = baby_spice, star_rating = 5)
    r2 = Review(restaurant = shack, customer = sporty_spice, star_rating = 4)
    r3 = Review(restaurant = shack, customer = posh_spice, star_rating = 5)
    r4 = Review(restaurant = bistro, customer = baby_spice, star_rating = 3)
    r5 = Review(restaurant = bistro, customer = sporty_spice, star_rating = 4)
    r6 = Review(restaurant = palace, customer = ginger_spice, star_rating = 2)
    r7 = Review(restaurant = palace, customer = baby_spice, star_rating = 10)
    r8 = Review(restaurant = palace, customer = scary_spice, star_rating = 10)
    r9 = Review(restaurant = palace, customer = posh_spice, star_rating = 20)
    reviews = [r1, r2, r3, r4, r5, r6, r7, r8, r9]
    session.add_all(restaurants)
    session.add_all(customers)
    session.add_all(reviews)
    session.commit()

    print("Seeding done!")
