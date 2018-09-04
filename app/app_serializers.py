from rest_framework import serializers
from backweb.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'desc', 'is_show', 'is_recommend','content','image_url','oprate_time']