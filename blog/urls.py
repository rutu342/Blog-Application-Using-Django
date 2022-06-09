from django.urls import path
from . views import  HomeView,Article_DetailView,Addview,UpdatePostView,DeletePostView,CategoryView,Categorys,Like,CommentView
urlpatterns=[

    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',Article_DetailView.as_view(), name="detail"),
    path('addpost/',Addview.as_view(),name="add"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name="update"),
    path('article/<int:pk>/delete',DeletePostView.as_view(),name="delete"),
    path('addcategory/',CategoryView.as_view(),name="addcategory"),
    path('category/<str:cats>/',Categorys,name="category"),
    path('like/<int:pk>',Like,name="like_post"),
    path('article/<int:pk>/comment/',CommentView.as_view(),name="comment"),
    
    
]