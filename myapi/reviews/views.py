from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from movies.models import Movie
from reviews.models import Comment
from reviews.serializers import CommentSerializer


@csrf_exempt
def create_review(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_id)
        content = request.POST.get('content')
        rating = request.POST.get('rating')

        review = Comment(movie=movie, content=content, rating=rating)
        review.save()

        return JsonResponse({'message': '리뷰가 성공적으로 작성되었습니다.'})
    else:
        return JsonResponse({'error': 'POST 요청이 필요합니다.'}, status=400)


def get_reviews(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Comment.objects.filter(movie=movie)
    serializer = CommentSerializer(reviews, many=True)
    return JsonResponse(serializer.data, safe=False)
