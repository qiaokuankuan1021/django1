import re
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
class WebMiddleware(object):
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		urllist=['/orderform','/orderconfirm','/orderinsert','/shopcart']
		path=request.path
		if path in urllist:
			if 'webuser' not in request.session:
				return redirect(reverse('login'))
		response =self.get_response(request)
		return response
