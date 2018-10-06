from rest_framework import serializers
from backweb.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title', 'desc', 'is_read', 'is_recommend',
                  # 'content',
                  'image_url','oprate_time']