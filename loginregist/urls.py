from loginregist import views
from django.urls import path

app_name = 'loginregist'
urlpatterns = [
#登录注册
    path('login/',views.login,name='login'),
    path('regist/',views.regist,name='regist'),
    path('registOk/',views.registOk,name='registOk'),
    path('loginlogic/',views.loginlogic,name='loginlogic'),
    path('registlogic/',views.registlogic,name='registlogic'),
    path('registOklogic/',views.registOklogic,name='registOklogic'),
#     登出
    path('loginout/',views.loginout,name='loginout'),
#     用户名
    path('checkName/',views.checkName,name='checkName'),
#     密码
    path('checkPwd/',views.checkPwd,name='checkPwd'),
#     注册验证码
    path('changeCode1/',views.changeCode1,name='changeCode1'),
]