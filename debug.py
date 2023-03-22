import ipdb
from lib import *

# code here...

adam = Customer( "Adam", "La Rosa" )
emiley = Customer( "Emiley", "San Jose" )



veronas = Restaurant( "Verona's", 10 )
bk = Restaurant( "Burger King", 3 )


r1 = Review( 5, adam, veronas )
r2 = Review( 2, adam, bk )
r3 = Review( 1, adam, bk )

r4 = Review( 4, emiley, bk )

# veronas.reviews, bk.reviews
ipdb.set_trace()