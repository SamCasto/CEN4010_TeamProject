from bookstore_app.models import Book, Publisher, Author, User


def populateDb():
    # adding publishers
    publisher1 = Publisher.objects.create(name="Canongate Books")
    publisher2 = Publisher.objects.create(name="Doubleday Canada")
    publisher3 = Publisher.objects.create(name="Allen Lane")

    # adding authors
    author1 = Author.objects.create(
        firstName="Matt",
        lastName="Haig",
        bio="Writer of The Midnight Library",
        publisher=publisher1
    )
    author2 = Author.objects.create(
        firstName="Bonnie",
        lastName="Garmus",
        bio="Writer of Lessons in Chemistry",
        publisher=publisher2
    )
    author3 = Author.objects.create(
        firstName="Andrew",
        lastName="Roberts",
        bio="Writer of Churchill: Walking with Destiny",
        publisher=publisher3
    )

    # adding three books
    book1 = Book.objects.create(
        isbn="9780525559474",
        title="The Midnight Library",
        desc="Somewhere out beyond the edge of the universe there is a library that contains an infinite number of books, each one the story of another reality. One tells the story of your life as it is, along with another book for the other life you could have lived if you had made a different choice at any point in your life. While we all wonder how our lives might have been, what if you had the chance to go to the library and see for yourself? Would any of these other lives truly be better?",
        price=10.99,
        author=author1,
        genre="Fiction",
        publisher=publisher1,
        yearPublished=2022,
        copiesSold=0
    )
    book2 = Book.objects.create(
        isbn="9780385547345",
        title="Lessons in Chemistry",
        desc="Chemist Elizabeth Zott is not your average woman. In fact, Elizabeth Zott would be the first to point out that there is no such thing as an average woman. But it’s the early 1960s and her all-male team at Hastings Research Institute takes a very unscientific view of equality. Except for one: Calvin Evans; the lonely, brilliant, Nobel–prize nominated grudge-holder who falls in love with—of all things—her mind. True chemistry results.",
        price=9.99,
        author=author2,
        genre="Fiction",
        publisher=publisher2,
        yearPublished=2022,
        copiesSold=0
    )
    book3 = Book.objects.create(
        isbn="9788535933239",
        title="Churchill: Walking with Destiny",
        desc="When we seek an example of great leaders with unalloyed courage, the person who comes to mind is Winston Churchill: the iconic, visionary war leader immune from the consensus of the day, who stood firmly for his beliefs when everyone doubted him. But how did young Winston become Churchill? What gave him the strength to take on the superior force of Nazi Germany when bombs rained on London and so many others had caved? In Churchill, Andrew Roberts gives readers the full and definitive Winston Churchill, from birth to lasting legacy, as personally revealing as it is compulsively readable.",
        price=1.99,
        author=author3,
        genre="Nonfiction",
        publisher=publisher3,
        yearPublished=2023,
        copiesSold=0
    )

    #adding users
    user1 = User.objects.create(
        username = "testUser1",
        password = "password1",
        firstName = "test1",
        lastName = "User1",
        email = "user1@example.com",
        address = "testAddress 1"
    )
    user2 = User.objects.create(
        username = "testUser2",
        password = "password2",
        firstName = "test2",
        lastName = "User2",
        email = "user2@example.com",
        address = "testAddress 2"
    )
    user3 = User.objects.create(
        username = "testUser3",
        password = "password3",
        firstName = "test3",
        lastName = "User3",
        email = "user3@example.com",
        address = "testAddress 3"
    )

if __name__ == '__main__':
    populateDb()