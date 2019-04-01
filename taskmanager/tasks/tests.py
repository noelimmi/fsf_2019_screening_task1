from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task


class TestTaskView(TestCase):
    def setUp(self):
        self.grouptask = Task.objects.get(pk=29)
        self.personaltask = Task.objects.get(pk=28)
        self.admin = User.objects.get(username="admin")

    def test_to_select_only_user_personal_task(self):
        userlisttask = self.admin.tasks.filter(
            ownwer=self.admin, team__isnull=True)
        check = False
        if self.grouptask in userlisttask:
            check = True
