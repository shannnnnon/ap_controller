from rest_framework import serializers
from ntnuapp.models import AP


class APSerializer(serializers.ModelSerializer):
    class Meta:
        model = AP
        # fields = '__all__'
        fields = ('id', 'name', 'ap_id')
