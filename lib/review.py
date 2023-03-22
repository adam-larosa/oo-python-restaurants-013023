
class Review:
    all = []

    def __init__( self, star_rating, customer_instance, restaurant_instance ):
        self.star_rating = star_rating
        self.customer = customer_instance
        self.restaurant = restaurant_instance
        Review.all.append( self )

    # Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.
    @property
    def full_review( self ):
        #how to do the same but on seperate lines....
        # return f"Review for {self.restaurant.name} by " \
        # + f" {self.customer.full_name}: {self.star_rating} stars."
        return f"Review for {self.restaurant.name} by {self.customer.full_name}: {self.star_rating} stars."