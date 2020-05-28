from rest_framework import generics
from rest_framework import mixins
from django.db import transaction
from rest_framework import filters
from rest_framework.views import APIView
from django_redis import get_redis_connection
from django.utils.translation import gettext as _
from rest_framework import status, mixins, generics
from django.shortcuts import get_object_or_404, redirect
from rest_framework.exceptions import ParseError, PermissionDenied
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# 获取django default默认cache，获得redis或memcache缓存实例
redis_cli = get_redis_connection("default")


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
        # 可以直接返回400错误并附带键值的错误信息
        # raise ParseError({'name': "电话重复了"})
        # 可直接返回403权限错误
        # raise PermissionDenied("您没有权限")

        res = self.list(request, *args, **kwargs)

        return res

    def perform_create(self, serializer):
        # 重写save的逻辑 实现自定义变量save
        obj = serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        res = self.post(request, *args, **kwargs)

        return res


# Restfull 更新资源、删除资源
class XXXXXXAPIView(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = XXXXX.objects.all()
    serializer_class = XXXXXSerializer
    schema = XXXXX_SCHEMAS

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # 没有特殊逻辑需要制定obj 无需声明
    def get_object(self):
        obj = get_object_or_404(ClassName, pk=self.pk)

        return obj

    @transaction.atomic
    def put(self, request, pk, *args, **kwargs):
        self.pk = pk
        # partial 允许部分修改
        return self.update(request, *args, **kwargs, partial=True)

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """默认参数名为pk"""
        res = self.retrieve(request, *args, **kwargs)

        return res


# API View
class XXXXXXAPIView(APIView):
    serializer_class = XXXXXXXSerializer
    schema = XXXXXX_SCHEMA

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @transaction.atomic()
    def post(self, request, format=None):
        serializer = XXXXXXXXSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            return JsonResponse({}, status=status.HTTP_200_OK, safe=False)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
