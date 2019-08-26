import re,hashlib

from django.db import transaction
from django.db.models import Q
from django.shortcuts import render,redirect,HttpResponse
from loginregist.models import DCategory,TBook,TUser

# Create your views here.
def login(request):
    state_car = request.GET.get('state')
    request.session['state_car'] = state_car
    # print(state_car)
    return render(request,'login.html',{'state_car':state_car})
def loginlogic(request):
    username = request.POST.get('txtUsername')
    password = request.POST.get('txtPassword')

    sha256 = hashlib.sha256()
    yan = username
    sha256.update(password.encode()+yan.encode())
    ox = sha256.hexdigest()
    #获取购物车状态
    state = request.session.get('state_car')

    # print(username, password)
    captcha = request.POST.get('txtVerifyCode')
    codes = request.session.get('codes')
    if captcha.lower() == codes.lower():
        user = TUser.objects.filter(Q(user_email=username)|Q(user_name=username), user_password=ox)
        if user:
            request.session['login']=username
            request.session['pwd']=password
            if state:
                return HttpResponse('ok1')
            return HttpResponse('ok')
        return HttpResponse('error')
    return HttpResponse('error')

def loginout(request):
    request.session.clear()
    return redirect('indexapp:index')


def regist(request):
    return render(request,'register.html')

def registlogic(request):
    username = request.POST.get('txt_username')
    password = request.POST.get('txt_password')
    captcha = request.POST.get('txt_vcode')
    codes = request.session.get('codes')

    m = hashlib.sha256()
    yan = username
    m.update(password.encode()+yan.encode())
    ox = m.hexdigest()
    print(ox)


    # print(username,password)
    try:
        with transaction.atomic():
            if captcha.lower() == codes.lower():
                TUser.objects.create(user_email=username,user_name=username,user_password=ox,user_status=1)
                res = HttpResponse('ok')
                res.set_cookie('username', username, max_age=7 * 24 * 3600)
                request.session['register'] = username
                return HttpResponse('ok')
            return HttpResponse('error')
    except:
        return HttpResponse('error')

def checkName(request):
    username = request.POST.get('txt_username')
    query = TUser.objects.filter(Q(user_email=username) | Q(user_name=username))
    if query:
        return HttpResponse('error1')
    else:
        re_email = re.compile(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$')
        re_phone = re.compile(r'^[1][3,4,5,7,8][0-9]{9}$')
        if re_email.match(username) or re_phone.match(username):
            return HttpResponse('ok')
        else:
            return HttpResponse('error2')
def checkPwd(request):
    password = request.POST.get('txt_password')
    # print(password)
    re_pwd1 = re.compile(r'^(?=.*?[a-z)(?=.*>[A-Z])(?=.*?[0-9])[a-zA_Z0-9]{0,6}$')
    re_pwd2 = re.compile(r'^(?=.*?[a-z)(?=.*>[A-Z])(?=.*?[0-9])[a-zA_Z0-9]{6,12}$')
    re_pwd3 = re.compile(r'^(?=.*?[a-z)(?=.*>[A-Z])(?=.*?[0-9])[a-zA_Z0-9]{12,}$')
    if re_pwd1.match(password):
        return HttpResponse('ok1')
    elif re_pwd2.match(password):
        return HttpResponse('ok2')
    elif re_pwd3.match(password):
        return HttpResponse('ok3')
    else:
        return HttpResponse('error')

# 验证码
def changeCode1(request):
    captcha = request.POST.get('txt_vcode')
    print(captcha)
    codes = request.session.get('codes')
    if captcha.lower() == codes.lower():
        return HttpResponse('ok')
    else:
        return HttpResponse('error')

def registOk(request):
    username = request.session.get('register')
    request.session['login'] = username
    login = request.session.get('login')

    # 获取订单状态
    state_car = request.session.get('state_car')
    print(state_car)
    if username:
        if state_car:
            return render(request, 'register ok.html', {"username": username, 'login': login, 'state_car': state_car})
        return render(request,'register ok.html',{"username":username,'login':login})
    else:
        return redirect('loginregist:regist')
def registOklogic(request):
    return HttpResponse('error')