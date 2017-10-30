from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from myadmin.models import Users,Type,Orders,Detail,Goods
import time,re
# Create your views here.
# 后台首页
def index(request):
	orders = Orders.objects.filter(status = '0')
	for a in orders:
		a.ptime= time.strftime('%Y-%m-%d %H:%M:%S',(time.localtime(int(a.addtime))))
	detail = Detail.objects.filter(orderid__in=Orders.objects.only(id).filter(status = '0'))
	for i in detail:
		i.picname = Goods.objects.get(id = i.goodsid).picname
		
	context = {'detailslsit':detail,'orderslist':orders}
	return render(request,'myadmin/index.html',context)

#后台管理员 

#会员登录表单
def login(request):
	return render(request,'myadmin/login.html')
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
	height = 25
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
	draw.text((5, 0), rand_str[0], font=font, fill=fontcolor1)
	draw.text((25, 0), rand_str[1], font=font, fill=fontcolor2)
	draw.text((50, 0), rand_str[2], font=font, fill=fontcolor3)
	draw.text((75, 0), rand_str[3], font=font, fill=fontcolor4)
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


#会员登录执行
def dologin(request):
	verifycode = request.session['verifycode']
	code = request.POST['code']
	if verifycode != code:
		context= {'info':'验证码错误'}
		return render(request,'myadmin/login.html',context)
	try:
		user=Users.objects.get(username=request.POST['username'])
		if user.state == 0:
			import hashlib
			m = hashlib.md5() 
			m.update(bytes(request.POST['password'],encoding="utf8"))
			if user.password == m.hexdigest():
				request.session['adminuser']=user.name
				return redirect(reverse('myadmin_index'))
			else:
				context = {'info':'登录密码错误'}
		else:
			context = {'info':'此用户非后台管理用户'}
	except:
		context = {'info':'账号或密码错误'}
	return render(request,'myadmin/login.html',context)

def logout(request):
	del request.session['adminuser']
	return redirect(reverse('myadmin_login'))

#后台会员管理
#浏览用户
def usersindex(request,pIndex):
    list = Users.objects.filter()
    #实例化分页对象
    p = Paginator(list,10)
    # 处理当前页号信息
    if pIndex=="":
        pIndex = '1'
    pIndex = int(pIndex)
    # 获取当前页数据
    list2 = p.page(pIndex)
    plist = p.page_range
    return render(request,"myadmin/users/index.html",{'userlist':list2,'pIndex':pIndex,'plist':plist})


def usersadd(request):
	return render(request,'myadmin/users/add.html')

#添加用户
def usersinsert(request):
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
		a.state=request.POST['state']
		a.addtime=time.time()
		a.save()
		context={'info':'添加成功'}
	except:
		context={'info':'添加失败'}
	return render(request,'myadmin/info.html',context)

#删除用户
def usersdel(request,id):
	b=Users.objects.get(id=id)
	b.delete()
	return HttpResponseRedirect(reverse('myadmin_usersindex',args=(1,)))
#修改用户
def usersedit(request,id):
	b=Users.objects.get(id=id)
	context = {'user':b}
	return render(request,'myadmin/users/edit.html',context)
def usersupdate(request,id):
	try:
		ob=Users.objects.get(id=id)
		ob.name=request.POST['name']
		ob.sex=request.POST['sex']
		ob.address=request.POST['address']
		ob.code=request.POST['code']
		ob.phone=request.POST['phone']
		ob.email=request.POST['email']
		ob.state=request.POST['state']
		ob.save()
		context= {'info':'修改成功'}
	except:
		context={'info':'修改失败'}
	return render(request,'myadmin/info.html',context)

