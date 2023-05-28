import random
import factory

from django.test import TestCase
from .models import User

class RandomUserFactory(factory. django. DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    age = random.randint(1, 100)
    class Meta:
        model = User

class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(first_name='Test', last_name="Test", age=19)
    def test_user(self):
        self.assertIsInstance(self.user, User)


class UserViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = RandomUserFactory.create()

    def test_users_list(self):
        resp = self.client.get(f'/users/')
        self.assertEqual(resp.status_code, 200)

    def test_get_user_detail(self):
        resp = self.client.get(f'/users/{self.user.id}/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('first_name'), self.user.first_name)

    def test_delete_user(self):
        resp = self.client.delete(f'/users/{self.user.id}/')
        self.assertEqual(resp.status_code, 204)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=self.user.id)