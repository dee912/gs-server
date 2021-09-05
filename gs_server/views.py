from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Shoe
from .serializers import ShoeSerializer

class ShoeListView(APIView):

    def get(self, _request):
        shoes = Shoe.objects.all()
        serialized_shoes = ShoeSerializer(shoes, many=True)
        return Response(serialized_shoes.data, status=status.HTTP_200_OK)


class ShoeDetailView(APIView):

    def get(self, _request, pk):
        shoe = Shoe.objects.get(pk=pk)
        serialized_shoe = ShoeSerializer(shoe)
        return Response(serialized_shoe.data, status=status.HTTP_200_OK)
