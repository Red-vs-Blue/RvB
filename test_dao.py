import unittest
import dao
import random
import string

class TestDAO(unittest.TestCase):

    def test_login(self):
        response = dao.login("abc@gmail.com", "Password123")
        self.assertIsNotNone(response)

    def test_signup(self):
        letters = string.ascii_letters
        digits = string.digits
        ending = ''.join(random.choice(digits) for i in range(5))
        username = "testing" + ''.join(random.choice(letters) for i in range(7)) + ending
        firstname = ''.join(random.choice(letters) for i in range(7))
        lastname = ''.join(random.choice(letters) for i in range(7))
        email = username + "@gmail.com"
        party = "Green"
        password = "pwd" + ''.join(random.choice(letters) for i in range(7)) + ending
        response = dao.signup(username, firstname, lastname, email, party, password)
        self.assertEqual(username, response)

    def test_contact(self):
        letters = string.ascii_letters
        digits = string.digits
        name = ''.join(random.choice(letters) for i in range(7))
        ending = ''.join(random.choice(digits) for i in range(5))
        username = "testing" + ''.join(random.choice(letters) for i in range(7)) + ending
        email = username + "@gmail.com"
        message = ''.join(random.choice(letters) for i in range(20))
        response = dao.contact(name, email, message)
        self.assertEqual(email, response)

    def test_retrieve_issues(self):
        response = dao.retrieve_issues("National")
        self.assertIsNotNone(response)

    def test_retrieve_areas(self):
        response = dao.retrieve_areas("National")
        self.assertIsNotNone(response)

    def test_retrieve_thread_left(self):
        response = dao.retrieve_thread_left(2)
        self.assertIsNotNone(response)

    def test_retrieve_thread_right(self):
        response = dao.retrieve_thread_right(1)
        self.assertIsNotNone(response)

    def test_pageID_to_page(self):
        response = dao.pageID_to_page(1)
        self.assertEqual("Abortion", response)

    def test_partyID_to_party(self):
        response = dao.partyID_to_party(1)
        self.assertEqual("Republican", response)
        
if __name__ == '__main__':
    unittest.main()
