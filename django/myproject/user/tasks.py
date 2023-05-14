from celery import shared_task
from .models import User
from purchase.models import Purchase


@shared_task
def print_text():
    print("Hello, world!")

@shared_task
def purchase(user_id):
    user = User.objects.get(id=user_id)
    purchases = Purchase.objects.filter(user=user).count()
    print(f"User {user.first_name} has {purchases} purchase(s).")

@shared_task
def users():
    users = User.objects.count()
    print(f"There are {users} users in the database.")