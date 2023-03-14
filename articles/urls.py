from django.urls import path
from .views import ArticlesList , ArticleDetailedView, ArticleUpdateView, ArticleDeleteView, CreateNewArticle



urlpatterns = [path('', ArticlesList.as_view(), name = 'articles_list'),
               path('<int:pk>/', ArticleDetailedView.as_view(), name='Article_detail'),
               path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='Article_edit'),
               path('<int:pk>/delete/', ArticleDeleteView.as_view(), name= 'Article_delete'),
               path('new/', CreateNewArticle.as_view(), name= 'Article_new'),


               ]