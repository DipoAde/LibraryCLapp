import unittest
import Library



Library.User.UserBase["Didaade"] = {'first_name': "Dipo",
                            'last_name':"Ade",
                            'email':"email", 
                            'password': "password" }


Library.Book_Archive.archive[Library.book_ID("running", "1")] = {'title' : "running", 
                                        'book_number' : "1",
                                        'image': "na", 
                                        'description': "Great adventure tail"
                                        }
Library.Book_Archive.archive[Library.book_ID("walking", "1")] = {'title' : "walking", 
                                        'book_number' : "1",
                                        'image': "na", 
                                        'description': "Great adventure tail"
                                        }

Library.Book_Archive.borrowed_books_dictionary[Library.book_ID("swimming","1")] = {'title': "swimming",
                                                                'first_name': "Dipo", 
                                                                'last_name': "Ade",
                                                                'email': "email",
                                                                'return_date': Library.datetime.today().strftime('%Y-%m-%d')
                                                                }

class TestLibrary(unittest.TestCase):
    def test_bookID(self):
        result = Library.book_ID("running","1")
        answer = ["running","1"]
        self.assertEqual(result, str(hash(tuple(answer))))

    def test_return_date(self):
        result = Library.return_date()
        self.assertEqual(result, ((Library.datetime.today()+Library.timedelta(weeks=4)).strftime('%Y-%m-%d')))

    def test_automatic(self):
        Library.Automatic()
        result = []
        if Library.book_ID("running","1") in Library.Book_Archive.available_books:
            result.append(True)
        if Library.book_ID("swimming","1") in Library.Book_Archive.books_on_loan:
            result.append(True)
        if Library.book_ID("swimming","1") in Library.Book_Archive.books_due_today:
            result.append(True)
        self.assertEqual(result,[True,True,True])


if __name__ == "__main__":
    unittest.main()




