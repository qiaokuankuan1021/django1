from django.conf.urls import url
from . import views,viewsgoods,viewsorders
urlpatterns = [
	#后台首页
    url(r'^$',views.index,name='myadmin_index'),
    
    #后台管理员路由
    url(r'^login$',views.login,name='myadmin_login'),
    url(r'^dologin$',views.dologin,name='myadmin_dologin'),
    url(r'^logout$',views.logout,name='myadmin_logout'),

    #验证码
    url(r'^verify$',views.verify,name='myadmin_verify'),

    #后台用户管理
    url(r'^users/(?P<pIndex>[0-9]+)$',views.usersindex,name='myadmin_usersindex'),
    url(r'^usersadd$',views.usersadd,name='myadmin_usersadd'),
    url(r'^usersinsert$',views.usersinsert,name='myadmin_usersinsert'),
    url(r'^usersdel/(?P<id>[0-9]+)$',views.usersdel,name='myadmin_usersdel'),
    url(r'^usersedit/(?P<id>[0-9]+)$',views.usersedit,name='myadmin_usersedit'),
    url(r'^usersupdate/(?P<id>[0-9]+)$',views.usersupdate,name='myadmin_usersupdate'),

    #商品分类
    url(r'^shoptype$',viewsgoods.shoptype,name="myadmin_shoptype"),
    url(r'^shoptypeadd/(?P<id>[0-9]+)$',viewsgoods.shoptypeadd,name="myadmin_shoptypeadd"),
    url(r'^shoptypeinsert$',viewsgoods.shoptypeinsert,name="myadmin_shoptypeinsert"),
    url(r'^shoptypedel/(?P<id>[0-9]+)$',viewsgoods.shoptypedel,name="myadmin_shoptypedel"),
    url(r'^shoptypeedit/(?P<id>[0-9]+)$',viewsgoods.shoptypeedit,name="myadmin_shoptypeedit"),
    url(r'^shoptypeupdate/(?P<id>[0-9]+)$',viewsgoods.shoptypeupdate,name="myadmin_shoptypeupdate"),

    #商品信息
    url(r'^good/(?P<pIndex>[0-9]+)$',viewsgoods.goodsindex,name="myadmin_goodsindex"),
    url(r'^goodsadd$',viewsgoods.goodsadd,name="myadmin_goodsadd"),
    url(r'^goodsinsert$',viewsgoods.goodsinsert,name="myadmin_goodsinsert"),
    url(r'^goodsdel/(?P<id>[0-9]+)$',viewsgoods.goodsdel,name="myadmin_goodsdel"),
    url(r'^goodsedit/(?P<id>[0-9]+)$',viewsgoods.goodsedit,name="myadmin_goodsedit"),
    url(r'^goodsupdate/(?P<id>[0-9]+)$',viewsgoods.goodsupdate,name="myadmin_goodsupdate"),
    

    #订单信息
    url(r'^order/(?P<pIndex>[0-9]+)$',viewsorders.order,name="myadmin_order" ),#订单表
    url(r'^orderedit/(?P<pid>[0-9]+)$',viewsorders.orderedit,name="myadmin_orderedit" ),#修改订单状态
    url(r'^orderupdate/(?P<pid>[0-9]+)$',viewsorders.orderupdate,name="myadmin_orderupdate" ),#提交修改订单状态
    url(r'^detail/(?P<pid>[0-9]+)$',viewsorders.detail,name="myadmin_detail" ),#订单详情表
    url(r'^detailform/(?P<pid>[0-9]+)$',viewsorders.detailform,name="myadmin_detailform" ),#订单详情表提交
    url(r'^orderhistory/(?P<pIndex>[0-9]+)$',viewsorders.orderhistory,name="myadmin_orderhistory" ),#历史订单表

]