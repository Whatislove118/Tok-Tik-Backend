from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer

@api_view(['POST'])
def register(request):
    response = Response()
    user = request.data.get('user')
    print(user)
    serializer = UserSerializer(data=user)
    serialized_user = None
    if serializer.is_valid():
        serialized_user = serializer.save()
    print(serialized_user.id)
    response.set_cookie('AUTH', '2', samesite='None')
    response.data = {
        'user': 1
    }
    return response

@api_view(['GET'])
def test_cookie(request):
    if not request.COOKIES.get('team'):
        response = Response("Visiting for the first time.")
        response.set_cookie('team', 'barcelona')
        return response
    else:
        return Response("Your favorite team is {}".format(request.COOKIES['team']))