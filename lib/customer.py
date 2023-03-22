from .review import Review

class Customer:
    def __init__( self, first_name, last_name ):
        self.first_name = first_name
        self.last_name = last_name


    @property
    def reviews( self ):
        return [ r for r in Review.all if r.customer == self ]

    @property
    def restaurants( self ):
        return [ r.restaurant for r in self.reviews ]

    @property
    def full_name( self ):
        return f"{self.first_name}" + f" {self.last_name}"

    # returns the restaurant instance that has the highest star rating from this 
    # customer
    @property
    def favorite_restaurant( self ):
        rating = 0
        restaurant_instance = ''
        for review in self.reviews:
            if review.star_rating >= rating:
                rating = review.star_rating
                restaurant_instance = review.restaurant
        return restaurant_instance

        # reviews = self.reviews
        # reviews.sort( key=lambda r : r.star_rating )
        # return reviews[-1].restaurant

        # def by_rating( review ):
        #     return review.star_rating
        # new_list = self.reviews
        # new_list.sort( key=by_rating )
        # return new_list[-1].restaurant


    # takes a restaurant (an instance of the Restaurant class) and a 
    # rating creates a new review for the restaurant
    def add_review( self, restaurant, rating ):
        Review( rating, self, restaurant )
        

    # takes a restaurant (an instance of the Restaurant class) and removes 
    # all their reviews for this restaurant you will have to delete entries 
    # from the reviews to get this to work!
    def delete_reviews( self, restaurant ):
        doomed_list = [ r for r in self.reviews if r.restaurant == restaurant ]
        for review in doomed_list:
            Review.all.remove( review )
