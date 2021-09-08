from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

from jwt_auth.serializers import PopulatedUserSerializer

User = get_user_model()

class ProfileView(APIView):

    def get(self, _request, pk):
        try :
            user = User.objects.get(pk=pk)
            serialized_user = PopulatedUserSerializer(user)
            return Response(serialized_user.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            raise NotFound()
