from django.contrib.auth import get_user_model
from django.test import TestCase

from core import models


def sample_user(email="test@londonappdev.com", password="testpass"):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email"""
        email = "loren@company.com"
        password = "secretpassword"

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password), True)

    def test_new_user_email_normalized(self):
        """Test that new user's email is normalized"""
        email = "loren@ComPany.com"
        user = get_user_model().objects.create_user(email, "passwordhere")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "passwordhere")

    def test_create_super_user(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            "loren@company.com", "passwordhere"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(user=sample_user(), name="Vegan")
        self.assertEqual(str(tag), tag.name)
