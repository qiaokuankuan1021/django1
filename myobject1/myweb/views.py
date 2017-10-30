from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from myweb.models import Users,Type,Goods,Orders,Detail
import time,re
# Create your views here.
#公共信息加载
def loadContext(request):
	context ={}
	context['typeslist'] = Type.objects.filter(pid=0)
	return context
#首页
def index(request):
	print(request.path)
	if 'zaixian' not in request.session:
		request.session['zaixian']='False'
	context = loadContext(request)
	return render(request,'myweb/index.html',context)
#列表页
def list(request,id=0):
	context = loadContext(request)
	if id == 0:
		context['goodslist']=Goods.objects.all()
	else:
		context['types']=Type.objects.filter(pid=id)
		if request.GET.get('ttid',None):
			context['goodslist'] = Goods.objects.filter(typeid=request.GET['ttid'])
		else:
			context['goodslist'] = Goods.objects.filter(typeid__in=Type.objects.only('id').filter(path__contains=','+str(id)+','))
	return render(request,'myweb/list.html',context)

#详情页
def detail(request,id):
	context = loadContext(request)
	goods = Goods.objects.get(id = id)
	goods.clicknum+=1
	goods.save()
	context['goods']=goods
	return render(request,'myweb/detail.html',context)

#验证码
def verify(request):
	 #引入随机函数模块
	import random
	from PIL import Image, ImageDraw, ImageFont
	#定义变量，用于画面的背景色、宽、高
	#bgcolor = (random.randrange(20, 100), random.randrange(
	#    20, 100),100)
	bgcolor = (242,164,247)
	width = 100
	height = 45
	#创建画面对象
	im = Image.new('RGB', (width, height), bgcolor)
	#创建画笔对象
	draw = ImageDraw.Draw(im)
	#调用画笔的point()函数绘制噪点
	for i in range(0, 100):
		xy = (random.randrange(0, width), random.randrange(0, height))
		fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
		draw.point(xy, fill=fill)
	#定义验证码的备选值
	str1 = '1234567890'
	#随机选取4个值作为验证码
	rand_str = ''
	for i in range(0, 4):
		rand_str += str1[random.randrange(0, len(str1))]
	#构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
	font = ImageFont.truetype('static/STXIHEI.TTF', 21)
	#font = ImageFont.load_default().font
	#构造字体颜色
	fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
	fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
	fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
	fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
	#绘制4个字
	draw.text((5, 5), rand_str[0], font=font, fill=fontcolor1)
	draw.text((25, 5), rand_str[1], font=font, fill=fontcolor2)
	draw.text((50, 5), rand_str[2], font=font, fill=fontcolor3)
	draw.text((75, 5), rand_str[3], font=font, fill=fontcolor4)
	#释放画笔
	del draw
	#存入session，用于做进一步验证
	request.session['verifycode'] = rand_str
	"""
	python2的为
	# 内存文件操作
	import cStringIO
	buf = cStringIO.StringIO()
	"""
	# 内存文件操作-->此方法为python3的
	import io
	buf = io.BytesIO()
	#将图片保存在内存中，文件类型为png
	im.save(buf, 'png')
	#将内存中的图片数据返回给客户端，MIME类型为图片png
	return HttpResponse(buf.getvalue(), 'image/png')


#登录页
def login(request):
	return render(request,'myweb/login.html')

#执行登录
def dologin(request):
	verifycode = request.session['verifycode']
	code = request.POST['code']
	if code != verifycode:
		context = {'info':'验证码输入有瑕疵'}
		return render(request,'myweb/login.html',context)
	try:
		a=request.POST['username']
		user = Users.objects.get(username = a)
		if user.state == 1:
			import hashlib
			m=hashlib.md5()
			m.update(bytes(request.POST['password'],encoding="utf8"))
			if user.password == m.hexdigest():
				request.session['webuser']=user.userslist()
				request.session['zaixian']='True'
				return redirect(reverse('index'))
			else:
				context = {'info':'账号或密码错误'}
		else:
			context = {'info':'此用户不是会员用户'}
	except:
		context = {'info':'账号或密码错误'}
	return render(request,'myweb/login.html',context)
#会员退出
def logout(request):
	try:
		del request.session['webuser']
		request.session['zaixian']='False'
		return redirect(reverse('login'))
	except:
		return redirect(reverse('index'))
#会员添加
def useradd(request):
	return render(request,'myweb/add.html')
def userinsert(request):
	try:
		a=Users()
		a.username=request.POST["username"]
		a.name=request.POST['name']
		
		import hashlib
		m=hashlib.md5()
		m.update(bytes(request.POST['password'],encoding='utf8'))
		a.password=m.hexdigest()

		a.sex=request.POST['sex']
		a.address=request.POST['address']
		a.code=request.POST['code']
		a.phone=request.POST['phone']
		a.email=request.POST['email']
		a.state=1
		a.addtime=time.time()
		a.save()
		context = {'info':'添加成功请登录'}
		return render(request,'myweb/login.html',context)
	except:
		context={'info':'添加失败'}
		return render(request,'myweb/add.html',context)

#个人中心
def zhongxin(request):
	context = loadContext(request)
	uids = request.session['webuser']['id']
	# return HttpResponse(uids)
	#获取订单表中的订单
	orders = Orders.objects.filter(uid = uids)
	for i in orders:
		i.ptime = time.strftime('%y-%m-%d %H:%M:%S',(time.localtime(int(i.addtime))))
	# times = time.strftime('%y-%m-%d',(time.localtime(int(orders.addtime))))
	#获取orderid 在orders中的id
	details = Detail.objects.filter(orderid__in=Orders.objects.only('id').filter(uid=uids))
	for goods in details:
		goods.img = Goods.objects.get(id = goods.goodsid).picname
		goods.status = Orders.objects.get(id = goods.orderid).status
		goods.time = time.strftime('%Y-%m-%d %H:%M:%S',(time.localtime(int(Orders.objects.get(id = goods.orderid).addtime))))
	context['detail'] = details
	context['orders']=orders

	return render(request,'myweb/zhongxin.html',context)
#订单商品退货
def zhongxinordertui(request,sid):
	order = Orders.objects.get(id =sid )
	order.status = 3
	order.save()
	context = {'info':'退货成功'}
	return render(request,'myweb/info.html',context)

#订单待发货
def zhongxinweifa(request):
	context = loadContext(request)
	uids = request.session['webuser']['id']
	# return HttpResponse(uids)
	#获取订单表中的订单
	orders = Orders.objects.filter(uid = uids)
	# times = time.strftime('%y-%m-%d',(time.localtime(int(orders.addtime))))
	#获取orderid 在orders中的id
	details = Detail.objects.filter(orderid__in=Orders.objects.only('id').filter(uid=uids))
	for goods in details:
		goods.img = Goods.objects.get(id = goods.goodsid).picname
		goods.status = Orders.objects.get(id = goods.orderid).status
		goods.time = time.strftime('%Y-%m-%d %H:%M:%S',(time.localtime(int(Orders.objects.get(id = goods.orderid).addtime))))
	context['detail'] = details
	context['orders']=orders

	return render(request,'myweb/zhongxinweifa.html',context)
#订单以发货
def zhongxinyifa(request):
	context = loadContext(request)
	uids = request.session['webuser']['id']
	# return HttpResponse(uids)
	#获取订单表中的订单
	orders = Orders.objects.filter(uid = uids)
	# times = time.strftime('%y-%m-%d',(time.localtime(int(orders.addtime))))
	#获取orderid 在orders中的id
	details = Detail.objects.filter(orderid__in=Orders.objects.only('id').filter(uid=uids))
	for goods in details:
		goods.img = Goods.objects.get(id = goods.goodsid).picname
		goods.status = Orders.objects.get(id = goods.orderid).status
		goods.time = time.strftime('%Y-%m-%d %H:%M:%S',(time.localtime(int(Orders.objects.get(id = goods.orderid).addtime))))
	context['detail'] = details
	context['orders']=orders

	return render(request,'myweb/zhongxinyifa.html',context)
#订单以收货
def zhongxinshou(request):
	context = loadContext(request)
	uids = request.session['webuser']['id']
	# return HttpResponse(uids)
	#获取订单表中的订单
	orders = Orders.objects.filter(uid = uids)
	# times = time.strftime('%y-%m-%d',(time.localtime(int(orders.addtime))))
	#获取orderid 在orders中的id
	details = Detail.objects.filter(orderid__in=Orders.objects.only('id').filter(uid=uids))
	for goods in details:
		goods.img = Goods.objects.get(id = goods.goodsid).picname
		goods.status = Orders.objects.get(id = goods.orderid).status
		goods.time = time.strftime('%Y-%m-%d %H:%M:%S',(time.localtime(int(Orders.objects.get(id = goods.orderid).addtime))))
	context['detail'] = details
	context['orders']=orders

	return render(request,'myweb/zhongxinshou.html',context)

#订单收货
def zhongxinordershou(request,sid):
	order = Orders.objects.get(id =sid )
	order.status = 2
	order.save()
	context = {'info':'收货成功'}
	return render(request,'myweb/info.html',context)

#个人信息
def gerenxinxi(request):
	context = loadContext(request)
	uid = request.session['webuser']['id']
	users = Users.objects.get(id = uid)
	context['users']=users
	return render(request,'myweb/gerenxinxi.html',context)
#个人信息修改
def gerenedit(request,sid):
	context = loadContext(request)
	users = Users.objects.get(id =sid)
	context['users'] = users
	return render(request,'myweb/gerenedit.html',context)

def gerenupdate(request,sid):
	try:
		context = loadContext(request)
		users = Users.objects.get(id =sid)
		users.sex = request.POST['sex']
		users.code = request.POST['code']
		users.phone = request.POST['phone']
		users.email = request.POST['email']
		users.address = request.POST['address']
		users.save()
		context = {'info':'修改成功'}
	except:
		context = {'info':'修改失败'}
	return render(request,'myweb/info.html',context)

