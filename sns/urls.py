from django.urls import path
from . import views

app_name = 'sns'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:condition>/', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('category/<str:category_slug>/',
         views.CategoryPostView.as_view(), name='category_post'),
    path('category/<str:category_slug>/<int:condition>',
         views.CategoryPostView.as_view(), name='category_post'),
    path('create/', views.form_view, name='form_view'),
    path('my_page/', views.MyPage.as_view(), name='my_page'),
    path('my_page/<int:pk>/', views.MyPage.as_view(), name='my_page'),
    path('comment/<int:pk>/', views.CommentFormView.as_view(), name='comment_form'),
    path('reply/<int:pk>/', views.ReplyFormView.as_view(), name='reply_form'),
    path('good/<int:pk>/', views.good_func, name='good'),
]
