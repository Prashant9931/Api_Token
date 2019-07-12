from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from pymongo import response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.response import Response
from django.contrib.auth.models import User,auth
from .models  import Book
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    else:
        user = User.objects.create_user(username=username, password=password)
        user.save();
        return Response({'Result': 'user Registered'},
                        status=HTTP_200_OK)

#
# class CustomObtainAuthToken(ObtainAuthToken):
#
#     def post(self, request, *args, **kwargs):
#         response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
#         token = Token.objects.get(key=response.data['token'])
#         return Response({'token': token.key, 'id': token.user_id})






@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def book_fill(request):
    # token = Token.objects.get(key=response.data['token'])
    id = request.data.get("id")
    title= request.data.get("title")
    author = request.data.get("author")

    token_detail = Token.objects.get(user=request.user)

    print("working")
    user1 = User.objects.get(username=request.user)
    if id is None or user1.id is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    else:
        user1= Book.objects.create(user_id=user1,title=title,author=author)
        user1.save();
        return Response({'Result': 'user Registered'},
                        status=HTTP_201_CREATED)



@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def findbook(request):
    # token=request.data.get("Token")
    print(request.user)
    token_detail=Token.objects.get(user=request.user)
    print("working")
    user=Book.objects.filter(user_id=request.user)
    print(user)
    ti=[]
    au=[]
    for i in user:
        ti.append(i.title)
        au.append(i.author)
    d={}
    d['title']=ti
    d['author']=au
    # data = {'username':user.username,'password':user.password}
    return Response(d, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def findbook_with_id(request):
    k = request.query_params.get('id')
    id=int(k)
    token_detail=Token.objects.get(user=request.user)
    user=Book.objects.filter(id = id)
    result=[]
    for i in user:
        d={}
        d['id']=i.id
        d['title']=i.title
        d['author']=i.author
        result.append(d)
        print(i.id,i.title)
    # data = {'username':user.username,'password':user.password}
    return Response(result, status=HTTP_200_OK)



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    # token, _ = Token.objects.get_or_create(user=user)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def sample_api(request):
    # token=request.data.get("Token")
    print(request.user)
    token_detail=Token.objects.get(user=request.user)
    print("working")
    user=User.objects.filter(username=request.user)
    print(request.user)
    # data = {'username':user.username,'password':user.password}
    return Response({'Message':'Authentication Complete'}, status=HTTP_200_OK)
