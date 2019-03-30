from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Team(models.Model):
    name = models.CharField(max_length=100)
    teamicon = models.ImageField(
        default='groupdefault.png', upload_to='group_icons')
    description = models.TextField(max_length=1024, null=True, blank=True)
    admin = models.ForeignKey(
        User, related_name="teamadmin", null=True, on_delete=models.CASCADE)
    member = models.ManyToManyField(
        User, related_name="teammembers")

    def __str__(self):
        return str(str(self.id) + "-" + self.name+"-"+self.admin.username)

    def save(self, **kwargs):
        # below statement is to make the Parent class method to run before our changes
        super().save()

        img = Image.open(self.teamicon.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.teamicon.path)
