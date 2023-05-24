from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from movies.models import Genre

@api_view(['POST'])
def sign_up(request):
    User = get_user_model()
    username = request.data.get('username')
    password1 = request.data.get('password1')
    password2 = request.data.get('password2')
    selected_genres = request.data.get('selectedGenres')

    # 입력 유효성 검사 및 비밀번호 확인
    if not username or not password1 or not password2 or password1 != password2:
        return Response({'message': 'Invalid data'}, status=400)

    # 선택한 장르들을 가져와서 User 객체 생성
    selected_genres = Genre.objects.filter(id__in=selected_genres)
    user = User.objects.create_user(username=username, password=password1)
    user.selectedGenres.set(selected_genres)

    # 성공적으로 회원가입한 경우
    return Response({'message': 'User created successfully'}, status=201)