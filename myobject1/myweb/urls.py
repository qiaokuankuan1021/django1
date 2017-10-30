from django.conf.urls import url
from . import views,viewsorders
urlpatterns = [
	#网站前端商品展示
	url(r'^$',views.index,name="index"),#首页
	url(r'^list/(?P<id>[0-9]+)$',views.list,name="list"),#列表页
	url(r'^list$',views.list,name="list"),#列表页
	url(r'^detail/(?P<id>[0-9]+)$',views.detail,name="detail"),#详情页
	#会员及个人中心等路由配置
	url(r'^login$',views.login,name='login'),#登录页
	url(r'^dologin$',views.dologin,name='dologin'),#登录提交
	url(r'^logout$',views.logout,name='logout'),#登录退出
	url(r'^zhongxin$',views.zhongxin,name='zhongxin'),#个人中心订单浏览
	url(r'^zhongxinordertui/(?P<sid>[0-9]+)$',views.zhongxinordertui,name='zhongxinordertui'),#个人中心订单退货
	url(r'^zhongxinordershou/(?P<sid>[0-9]+)$',views.zhongxinordershou,name='zhongxinordershou'),#个人中心订单收货
	url(r'^zhongxinweifa$',views.zhongxinweifa,name='zhongxinweifa'),#个人中心订单未发货浏览
	url(r'^zhongxinyifa$',views.zhongxinyifa,name='zhongxinyifa'),#个人中心订单以发货浏览
	url(r'^zhongxinshou$',views.zhongxinshou,name='zhongxinshou'),#个人中心订单以收货浏览
	url(r'^gerenxinxi$',views.gerenxinxi,name='gerenxinxi'),#个人信息列表
	url(r'^gerenedit/(?P<sid>[0-9]+)$',views.gerenedit,name='gerenedit'),#个人信息修改
	url(r'^gerenupdate/(?P<sid>[0-9]+)$',views.gerenupdate,name='gerenupdate'),#个人信息修改
	#验证码
	url(r'^verify$',views.verify,name='verify'),
	#添加用户
	url(r'^useradd$',views.useradd,name='useradd'),
	url(r'^userinsert$',views.userinsert,name='userinsert'),
	
	#购物车及订单路由
	url(r'^shopcart$',viewsorders.shopcart,name='shopcart'),#浏览购物车
	url(r'^shopadd/(?P<sid>[0-9]+)$',viewsorders.shopadd,name='shopadd'),
	url(r'^shopdel/(?P<sid>[0-9]+)$',viewsorders.shopdel,name='shopdel'),
	url(r'^shopchange$',viewsorders.shopchange,name='shopcartchange'),
	url(r'^shopclear$',viewsorders.shopclear,name='shopclear'),

	#订单页
	url(r'^orderform$',viewsorders.orderform,name='orderform'),#浏览订单页
	url(r'^orderconfirm$',viewsorders.orderconfirm,name='orderconfirm'),#确认订单页
	url(r'^orderinsert$',viewsorders.orderinsert,name='orderinsert'),#订单添加


]