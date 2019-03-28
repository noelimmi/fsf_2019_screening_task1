from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1024, null=True, blank=True)
    admin = models.ForeignKey(
        User, related_name="teamadmin", null=True, on_delete=models.CASCADE)
    member = models.ManyToManyField(
        User, related_name="teammembers")

    @classmethod
    def add_member(cls, admin, new_member):
        team, created = cls.objects.get_or_create(
            admin=admin
        )
        team.member.add(new_member)

    @classmethod
    def remove_member(cls, admin, member_to_remove):
        team, created = cls.objects.get_or_create(
            admin=admin
        )
        team.member.remove(member_to_remove)

    def __str__(self):
        return str(self.name+"-"+self.admin.username)
