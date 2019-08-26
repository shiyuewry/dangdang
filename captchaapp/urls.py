from django.urls import path
from captchaapp import views

app_name='captcha'
urlpatterns = [
    path('getcaptcha/',views.getcaptcha,name='getcaptcha'),
]