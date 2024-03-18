from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import UsersView, LoginView, TiketsView, TiketView

#Auth
urlpatterns = [
    path('auth-signup/', UsersView.as_view(), name='auth-signup'),
    path('auth-login/', LoginView.as_view(), name='auth-login'),
    path('token-refresh/', TokenRefreshView.as_view)
]

#Tiket
urlpatterns += [
    path('tikets/', TiketsView.as_view()),
    path('tiket/', TiketView.as_view())
]