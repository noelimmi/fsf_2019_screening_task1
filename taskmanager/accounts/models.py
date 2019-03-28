from django.db import models
from django.contrib.auth.models import User
from usergroups.models import Team
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    github = models.URLField(max_length=400, blank=True)
    linkedin = models.URLField(max_length=400, blank=True)
    teamcreated = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="myteam", null=True, blank=True)
    teamenrolled = models.ManyToManyField(
        Team, related_name="enrolledteam", blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        # below statement is to make the Parent class method to run before our changes
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
