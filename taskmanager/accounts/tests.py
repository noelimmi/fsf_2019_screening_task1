from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileModelTest(TestCase):
    def test_creating_user_signals_fires_up(self):
        user = User.objects.create_user(
            username="test1user", email="testuser@gmail.com", password="wasd1234")
        test = False
        if user.profile:
            test = True

        self.assertIs(test, True)

    def test_puting_a_default_img_fires_up(self):
        user = User.objects.create_user(
            username="test1user", email="testuser@gmail.com", password="wasd1234")
        test = False
        if user.profile.image.url == '/media/default.jpg':
            test = True

        self.assertIs(test, True)
