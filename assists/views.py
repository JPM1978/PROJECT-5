from .models import Assist
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AssistSerializer


class AssistViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Assist.objects.all()
    # The serializer class for serializing output
    serializer_class = AssistSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]
