from django.shortcuts import get_object_or_404, redirect
from rest_framework.exceptions import ParseError, PermissionDenied

from rest_framework import filters
from django.conf import settings
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from django.utils.translation import gettext as _
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Restfull 获取资源、创建资源
class XXXXXInfoListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = XXXXX.objects.all()
    serializer_class = XXXXXSerializer
    schema = XXXXXX_SCHEMAS

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        res = self.list(request, *args, **kwargs)

        return res


class XXXXXXAPIView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = XXXXX.objects.all()
    serializer_class = XXXXXSerializer
    schema = XXXXX_SCHEMAS

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        XXXXX = get_object_or_404(XXXX, pk=self.pk)

        return XXXXX

    def put(self, request, pk, *args, **kwargs):
        self.pk = pk
        self.original_obj = self.get_object()

        # partial 允许部分修改
        return self.update(request, *args, **kwargs, partial=True)
