from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Restaurant, Review, Customer
from unittest.mock import patch

class TestRestaurant:
    '''Restaurant in models.py'''

    def test_has_attributes(self):
        '''has attributes id, name, price, customers, reviews'''

        engine = create_engine("sqlite:///restaurants.db")
        Session = sessionmaker(bind=engine)
        session = Session()

        customer = Customer(first_name="Steve", last_name="Wayne")
        bistro = Restaurant(name = "Sanjay's Lobster Bistro", price = 2)
        review = Review(star_rating = 5, restaurant = bistro, customer= customer)
        session.add_all([customer, bistro, review])
        session.commit()
        assert hasattr(bistro, "id")
        assert hasattr(bistro, "name")
        assert hasattr(bistro, "price")
        assert hasattr(bistro, "reviews")
        assert hasattr(bistro, "customers")

        session.query(Restaurant).delete()
        session.query(Review).delete()
        session.query(Customer).delete()

        session.commit()

    def test_has_many_reviews(self):
        '''has an attribute "reviews" that is a sequence of Review records.'''

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
        assert len(bistro.reviews) == 1
        assert review in bistro.reviews 
        assert review2 not in bistro.reviews 

        session.query(Restaurant).delete()
        session.query(Review).delete()
        session.query(Customer).delete()

        session.commit()

    def test_has_many_customers(self):
        '''has an attribute "customers" that is a sequence of Customer records.'''

        engine = create_engine("sqlite:///restaurants.db")
        Session = sessionmaker(bind=engine)
        session = Session()

        customer = Customer(first_name="Steve", last_name="Wayne")
        customer2 = Customer(first_name="Jason", last_name="Maxwell")

        bistro = Restaurant(name = "Sanjay's Lobster Bistro", price = 2)
        palace = Restaurant(name = "Kiki's Lobster Palace", price = 3)
        shack = Restaurant(name = "Karen's Lobster Shack", price = 1)

        review = Review(star_rating = 5, restaurant = bistro, customer= customer)
        review2 = Review(star_rating = 5, restaurant = palace, customer= customer)

        session.add_all([customer, bistro, palace, customer2,  review, review2])
        session.commit()
        assert len(customer.restaurants) == 2
        assert bistro in customer.restaurants 
        assert palace in customer.restaurants 
        assert shack not in customer.restaurants

        session.query(Restaurant).delete()
        session.query(Review).delete()
        session.query(Customer).delete()

        session.commit()

    def test_all_reviews(self):
        '''has an attribute "all_reviews" that returns a list of reviews for the restaurant.'''

        engine = create_engine("sqlite:///restaurants.db")
        Session = sessionmaker(bind=engine)
        session = Session()

        customer = Customer(first_name="Steve", last_name="Wayne")
        customer2 = Customer(first_name="Jason", last_name="Maxwell")

        bistro = Restaurant(name = "Sanjay's Lobster Bistro", price = 2)
        palace = Restaurant(name = "Kiki's Lobster Palace", price = 3)
        shack = Restaurant(name = "Karen's Lobster Shack", price = 1)

        review = Review(star_rating = 5, restaurant = bistro, customer= customer)
        review2 = Review(star_rating = 5, restaurant = bistro, customer= customer2)

        session.add_all([customer, bistro, palace, shack, customer2,  review, review2])
        session.commit()
        assert bistro.all_reviews() == ["Review for Sanjay's Lobster Bistro by Steve Wayne: 5 stars.", "Review for Sanjay's Lobster Bistro by Jason Maxwell: 5 stars."]

        session.query(Restaurant).delete()
        session.query(Review).delete()
        session.query(Customer).delete()

        session.commit()
