# CEN4010_TeamProject
Spring 2023 CEN4010 Software Engineering group project

Details from the project assignment page
Feature ID
Feature Benefit
Feature Details

1 
Book Browsing and Sorting
Users will have a simple and enjoyable way to discover new books and
Authors and sort results.
REST API Actions:
   Retrieve List of Books by Genre
o Logic: Given a specific genre, return a list of books for that genre.
o HTTP Request Type: GET
o Parameters Sent: Genre
o Response Data: JSON List of book objects

   Retrieve List of Top Sellers (Top 10 books that have sold the most copied)
o Logic: Return the top 10 books that have sold the most copies in
descending order (most copies sold would be #1)
o HTTP Request Type: GET
o Parameters Sent: None
o Response Data : JSON List of book objects

   Retrieve List of Books for a particular rating and higher
o Logic: Filter by rating higher or equal to the passed rating value.
o HTTP Request Type: GET
o Parameters Sent: Rating
o Response Data: JSON List of book objects

   Discount books by publisher.
o Logic: Update the price of all books under a publisher by a discount
percent.
o HTTP Request Type: PUT or PATCH
o Parameters Sent: Discount percent, Publisher
o Response Data: None

2 
Profile Management
Users can create and maintain their profiles rather than enter in
their information each time they order
REST API Actions:
   Create a User with username, password and optional fields (name, email
address, home address)
o Logic: Provided the user fields, create the user in the database..
o HTTP Request Type: POST
o Parameters Sent: User Object
o Response Data: None

   Retrieve a User Object and its fields by their username
o Logic: Given a specific username, retrieve the user details.
o HTTP Request Type: GET
o Parameters Sent: Username
o Response Data: JSON User object.

   Update the user and any of their fields except for mail
o Logic: Given the username as a key lookup value and any other user
field, update that user field with the new param value.
o HTTP Request Type: PUT / PATCH
o Parameters Sent: Username
o Response Data: None

   Create Credit Card that belongs to a User
o Logic: Given a user name and credit card details, create a credit
card for that user.
o HTTP Request Type: POST
o Parameters Sent: User name, Credit Card Object
o Response Data: None

3
Shopping Cart Users can manage items in a shopping cart for immediate or future Purchase
REST API Actions:
   Retrieve the subtotal price of all items in the user’s shopping cart.
o Logic: Give a user Id,return the subtotal of the books in the cart.
o HTTP Request Type: GET
o Parameters Sent: User Id
o Response Data: Calculated Subtotal

   Add a book to the shopping cart.
o Logic: Provided with a book Id and a User Id, add the book to the
user’s shopping cart.
o HTTP Request Type: POST
o Parameters Sent: Book Id, User Id
o Response Data: None

   Retrieve the list of book(s) in the user’s shopping cart.
o Logic: Give a user Id, return a list of books that are in the shopping
cart.
o HTTP Request Type: GET
o Parameters Sent: User Id
o Response Data: List of Book Objects

   Delete a book from the shopping cart instance for that user.
o Logic: Given a book If and a User Id, remove the book from the
user’s shopping cart.
o HTTP Request Type: DELETE
o Parameters Sent: Book Id, User Id
o Response Data: None


4 <br>
Book Details Users can see informative and enticing details about a book <br>
Developer: Sam Casto <br>
REST API Actions: <br>
   An administrator must be able to create a book with the book ISBN, book
name, book description, price, author, genre, publisher , year published and
copies sold.
o Logic: Given a Book’s info, add it to the system.
o HTTP Request Type: POST
o Parameters Sent: Book Object
o Response Data: None

   Must be able retrieve a book’s details by the ISBN
o Logic: Given a book id, retrieve the book information
o HTTP Request Type: GET
o Parameters Sent: Book Id
o Response Data: Book object JSON

   An administrator must be able to create an author with first name, last
name, biography and publisher
o Logic: Given an Author’s Info, add it to the system.
o HTTP Request Type: POST
o Parameters Sent: Author Object
o Response Data: None

   Must be able to retrieve a list of books associated with an author
o Logic: Given an Author’s Id, return the list of books for that author.
o HTTP Request Type: GET
o Parameters Sent: Author Id
o Response Data: JSON list of Book Objects

5
Book Rating and Commenting
Users can rate AND comment on books they’ve purchased to help others in their
selection
REST API Actions:
   Must be able to create a rating for a book by a user on a 5 star scale with a
datestamp
o Logic: Create a rating for a book given by a user.
o HTTP Request Type: POST
o Parameters Sent: Rating, User Id, Book Id
o Response Data: None

   Must be able to create a comment for a book by a user with a datestamp
o Logic: Create a comment for a book given by a user.
o HTTP Request Type: POST
o Parameters Sent: Comment, User Id, Book Id
o Response Data: None

   Must be able to retrieve a list of all comments for a particular book.
o Logic: Retrieve a list of comments for the book
o HTTP Request Type: GET
o Parameters Sent: Book Id
o Response Data: JSON list of comments

   Must be able to retrieve the average rating for a book
o Logic: Given a book Id, calculate the average rating as a decimal.
o HTTP Request Type: GET
o Parameters Sent: Book Id
o Response Data: Computed Average rating (decimal)
