from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from alphacloud.models import Alphacloud
from alphacloud.serializers import AlphacloudSerializer

######################################################
# Start CBV
######################################################
class AlphacloudListCbv(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self,request,format=None):
        alphacloud = Alphacloud.objects.all()
        serializer = AlphacloudSerializer(alphacloud, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = AlphacloudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AlphacloudUpdateCbv(APIView):
    def get_object(self, pk):
        try:
            return Alphacloud.objects.get(pk=pk)
        except Alphacloud.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        alphacloud = self.get_object(pk)
        serializer = AlphacloudSerializer(alphacloud)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        alphacloud = self.get_object(pk)
        serializer = AlphacloudSerializer(alphacloud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        alphacloud = self.get_object(pk)
        alphacloud.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
######################################################
# End CBV
######################################################
'''
######################################################
# Start FBV
######################################################

# @csrf_exempt
@api_view(['GET', 'POST'])
def alphacloud_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        alphacloud = Alphacloud.objects.all()
        serializer = AlphacloudSerializer(alphacloud, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        # serializer = AlphacloudSerializer(data=data)
        serializer = AlphacloudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        #     return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def alphacloud_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        alphacloud = Alphacloud.objects.get(pk=pk)
    except Alphacloud.DoesNotExist:
        # return HttpResponse(status=404)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlphacloudSerializer(alphacloud)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = AlphacloudSerializer(alphacloud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data)
            return Response(serializer.data)
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        alphacloud.delete()
        # return HttpResponse(status=204)
        return Response(status=status.HTTP_204_NO_CONTENT)
######################################################
# End FBV
######################################################
'''