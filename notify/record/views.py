from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import list_route, api_view
from datetime import date
from .serializers import PickUpSerializer
from .models import PickUp
import redis
import json
from django.conf import settings

# Create your views here.

r_cli = redis.StrictRedis()

class PickUpViewSet(ModelViewSet):
    queryset = PickUp.objects.all()
    serializer_class = PickUpSerializer

    def create(self, request, *args, **kwargs):
        class_id = request.data.get('class')
        request.data.update({'klass': class_id})
        # save to redis
        # import ipdb; ipdb.set_trace()
        # res = r_cli.sadd('center_{}_class_{}'.format(center_id, class_id), serializer.data)
        # return  super(PickUpViewSet, self).create(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @list_route(methods=['POST'])
    def batch_create(self, request):
        data = []
        for obj in request.data:
            class_id = obj.get('class')
            obj.update({'klass': class_id})
            data.append(obj)
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view()
def get_pickup(request, center_id, class_id):
    cache = r_cli.get(key_center_class_today(center_id, class_id))
    if cache:
        return Response(data=json.loads(cache))
    query = PickUp.objects.filter(date=date.today(), center=center_id, klass=class_id)
    # import ipdb; ipdb.set_trace()
    data = PickUpSerializer(query, many=True).data
    r_cli.set(key_center_class_today(center_id, class_id), json.dumps(data), ex=settings.ATTENDANCE_CACHE_EXPIRE)
    return Response(data)


@api_view(http_method_names=['DELETE'])
def del_student_today(request, student_id):
    today = date.today()
    queryset = PickUp.objects.filter(student=student_id, date=today)
    count = queryset.count()
    if count > 0:
        obj = queryset.first()
        queryset.delete()
        key = key_center_class_today(obj.center, obj.klass)
        r_cli.delete(key)
    return Response(data={}, status=status.HTTP_204_NO_CONTENT)


def key_center_class_today(center, class_id):
    return 'center_{}_class_{}_{}'.format(center, class_id, date.today())
