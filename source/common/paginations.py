from rest_framework.pagination import PageNumberPagination


class ThirtyPagePagination(PageNumberPagination):
    page_size = 30
