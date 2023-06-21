from rest_framework import serializers

class QuizResponseSerializer(serializers.Serializer):
    store_name = serializers.CharField()
    quiz_id = serializers.ListField(child=serializers.CharField())
