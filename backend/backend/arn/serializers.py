from rest_framework import serializers
from arn.models import Arn, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class ArnSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Arn
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']

    def create(self, validated_data):
        """
        Create and return a new 'Snippet' instance, given the validated data.
        """
        return Arn.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Snippet' instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.codee)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Arn.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']