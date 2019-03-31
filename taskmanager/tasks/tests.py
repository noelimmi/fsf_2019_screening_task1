from django.test import TestCase, Client
from django.urls import reverse
from .models import Task


class TestTaskView(TestCase):

    def test_task_done_by_user_not(self):
        client = Client()
        response = client.get(reverse('task-manager'))

        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'tasks/taskslist.html')
