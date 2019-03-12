from rest_framework import serializers
from comments.models import Comment


# Task Serializers
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'id', 'content')
