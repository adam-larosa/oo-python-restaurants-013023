from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Review, Customer
from unittest.mock import patch

class TestCustomer:
    '''Product in models.py'''

    def test_has_attributes(self):
        '''has attributes id, first_name, last_name, restaurants, reviews'''

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
        assert len(customer.reviews) == 2
        assert review in customer.reviews 
        assert review2 in customer.reviews 

        session.query(Restaurant).delete()
        session.query(Review).delete()
        session.query(Customer).delete()

        session.commit()

    def test_has_many_restaurants(self):
        '''has an attribute "restaurants" that is a sequence of Restaurant records.'''

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

    def test_has_many_restaurants(self):
        '''has an attribute "restaurants" that is a sequence of Restaurant records.'''

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

    def test_full_name(self):
        '''has an function "full_name" that returns a string of the customers full name.'''

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

        assert customer.full_name() == 'Steve Wayne'
        session.query(Restaurant).delete()
        session.query(Review).delete()
        session.query(Customer).delete()

        session.commit()

    def test_favorite_restaurant(self):
        '''has an function "favorite_restaurant" returns the customers favorite restaurant.'''

        engine = create_engine("sqlite:///restaurants.db")
        Session = sessionmaker(bind=engine)
        session = Session()

        customer = Customer(first_name="Steve", last_name="Wayne")
        customer2 = Customer(first_name="Jason", last_name="Maxwell")

        bistro = Restaurant(name = "Sanjay's Lobster Bistro", price = 2)
        palace = Restaurant(name = "Kiki's Lobster Palace", price = 3)
        shack = Restaurant(name = "Karen's Lobster Shack", price = 1)

        review = Review(star_rating = 3, restaurant = bistro, customer= customer)
        review2 = Review(star_rating = 5, restaurant = palace, customer= customer)

        session.add_all([customer, bistro, palace, customer2,  review, review2])
        session.commit()

        assert customer.favorite_restaurant() == palace
        session.query(Restaurant).delete()
        session.query(Review).delete()
        session.query(Customer).delete()

        session.commit()

    def test_add_review(self):
        '''has an function "add_review" adds a review for the restaurant.'''

        engine = create_engine("sqlite:///restaurants.db")
        Session = sessionmaker(bind=engine)
        session = Session()

        customer = Customer(first_name="Steve", last_name="Wayne")
        customer2 = Customer(first_name="Jason", last_name="Maxwell")

        bistro = Restaurant(name = "Sanjay's Lobster Bistro", price = 2)
        palace = Restaurant(name = "Kiki's Lobster Palace", price = 3)
        shack = Restaurant(name = "Karen's Lobster Shack", price = 1)

        review = Review(star_rating = 3, restaurant = bistro, customer= customer)
        review2 = Review(star_rating = 5, restaurant = palace, customer= customer)

        session.add_all([customer, bistro, palace, shack, customer2,  review, review2])
        session.commit()

        customer.add_review(shack, 5)
        assert shack in customer.restaurants
        assert customer.reviews[2].star_rating == 5
        session.query(Restaurant).delete()
        session.query(Review).delete()
        session.query(Customer).delete()

        session.commit()
    
    def test_delete_review(self):
        '''has an function "delete_review" deletes all reviews for the restaurant from customer.'''

        engine = create_engine("sqlite:///restaurants.db")
        Session = sessionmaker(bind=engine)
        session = Session()

        customer = Customer(first_name="Steve", last_name="Wayne")
        customer2 = Customer(first_name="Jason", last_name="Maxwell")

        bistro = Restaurant(name = "Sanjay's Lobster Bistro", price = 2)
        palace = Restaurant(name = "Kiki's Lobster Palace", price = 3)
        shack = Restaurant(name = "Karen's Lobster Shack", price = 1)

        review = Review(star_rating = 3, restaurant = bistro, customer= customer)
        review2 = Review(star_rating = 5, restaurant = palace, customer= customer)
        review3 = Review(star_rating = 5, restaurant = shack, customer= customer2)

        session.add_all([customer, bistro, palace, shack, customer2,  review, review2, review3])
        session.commit()

        customer.delete_reviews(bistro) 
        assert bistro not in customer.restaurants
        assert palace in customer.restaurants
        assert review not in customer.reviews
        assert review3 in customer2.reviews
        session.query(Restaurant).delete()
        session.query(Review).delete()
        session.query(Customer).delete()

        session.commit()
