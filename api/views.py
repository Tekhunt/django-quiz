from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from api.utils import get_quiz_ids
from .serializers import QuizResponseSerializer

@extend_schema(tags=["Quiz IDs"])
class QuizIdsView(APIView):
    seri
    def get(self, request, store):
        quiz_ids = get_quiz_ids(store)
        serializer = QuizResponseSerializer(data={
            'store_name': store,
            'quiz_id': quiz_ids,
        })
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    
class Home(APIView):
    def get(self, request):
        
        return Response({
            'message': 'Welcome to quiz app'
        })

