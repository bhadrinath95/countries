from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )
    
class PageNumberPagination(PageNumberPagination):
    page_size = 10
    
    