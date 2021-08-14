from rest_framework import serializers
from .models import Doibong,Cauthu

class CauThuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cauthu
        fields="__all__"

class DoiBongSerializer(serializers.ModelSerializer):
    cauthu_set = CauThuSerializer(many=True, read_only=True)
    key = serializers.CharField(source='get_key', read_only=True)

    class Meta:
        model=Doibong
        fields=('id', 'name','short_name', 'area','cauthu_set','key')

