import datetime
import re

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from loginregist.models import TBook,TUser,TShopcar,TAddress,DOrderiterm,TOrder
from carapp.car import *
import random,string
# Create your views here.

# 购物车
def shopcar(request):
    car = request.session.get('car')
    name = request.session.get('login')
    email = request.COOKIES.get('username')
    # print(result)
    if name:
        result = TUser.objects.filter(user_email=name)[0]
        if car:
            for i in car.car_items:
                TShopcar.objects.create(book_name=i.book.book_name, user_id=result.user_id,counts=i.number)
            return render(request, 'car.html', {'car': car,'login': name,'username': email})
        return render(request,'car.html',{'login': name,'car':car})
    return render(request,'car.html',{'car':car})

# 结算
def count(request):
    login = request.session.get('login')
    # print(login)
    t_count = request.GET.get('t_count')
    request.session['t_count'] = t_count
    car = request.session.get('car')
    if login:
        return  redirect('carapp:indent')
    return HttpResponse('error')

# 订单
def indent(request):
    name = request.session.get('login')
    t_count = request.session.get('t_count')
    car = request.session.get('car')

    user = TUser.objects.filter(Q(user_email=name) | Q(user_name=name))[0]
    # 获取地址
    addr = TAddress.objects.filter(user_id=user.user_id)
    print(addr)
    if name:
        return render(request, 'indent.html',{'login':name,'t_count':t_count,'car':car,'addr':addr})
    return render(request,'indent.html',{'t_count':t_count,'car':car,'addr':addr})


def addr(request):
    id = request.GET.get('id')
    address = TAddress.objects.filter(id=int(id))[0]
    # print(address.detail_address,address.zipcode,address.telphone)
    return JsonResponse({"name": address.name, "add": address.detail_address, "zip": address.zipcode, "telephone": address.telphone,
                         "addr_mobile": address.addr_mobile})

def zipcode(request):
    return HttpResponse('ok')
def phonenum(request):
    return HttpResponse('ok')



# 订单成功
def indentOk(request):
    name = request.session.get('login')
    user = TUser.objects.filter(Q(user_email=name) | Q(user_name=name))[0]

    ordernum = random.sample(string.digits, 9)
    ordernum = ''.join(ordernum)

    addre = TAddress.objects.filter(user_id=user.user_id)[0]
    car = request.session.get('car')
    # print(type(car.total_price))
    ord = TOrder.objects.create(user_id=user.user_id,num=ordernum,create_date=datetime.datetime.now(),
                          price=car.total_price,order_addrid=addre.detail_address,status=1)
    for i in car.car_items:
        orditems = DOrderiterm.objects.create(shop_id=ord.user_id,book_id=i.book.book_id,
                                   shop_ordid=ord.num,shop_num=i.number,total_price=ord.price)
    del request.session['car']

    return render(request,'indent ok.html',{'ord':ord,'login':name})

def indentok2(request):
    name = request.session.get('login')
    user = TUser.objects.filter(Q(user_email=name) | Q(user_name=name))[0]
    ship_man = request.GET.get('ship_man')
    ship_add = request.GET.get('ship_add')
    ship_zipcode = request.GET.get('ship_zipcode')
    ship_tel = request.GET.get('ship_tel')
    ship_phone = request.GET.get('ship_phone')
    # print(ship_man,ship_add,ship_zipcode,ship_tel,ship_phone)
    result = TAddress.objects.filter(Q(detail_address=ship_add)&Q(user_id=user.user_id))
    if result:
        return HttpResponse('ok')
    else:
        TAddress.objects.create(name=ship_man, detail_address=ship_add, zipcode=ship_zipcode, telphone=ship_tel,
                            addr_mobile=ship_phone, user_id=user.user_id)
        address = TAddress.objects.filter(name=ship_man, detail_address=ship_add, zipcode=ship_zipcode, telphone=ship_tel,
                            addr_mobile=ship_phone)[0]
        request.session['addre'] = address
        return HttpResponse('ok')


# 添加购物车商品
def add_car(request):
    bookid = request.GET.get('id')
    # print(bookid)
    car = request.session.get('car',0)
    if not car:
        car = Car()
        car.add_car(bookid)
        request.session['car']=car
        return HttpResponse('ok')
    else:
        car.add_car(bookid)
        request.session['car']=car
        return HttpResponse('ok')

#修改购物车
def change_car(request):
    bookid = request.GET.get('id')
    number = request.GET.get('number',1)
    print(number)

    car = request.session.get('car')
    car.change_item(bookid,number)
    request.session['car']=car
    return JsonResponse({'tot':car.total_price,'savem':car.save_price})


# 删除购物车
def del_car(request):
    bookid = request.GET.get('id')
    car = request.session.get('car')
    car.del_item(bookid)
    request.session['car'] = car

    return JsonResponse({'tot': car.total_price, 'savem': car.save_price})


def num(request):
    bookid = request.GET.get('id')

    car = request.session.get('car')
    number=request.GET.get("number")
    re_num = re.compile(r'^[1-9][0-9]{0,4}$')
    ret=re_num.match(number)
    if ret:
        # tbook = TBook.objects.filter(book_id=bookid)[0]
        car.change_item(bookid,int(number))
        request.session['car'] = car
        return JsonResponse({'tot': car.total_price, 'savem': car.save_price})
    return HttpResponse('error')
