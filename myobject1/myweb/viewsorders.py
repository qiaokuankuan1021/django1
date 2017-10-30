from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from myweb.models import Users,Type,Goods,Orders,Detail
import time,re
# Create your views here.
#购物车
#定义公共信息加载函数
def loadContext(request):
	context={}
	context['typeslist']=Type.objects.filter(pid=0)
	return context
#浏览购物车
def shopcart(request):
	context = loadContext(request)
	if 'shoplist' not in request.session:
		request.session['shoplist']={}
	return render(request,'myweb/shop.html',context)
#添加商品
def shopadd(request,sid):
	#获取要放入购物车中的商品信息
	goods = Goods.objects.get(id=sid)
	shop = goods.goodslist()
	shop['m']=int(request.POST['m'])
	if 'shoplist' in request.session:
		shoplist = request.session['shoplist']
	else:
		shoplist={}
	if sid in shoplist:
		shoplist[sid]['m']+=shop['m']
	else:
		shoplist[sid]=shop
	request.session['shoplist']=shoplist
	return redirect(reverse('shopcart'))
#删除商品
def shopdel(request,sid):
	print(sid)
	shoplist = request.session['shoplist']
	del shoplist[sid]
	request.session['shoplist']=shoplist
	return redirect(reverse('shopcart'))
#清空购物车
def shopclear(request):
	request.session['shoplist']={}
	return render(request,'myweb/shop.html')
#修改数量
def shopchange(request):
	context =loadContext(request)
	shoplist = request.session['shoplist']
	shopid = request.GET['gid']

	m =int(request.GET['m'])
	goods = Goods.objects.get(id = shopid)
	if m<goods.store:
		if m<1:
			m=1
		shoplist[shopid]['m']=m
		request.session['shoplist']=shoplist
		return render(request,'myweb/shop.html',context)
	else:
		context = {'info':'购买该商品数量以上限'}
		return redirect(reverse('shopcart'))

#订单页
def orderform(request):
	context = loadContext(request)
	#获取要结账的商品id信息
	ids=request.GET['gids']
	if ids == '':
		return HttpResponse('请选择您要结算的商品')
	gids = ids.split(',')
	shoplist = request.session['shoplist']
	#封装要结账的商品信息,计算累计的总价格
	orderlist = {}
	total = 0
	for i in gids:
		orderlist[i]=shoplist[i]
		total+=shoplist[i]['price']*shoplist[i]['m']#计算总金额
		request.session['orderlist']=orderlist
		request.session['total']=total
	return render(request,'myweb/orderform.html',context)
#订单确认页
def orderconfirm(request):
	return render(request,'myweb/orderconfirm.html')
#订单添加页
def orderinsert(request):
	#添加订单
	orders =Orders()
	orders.uid=request.session['webuser']['id']
	orders.linkman=request.POST['name']
	orders.address=request.POST['address']
	orders.code=request.POST['code']
	orders.phone=request.POST['phone']
	orders.addtime=time.time()
	orders.total=request.session['total']
	orders.status=0
	orders.save()
	#获取订单详情
	orderlist = request.session['orderlist']


	#获取购物车商品
	shoplist = request.session['shoplist']
	#遍历购物车信息放入到订单详情列表
	for shop in orderlist.values():
		detail = Detail()
		detail.orderid = orders.id
		detail.goodsid = shop['id']
		detail.name = shop['goods']
		detail.price = shop['price']
		detail.num = shop['m']
		detail.save()

		goods = Goods.objects.get(id = shop['id'])
		goods.store = int(goods.store)-int(shop['m'])
		goods.save()

		shoplist.pop(str(shop['id']))
	request.session['shoplist']=shoplist


	context = {'info':"下单成功: 您的订单号:"+str(orders.id)}
	return render(request,'myweb/info.html',context)