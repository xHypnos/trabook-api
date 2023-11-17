from rest_framework.views import APIView
from rest_framework.response import Response
from card.models import Card
from .serializers import CardSerializer
from rest_framework.decorators import api_view

class CardView(APIView):
    def get(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

""" @api_view(['GET'])
def CardView(request):
    cards = Card.objects.all()
    serializer = CardSerializer(cards, many=True)
    return Response(serializer.data) """




""" def post(self, request):
        serializer = CommnetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) """