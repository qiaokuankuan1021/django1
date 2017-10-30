from django.db import models

# Create your models here.
# 用户表
class Users(models.Model):
	username=models.CharField(max_length=32)
	name=models.CharField(max_length=16)
	password=models.CharField(max_length=32)
	sex=models.IntegerField()
	address=models.CharField(max_length=255)
	code=models.CharField(max_length=6)
	phone=models.CharField(max_length=16)
	email=models.CharField(max_length=50)
	state=models.IntegerField(default=1)
	addtime=models.IntegerField()
	def userslist(self):
		return {'id':self.id,'username':self.username,'name':self.name,'address':self.address,'code':self.code,'phone':self.phone}
	

#商品分类
class Type(models.Model):
	name=models.CharField(max_length=32)
	pid=models.IntegerField()
	path=models.CharField(max_length=255)
#商品信息表
class Goods(models.Model):
	typeid=models.IntegerField()
	goods=models.CharField(max_length=32)
	company=models.CharField(max_length=50)
	descr=models.TextField()
	price=models.DecimalField(max_digits=6, decimal_places=2)
	picname=models.CharField(max_length=255)
	state=models.IntegerField()
	store=models.IntegerField()
	num=models.IntegerField()
	clicknum=models.IntegerField()
	addtime=models.IntegerField()
	def goodslist(self):
		return {'id':self.id,'goods':self.goods,'price':self.price,'num':self.num,'picname':self.picname,'m':1}

#订单列表	
class Orders(models.Model):
	uid=models.IntegerField()
	linkman=models.CharField(max_length=32)
	address=models.CharField(max_length=255)
	code=models.CharField(max_length=6)
	phone=models.CharField(max_length=16)
	addtime=models.IntegerField()
	total=models.DecimalField(max_digits=8, decimal_places=2)
	status=models.IntegerField()

class Detail(models.Model):
	orderid=models.IntegerField()
	goodsid=models.IntegerField()
	name=models.CharField(max_length=32)
	price=models.DecimalField(max_digits=6, decimal_places=2)
	num=models.IntegerField()
	














