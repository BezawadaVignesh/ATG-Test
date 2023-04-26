from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),
    path('register/doctor/', user_views.register_d, name='register-doctor'),
    path('register/patient/', user_views.register_p, name='register-patient'),
    path('', user_views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

