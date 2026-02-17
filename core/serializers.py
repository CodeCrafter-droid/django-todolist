from rest_framework import serializers
from .models import taskdata

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = taskdata
        fields = "__all__"