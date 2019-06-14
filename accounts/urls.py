from django.conf.urls import url
from django.contrib import admin

from .views import register, login_view, logout_view

app_name='accounts'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^regter/$', register),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout')
]



# from django.conf.urls import url, include
# from .views import AccountHomeView, AccountEmailActivateView, UserDetailUpdateView, LoginView, RegisterView, GuestRegisterView, home_page, about_page, contact_page
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.auth.views import LogoutView
# from django.views.generic import TemplateView, RedirectView

# app_name='accounts'

# urlpatterns = [
#     url(r'^$', AccountHomeView.as_view(), name='home'),
#     url(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),
#     url(r'^$', home_page, name='home'),
#     url(r'^about/$', about_page, name='about'),
#     url(r'^accounts/login/$', RedirectView.as_view(url='/login')),
#     url(r'^accounts/$', RedirectView.as_view(url='/account')),
#     url(r'^account/', include("accounts.urls", namespace='account')),
#     url(r'^accounts/', include("accounts.passwords.urls")),
#     url(r'^login/$', LoginView.as_view(), name='login'),
#     url(r'^logout/$', LogoutView.as_view(), name='logout'),
#     url(r'^register/$', RegisterView.as_view(), name='register'),
#     url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
#     url(r'^settings/$', RedirectView.as_view(url='/account')),
    
# #     url('accounts/login/', login_view),
# #     url('accounts/register/', register_view),
# #     url('accounts/logout/', logout_view),
# #     path('login/', LoginView.as_view(), name='login'),
# #     # url('signup/', SignUp, name='signup'),
# #     url('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
# ]