from rest_framework.serializers import ModelSerializer
from ..models import Category
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name','img_src','created_at','modified_at')