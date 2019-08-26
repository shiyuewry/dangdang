from carapp import views
from django.urls import path

app_name = 'carapp'
urlpatterns = [
    path('shopcar/',views.shopcar,name='shopcar'),
    path('indent/',views.indent,name='indent'),
    path('indentOk/',views.indentOk,name='indentOk'),

    # 添加商品
    path('add_car/',views.add_car,name='add_car'),
    # 修改商品
    path('change_car/',views.change_car,name='change_car'),
    # 删除商品
    path('del_car/',views.del_car,name='del_car'),

    # 结算
    path('count/',views.count,name='count'),

    # 收货信息
    path('addr/',views.addr,name='addr'),
    path('zipcode/',views.zipcode,name='zipcode'),
    path('phonenum/',views.phonenum,name='phonenum'),
    path('indentok2/',views.indentok2,name='indentok2'),

    path('num/',views.num,name='num'),
]

