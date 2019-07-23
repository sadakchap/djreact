from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='article')
urlpatterns = router.urls


# from django.urls import path
# from .views import (
#     ArticleListView, 
#     ArticleDetailView, 
#     ArticleCreateView,
#     ArticleUpdateView,
#     ArticleDeleteView
#  )


# urlpatterns = [
#     path('', ArticleListView.as_view()),
#     path('create/', ArticleCreateView.as_view()),
#     path('update/<int:pk>/', ArticleUpdateView.as_view()),
#     path('delete/<int:pk>/', ArticleDeleteView.as_view()),
#     path('<int:pk>/', ArticleDetailView.as_view()),
# ]