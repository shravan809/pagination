from rest_framework.pagination import *

class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'
    page_size_query_param = 'records'
    max_page_size = 7
     

# class MyLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 5
#     limit_query_param = 'mylimit'
#     offset_query_param = 'myoffset'
#     max_limit = 6


# class MyCursorPagination(CursorPagination):
#  page_size = 5
#  ordering = 'product_name'
#  cursor_query_param = 'cu'