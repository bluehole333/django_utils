from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

# 1. 配置settings
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'conf.pagination.GlobalPageNumberPagination',
    'PAGE_SIZE': 10,
    'MAX_PAGE_SIZE': 50,
}


# 2. 添加继承自PageNumberPagination分页class

class GlobalPageNumberPagination(PageNumberPagination):
    # 这里会把settings.PAGE_SIZE、MAX_PAGE_SIZE替换掉，settings配置就无效了
    page_size = 2
    page_size_query_param = 'count'
    max_page_size = 50

    def get_paginated_response(self, data):
        # 自定义list返回数据类型
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('page', self.page.number),
            ('next', self.page.has_next()),
            ('previous', self.page.has_previous()),
            ('results', data)
        ]))
