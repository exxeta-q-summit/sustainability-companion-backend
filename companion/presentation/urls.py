from django.urls import path, include

from companion.presentation.homepage import HomepageView, HomepageApi

urlpatterns = [
    path('', HomepageView.index, name='home'),
    path('api/', HomepageApi.index),                    #include('companion.presentation.urls_api'))
    # path('<int:page>/', HomepageView.index),
    #
    # path('post/<int:post_id>/', PostView.post, name='post'),
    # path('post/<int:post_id>/<int:page>/', PostView.post),
    # path('post/<int:post_id>/liked', LikeEndpoint.liked),
    # path('post/<int:post_id>/comment', CommentEndpoint.comment),
    # path('post/<int:post_id>/comment/<int:comment_id>/rm', CommentEndpoint.comment_delete),
    #
    # path('new/', HomepageView.index, name='new'),
    # path('create/', PostView.create_post, name='create'),
    #
    #
    # path('@<str:user_name>/', ProfileView.user_profile, name='user_profile'),
    # path('@<str:user_name>/<str:activity_type>/', ProfileView.user_profile, name='user_profile_type'),
]