from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from myadmin.models import Orders,Detail,Goods
from PIL import Image
import time,re,os
# Create your views here.

#浏览订单信息
def order(request,pIndex):
	list = Orders.objects.filter()
	#实例化分页对象
	p = Paginator(list,10)
	# 处理当前页号信息
	if pIndex=="":
		pIndex = '1'
	pIndex = int(pIndex)
	# 获取当前页数据
	list2 = p.page(pIndex)
	plist = p.page_range
	return render(request,"myadmin/orders/order.html",{'orderslist':list2,'pIndex':pIndex,'plist':plist})
#修改订单状态
def orderedit(request,pid):
	orders = Orders.objects.get(id = pid)
	context = {'orders':orders}
	return render(request,'myadmin/orders/edit.html',context)
def orderupdate(request,pid):
	try:
		orders = Orders.objects.get(id = pid)
		orders.status = request.POST['status']
		orders.save()
		context = {'info':'修改成功'}
	except:
		context = {'info':'修改失败'}
	return render(request,'myadmin/info.html',context)

#订单详情
def detail(request,pid):
	list = Detail.objects.filter(orderid = pid)
	orders = Orders.objects.get(id =pid)
	for i in list:
		i.picname=Goods.objects.get(id =i.goodsid).picname
	
	times = time.strftime('%Y-%m-%d %H:%M:%S',(time.localtime(int(orders.addtime))))
	context = {'detailslsit':list,'orders':orders,'times':times}
	return render(request,"myadmin/orders/detail.html",context)

#订单提交
def detailform(request,pid):
	list = Orders.objects.get(id = pid)
	list.status='1'
	list.save()
	context = {'info':'发货成功'}
	return render(request,'myadmin/info.html',context)
#历史订单
def orderhistory(request,pIndex):
	list = Orders.objects.filter()
	#实例化分页对象
	p = Paginator(list,10)
	# 处理当前页号信息
	if pIndex=="":
		pIndex = '1'
	pIndex = int(pIndex)
	# 获取当前页数据
	list2 = p.page(pIndex)
	plist = p.page_range
	return render(request,"myadmin/orders/orderlishi.html",{'orderslist':list2,'pIndex':pIndex,'plist':plist})

