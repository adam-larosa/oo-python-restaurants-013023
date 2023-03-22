from .review import Review

class Restaurant:
    def __init__( self, name, price ):
        self.name = name
        self.price = price
       
    @property
    def reviews( self ):
        return [ r for r in Review.all if r.restaurant == self ]

    @property
    def customers( self ):
        return [ r.customer for r in self.reviews ]

    @property
    def all_reviews( self ):
        # string_reviews_list = []
        # for review in self.reviews:
        #     string_reviews_list.append( review.full_review )
        # return string_reviews_list 
        
        return [ r.full_review for r in self.reviews ]
        
