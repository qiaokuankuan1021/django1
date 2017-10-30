from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from myadmin.models import Goods,Type
from PIL import Image
import time,re,os
# Create your views here.

#浏览商品分类
def shoptype(request):
	ob = Type.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
	for a in ob :
		a.pname=' . . . '*(a.path.count(',')-1)
	context = {'typelist':ob}
	return render(request,'myadmin/type/index.html',context)
#添加商品类别
def shoptypeadd(request,id):
	if id == '0':
		context = {'pid':0,'path':'0,','name':'根类别'}
	else:
		types = Type.objects.get(id = id)
		print(types)
		context = {'pid':types.id,'path':types.path+str(types.id)+',','name':types.name}
	return render(request,'myadmin/type/add.html',context)

def shoptypeinsert(request):
	try:
		types = Type()
		types.name=request.POST['name']
		types.pid=request.POST['pid']
		types.path=request.POST['path']
		types.save()
		context={'info':'添加成功'}
	except:
		context={'info':'添加失败'}
	return render(request,'myadmin/info.html',context)

#删除商品类别
def shoptypedel(request,id):
		row = Type.objects.filter(pid=id).count()
		goods = Goods.objects.filter(typeid=id).count()
		if row == 0 and goods == 0:
			types=Type.objects.get(id=id)
			types.delete()
			return redirect(reverse('myadmin_shoptype'))
		else:
			context = {'info':'该类型下还有子类别'}
		return render(request,'myadmin/info.html',context)
		
#别修改商品类
def shoptypeedit(request,id):
	types=Type.objects.get(id=id)
	a = types.pid
	type1 = Type.objects.get(id=a)
	context = {'type':types,'type1':type1}
	return render(request,'myadmin/type/edit.html',context)
def shoptypeupdate(request,id):
	try:
		b=Type.objects.get(id=id)
		b.name=request.POST['name']
		b.save()
		context={'info':'修改成功'}
	except:
		context={'info':'修改失败'}
	return render(request,'myadmin/info.html',context)




#浏览商品信息
def goodsindex(request,pIndex):
	list = Goods.objects.filter()
	#实例化分页对象
	p = Paginator(list,10)
	# 处理当前页号信息
	if pIndex=="":
		pIndex = '1'
	pIndex = int(pIndex)
	# 获取当前页数据
	list2 = p.page(pIndex)
	for i in list2:
		types = Type.objects.get(id=i.typeid)
		i.tname = types.name
	plist = p.page_range
	return render(request,"myadmin/goods/index.html",{'goodslist':list2,'pIndex':pIndex,'plist':plist})
def goodsadd(request):
	types = Type.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
	context = {'types':types}
	return render(request,'myadmin/goods/add.html',context)
def goodsinsert(request):
	try:
		myfile = request.FILES.get('pic',None)
		if not myfile:
			return HttpResponse('没有上传图片')
		filename = str(time.time())+'.'+myfile.name.split('.').pop()
		destination = open(os.path.join('./static/goods',filename),'wb+')
		for chunk in myfile.chunks():
			destination.write(chunk)
		destination.close()
		im = Image.open('./static/goods/'+filename)
		im.thumbnail((800,800))
		im.save('./static/goods/x_'+filename,'jpeg')
		im.thumbnail((412,412))
		im.save('./static/goods/'+filename,'jpeg')
		im.thumbnail((200,200))
		im.save('./static/goods/m_'+filename,'jpeg')
		im.thumbnail((100,100))
		im.save('./static/goods/s_'+filename,'jpeg')
		goods = Goods()
		goods.typeid =request.POST['typeid'] 
		goods.goods =request.POST['goods'] 
		goods.company =request.POST['company'] 
		goods.price =request.POST['price'] 
		goods.picname =filename
		goods.state =request.POST['state'] 
		goods.store =request.POST['store'] 
		goods.descr =request.POST['descr'] 
		goods.num =0
		goods.clicknum =0
		goods.addtime =time.time()
		goods.save()
		context = {'info':'添加成功'}
	except:
		context = {'info':'添加失败'}
	return render(request,'myadmin/info.html',context)

def goodsdel(request,id):
	try:
		goods = Goods.objects.get(id=id)
		os.remove('./static/goods/'+goods.picname)
		os.remove('./static/goods/m_'+goods.picname)
		os.remove('./static/goods/s_'+goods.picname)
		goods.delete()
		context = {'info':'删除成功'}
	except:
		context = {'info':'删除失败'}
	return render(request,'myadmin/info.html',context)

def goodsedit(request,id):
	types = Type.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
	goods = Goods.objects.get(id=id)
	context = {'goodslist':goods,'types':types}
	return render(request,'myadmin/goods/edit.html',context)
def goodsupdate(request,id):
	try:
		oldpicname = request.POST['oldpicname']
		if request.FILES.get('pic') != None:
			myfile = request.FILES.get('pic',None)
			if not myfile :
				return HttpResponse('没有上传图片')
			filename = str(time.time())+'.'+myfile.name.split('.').pop()
			destination = open(os.path.join('./static/goods/',filename),'wb+')
			for chunk in myfile.chunks():
				destination.write(chunk)
			destination.close()
			im = Image.open('./static/goods/'+filename)
			im.thumbnail((800,800))
			im.save('./static/goods/x_'+filename,'jpeg')
			im.thumbnail((412,412))
			im.save('./static/goods/'+filename,'jpeg')
			im.thumbnail((220,220))
			im.save('./static/goods/m_'+filename,'jpeg')
			im.thumbnail((100,100))
			im.save('./static/goods/s_'+filename,'jpeg')
			picname = filename
			os.remove('./static/goods/'+oldpicname)
			os.remove('./static/goods/m_'+oldpicname)
			os.remove('./static/goods/s_'+oldpicname)
		else:
			picname = oldpicname
		goods = Goods.objects.get(id=id)
		goods.typeid =request.POST['typeid'] 
		goods.goods =request.POST['goods'] 
		goods.company =request.POST['company'] 
		goods.price =request.POST['price'] 
		goods.picname =picname
		goods.state =request.POST['state'] 
		goods.store =request.POST['store'] 
		goods.num =request.POST['num'] 
		goods.addtime =time.time()
		goods.save()
		context = {'info':'修改成功'}
	except:
		context = {'info':'修改失败'}
	return render(request,'myadmin/info.html',context)
