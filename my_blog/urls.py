
from django.contrib import admin
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name ='registration/login.html')),
    url(r'', include('blog.urls')),
    # url(r'^accounts/logout/$', auth_views.LogoutView.as_view(template_name ='registration/login.html')),
    url('accounts/login/$', auth_views.LoginView.as_view(), name ='login'),
url('accounts/logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
