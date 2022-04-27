from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.

class DisplayJsonFile(APIView):
    def get(self, request):
        return render(request, 'Countries_File.json')
