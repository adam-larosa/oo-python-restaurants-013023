from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Review, Customer
from unittest.mock import patch

class TestReview:
    '''Review in models.py'''

    def test_has_attributes(self):
        '''has attributes id, star_rating, last_name, restaurants, reviews'''

        engine = create_engine("sqlite:///restaurants.db")
        Session = sessionmaker(bind=engine)
        session = Session()

        customer = Customer(first_name="Steve", last_name="Wayne")
        bistro = Restaurant(name = "Sanjay's Lobster Bistro", price = 2)
        review = Review(star_rating = 5, restaurant = bistro, customer= customer)
        session.add_all([customer, bistro, review])
        session.commit()
        assert hasattr(customer, "id")
        assert hasattr(customer, "first_name")
        assert hasattr(customer, "last_name")
        assert hasattr(customer, "reviews")
        assert hasattr(customer, "restaurants")

        session.query(Restaurant).delete()
        session.query(Review).delete()
        session.query(Customer).delete()

        session.commit()

    def test_has_a_restaurant(self):
        '''has an attribute "restaurant" that is a Restaurant record.'''

        engine = create_engine("sqlite:///restaurants.db")
        Session = sessionmaker(bind=engine)
        session = Session()

        customer = Customer(first_name="Steve", last_name="Wayne")
        customer2 = Customer(first_name="Jason", last_name="Maxwell")

        bistro = Restaurant(name = "Sanjay's Lobster Bistro", price = 2)
        palace = Restaurant(name = "Kiki's Lobster Palace", price = 3)

        review = Review(star_rating = 5, restaurant = bistro, customer= customer)
        review2 = Review(star_rating = 5, restaurant = palace, customer= customer)

        session.add_all([customer, bistro, palace, customer2,  review, review2])
        session.commit()

        assert review.restaurant == bistro

        session.query(Restaurant).delete()
        session.query(Review).delete()
        session.query(Customer).delete()

        session.commit()

    def test_has_a_customer(self):
        '''has an attribute "customer" that is a Customer record.'''

        engine = create_engine("sqlite:///restaurants.db")
        Session = sessionmaker(bind=engine)
        session = Session()

        customer = Customer(first_name="Steve", last_name="Wayne")
        customer2 = Customer(first_name="Jason", last_name="Maxwell")

        bistro = Restaurant(name = "Sanjay's Lobster Bistro", price = 2)
        palace = Restaurant(name = "Kiki's Lobster Palace", price = 3)

        review = Review(star_rating = 5, restaurant = bistro, customer= customer)
        review2 = Review(star_rating = 5, restaurant = palace, customer= customer)

        session.add_all([customer, bistro, palace, customer2,  review, review2])
        session.commit()

        assert review.customer == customer

        session.query(Restaurant).delete()
        session.query(Review).delete()
        session.query(Customer).delete()

        session.commit()
