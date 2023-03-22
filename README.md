
A restaurant has many reviews

  restaurant -----< review 


A customer has many reviews

  customer -----< review



A review belongs to a restaurant

  review >------ restaurant 

A review belongs to a customer

  review >------ customer





                    customer -----< review >------ restaurant










# Phase 3 Code Challenge: Restaurants

For this assignment, we'll be working with a restaurant review domain.

We have three models: `Restaurant`, `Review`, and `Customer`.

For our purposes, a `Restaurant` has many `Review`s, a `Customer` has many
`Review`s, and a `Review` belongs to a `Restaurant` and to a `Customer`.

`Restaurant` - `Customer` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Instructions

Build out all of the functionality listed in the deliverables. The deliverables are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later deliverables may rely on earlier ones.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session with
your classes defined. You can test out the methods that you write here. 

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

***

## Deliverables

Write the following functionality for the classes in the files provided. Feel free to build out any helper methods if needed.


- A `Review` belongs to a `Restaurant`, and a `Review` also belongs to an `Customer`.

- The `reviews` table should also have:
  - A `star_rating` column that stores an integer.

After creating the `reviews` table using a migration, use the `seed.py` file to
create instances of your `Review` class so you can test your code.

**Once you've set up your `reviews` **, work on building out the following
deliverables.

#### Review

- `Review customer`
  - should return the `Customer` instance for this review
- `Review restaurant`
  - should return the `Restaurant` instance for this review

#### Restaurant

- `Restaurant name`
  - has a `name` that returns a string
- `Restaurant price`
  - has a `price` that returns an integer
- `Restaurant reviews`
  - returns a collection of all the reviews for the `Restaurant`
- `Restaurant customers`
  - returns a collection of all the customers who reviewed the `Restaurant`

#### Customer
- `Customer first_name` 
  - has a `first_name` that returns a string
- `Customer last_name`
  - has a `last_name` that returns a string
- `Customer reviews`
  - should return a collection of all the reviews that the `Customer` has left
- `Customer restaurants`
  - should return a collection of all the restaurants that the `Customer` has reviewed

Use `python debug.py` and check that these methods work before proceeding. 

### Aggregate and Relationship Methods

#### Customer

- `Customer full_name`
  - returns the full name of the customer, with the first name and the last name concatenated, Western style.
- `Customer favorite_restaurant`
  - returns the restaurant instance that has the highest star rating from this customer
- `Customer add_review(restaurant, rating)`
  - takes a `restaurant` (an instance of the `Restaurant` class) and a rating creates a new review for the restaurant
- `Customer delete_reviews(restaurant)`
  - takes a `restaurant` (an instance of the `Restaurant` class) and removes **all** their reviews for this restaurant
  - you will have to delete entries from the `reviews` to get this to work!

#### Review

- `Review full_review`
  - should return a string formatted as follows:

```txt
Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.
```

#### Restaurant

- `Restaurant all_reviews`
  - should return an list of strings with all the reviews for this restaurant
    formatted as follows:

```py
[
  "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
  "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
]
```
