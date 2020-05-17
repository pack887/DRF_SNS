from django.test import TestCase
from sns.logic import mul
from django.contrib.auth import get_user_model


# class LogicTest(TestCase):
#     def test_mul(self):
#         self.assertEqual(mul(2, 3), 5)


class UserCreateTests(TestCase):
    def test_createuser(self):
        email = 'dummy@gmail.com'
        password = 'dummy'

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
