import os

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from Tik_Tok import settings
from accounts.models import User
from jwtauth.utils import get_user_id_from_payload
from profilesettings.models import ProfileSettings
from statistic.models import VideoStatistics, VideoComments, Hashtags, HashtagsOnVideo
from video.models import Audio, Video


@api_view(['POST'])
def add_video(request: Request):
    access_token = request.headers.get('Access-Token')
    user_id = get_user_id_from_payload(access_token)
    audio_data = {
        'name': request.data.get('audio_name'),
        'author_name': request.data.get('author_name')
    }
    print(audio_data)
    audio = Audio(name=audio_data.get('name'), author_name=audio_data.get('author_name'))
    audio.save()

    video = request.data.get('video')
    path = os.path.join(settings.BASE_DIR) + '/static/video/{}/'.format(video)
    # if not os.path.isfile(path):
    default_storage.save(os.path.join(settings.BASE_DIR) + '/static/video/{}/'.format(video), ContentFile(video.read()))

    video_data = {
        'url': '/static/video/{}/'.format(video),
        'user_id': User.objects.get(id=user_id),
        'description': request.data.get('video_description'),
        'audio_id': audio,
    }

    video = Video(url=video_data.get('url'), uri=video_data.get('url'), user_id=video_data.get('user_id'),
                  description=video_data.get('description'), audio_id=video_data.get('audio_id'))
    video.save()
    video = VideoStatistics.objects.get(id=video.video_id)
    hashtags_array = request.data.get('hashtags').split(' ')
    print(hashtags_array)
    for i in hashtags_array:
        hashtag = Hashtags(hashtag=i)
        hashtag.save()
        hashtags_on_video = HashtagsOnVideo(video_id=video, hashtag=hashtag)
        hashtags_on_video.save()

    print(video_data)
    return Response('LOL', status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def get_video(request: Request):
    if request.method == 'POST':
        user_id = request.data.get('id')
        print('POST1')
    else:
        access_token = request.headers.get('Access-Token')
        user_id = get_user_id_from_payload(access_token)
    videos = Video.objects.all().filter(user_id=user_id)
    data = {}
    for i in range(videos.__len__()):
        video = {
            "url":videos[i].url,
            "id": videos[i].video_id
        }
        data[i] = video
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_videos(request: Request):
    videos = Video.objects.all()
    data = {}
    for i in range(videos.__len__()):
        hashtags_array = HashtagsOnVideo.objects.filter(video_id=videos[i].video_id)
        hashtags = ''
        for j in range(len(hashtags_array)):
            hashtags += hashtags_array[j].hashtag.hashtag
            print(hashtags)
        video = {
            'url': videos[i].url,
            'description': videos[i].description,
            'id': videos[i].video_id,
            'user_id': videos[i].user_id.id,
            'likes': VideoStatistics.objects.get(id=videos[i].video_id).likes,
            'username':  ProfileSettings.objects.get(id=videos[i].user_id).username,
            'hashtags': hashtags
        }
        data[i] = video
    return Response(data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def like_video(request: Request):
    video_id = request.data.get('video_id')
    video_statistics = VideoStatistics.objects.get(id=video_id)
    video_statistics.likes += 1
    video_statistics.save()

    return Response({'likes': video_statistics.likes}, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_audio(request: Request):
    video_id = request.data.get('video_id')
    video = Video.objects.get(video_id=video_id)
    audio = Audio.objects.get(audio_id=video.audio_id.audio_id)
    print(audio)
    data = {}
    data[0] = {
        'author_name': audio.author_name,
        'audio_name': audio.name
    }

    audio = Audio.objects.filter(name=audio.name)
    j = 1
    for i in audio:
        print(i.audio_id)
        video_db = Video.objects.get(audio_id=i.audio_id)
        video = {
            'url': video_db.url,
            'id': video_db.video_id,
        }
        data[j] = video
        j+=1

    print(data)

    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_comments(request: Request):
    video_id = request.data.get('id')
    access_token = request.headers.get('Access-Token')
    user_id = get_user_id_from_payload(access_token)
    comment = request.data.get('comment')
    username = ProfileSettings.objects.get(id=user_id).username
    video = Video.objects.get(video_id=video_id)
    comment_instance = VideoComments(video_id=video, username=username, comment=comment)
    comment_instance.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def get_video_with_hashtags(request: Request):
    hashtag = request.data.get('hashtags')
    video_ids = HashtagsOnVideo.objects.filter(hashtag=hashtag)
    data = {}
    for i in range(video_ids.__len__()):

        video = {
            'url': Video.objects.get(video_id=video_ids[i].video_id.id.video_id).url,
            'id': Video.objects.get(video_id=video_ids[i].video_id.id.video_id).video_id
        }

        data[i] = video
    print(data)
    return Response(data, status=status.HTTP_200_OK)



@api_view(['POST'])
def get_comments(request: Request):
    video_id = request.data.get('id')
    video = Video.objects.get(video_id=video_id)
    data = {}
    comments = VideoComments.objects.filter(video_id=video)
    j = 0
    for i in comments:
        comment = {
            'username': i.username,
            'date_of_published': i.date_of_published,
            'likes': i.likes,
            'comments': i.comment,
            'id': i.id
        }
        data[j] = comment
        j += 1

    return Response(data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def like_comments(request: Request):
    comment_id = request.data.get('id')
    comment = VideoComments.objects.get(id=comment_id)
    comment.likes+=1
    comment.save()
    return Response(status=status.HTTP_200_OK)