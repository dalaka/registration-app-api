from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_username_successful(self):
        """Test to create a user with username successful"""
        username = "dalaka@gmail.com"
        password = "password"
        user = get_user_model().objects.create_user(
            username=username, password=password)
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            'dalaka@gmail.com',
            'test12234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
