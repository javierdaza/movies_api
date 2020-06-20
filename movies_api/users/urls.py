from django.urls import path

from movies_api.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

from movies_api.users.api.views import UserViewSet


user_list = UserViewSet.as_view({
    'get': 'list'
})

app_name = "users"
urlpatterns = [
    path('list/', view=user_list, name='list'),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
