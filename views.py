from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_404_NOT_FOUND

from .serializers import UserSerializer
from .models import User


@api_view(['GET'])
def get_users(request):
    
    if request.method =='GET':
        users = User.objects.all()
        
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    return Response(status=HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def get_by_nick(request, nick):
    
    try:
        user = User.objects.get(pk=nick)
    except:
        return Response(status=HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED) # type: ignore
        return Response(status=HTTP_400_BAD_REQUEST) 

#CRUD
@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request):
    if request.method == 'GET':
        
        try:
            if request.GET['user']:
                user_nickname = request.GET['user']
                user = User.objects.get(pk=user_nickname)
                
                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return Response(status=HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=HTTP_400_BAD_REQUEST)

#DADOS
 
    if request.method == 'POST':
        new_user = request.data 
        serializer = UserSerializer(data=new_user)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED) # type: ignore
        return Response(status=HTTP_400_BAD_REQUEST)

#DADOOS PUT
    if request.method == 'PUT':
        nickname = request.data['user_nickname']
    try:
        updated_user = User.objects.get(pk=nickname)
    except:
        return Response(status=HTTP_404_NOT_FOUND)
    
    print(f'Data = {request.data}')
    serializer = UserSerializer(updated_user, data=request.data)
        
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED) # type: ignore
    return Response(status=HTTP_400_BAD_REQUEST)

#DELETE OBJETOS 

    if request.method == 'DELETE':
        try:
            user_to_delete = User.objects.get(pk=request.data['user_nickname'])
            user_to_delete.delete()
            return Response(status=HTTP_202_ACCEPTED)
        except:
            return Response(status=HTTP_400_BAD_REQUEST)
    






















#def databeseEmDjando():
#  data = User.objects.get(pk='weslley_nick') #objeto
# data = User.objects.filter(user_age='20')   #queryset
# data = User.objects.exclude(user_age='20')       #queryset
    
 
# data.save()
# data.delete()