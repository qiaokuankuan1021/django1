
	// 返回顶部
	$('.fding').click(function(){
		$('body').animate({scrollTop:0+'px'},1500);
	})
		
//是否自动登录
//点击事件
	var bba=false;
	$('.quan').click(function(){
		if (bba==false){
			$(this).css({background:'url('+'/static/myweb/img/dl/5.png'+') 0px 2px'})
			bba=true;
		}else if(bba==true){
			$(this).css({background:'url('+'/static/myweb/img/dl/5.png'+') 0px -18px'})
			bba=false;
		}
		
	})

	//   提交
	var nameOk=false;
	var paddOk=false;
	//获取焦点事件
	$('input[name=username]').focus(function(){
		//添加颜色
		$('input[name=username]').css('border','1px solid #CCCCCC');
		$('input[name=password]').css('border','1px solid #CCCCCC');
	})
	$('input[name=password]').focus(function(){
		$('input[name=password]').css('border','1px solid #CCCCCC');
		$('input[name=username]').css('border','1px solid #CCCCCC');
	})
	丧失焦点事件
	$('input[name=username]').blur(function(){
		//获取用户信息进行正则获取
		var v =$(this).val();
		var reg=/^\w{2,18}$/;
		//判断如果为true则通过
		if(reg.test(v)){
			nameOk=true;
		}else{
			$(this).css('border','1px solid red');
			nameOk=false;
		}
	})
	// //丧失焦点事件
	$('input[name=password]').blur(function(){
		//获取用户信息
		var v =$(this).val();
		var reg=/^\w{6,18}$/;
		//判断如果为true则通过
		if(reg.test(v)){
			passOk=true;
		}else{
			$(this).css('border','1px solid red');
			passOk=false;
		}


	})

	//鼠标移入事件
	$('.anniu1 button').mouseover(function(){
		$('input').trigger('blur');
		//都正确去掉按钮的disabled
		if(nameOk && passOk==true){
			$('.anniu1 button').removeClass("disabled")
			return false;
		}
		//错误添加按钮的disabled
		 if(nameOk==false || passOk==false){
			$('.anniu1 button').addClass("disabled")
		}
	})


	//表单提交事件
	$('form').submit(function(){
		//触发input 丧失焦点事件
		$('input').trigger('blur');
		//判断如果都正确
		if(nameOk && passOk==true){
			return true;
		}
		//阻止默认行为
		return false;
	})

