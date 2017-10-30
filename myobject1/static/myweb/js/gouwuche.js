

	$(document).ready(function(){
		var sum=0
		for (var i = 0; i < $('.xiaoji').length; i++) {
			a=$('.xiaoji').eq(i).text()
			var reg=/\d+/;
			var b=Number(reg.exec(a));
			sum+=b
		}

		// $('.zg h4 span').html(duigou);
		$('.zg h5 span').html($('input[name=m]').length);
		

	})

	// 加减
	//jia点击事件
	$('.jia').click(function(){
		// 获取class值
		var fzhi=$(this).attr('class');
		var reg=/f\d/;
		//找出是f几
		var newf=reg.exec(fzhi);
		//获取值并加1
		var shu=Number($(this).parent('.'+newf).find('.yi1').text());
		var newshu=shu+1;
		$(this).parent('.'+newf).find('.yi1').html(newshu);

		//获取当前价格
		var dqjinbi=$(this).parents('.zhanshi1').find('.xiaoji').text();
		var reg=/\d+/;
		var dqjb=Number(reg.exec(dqjinbi));
		//获取总和价格
		if(aa){
			var zgjinbi=$('.jine').find('h4 span').text();
			var regs=/\d+/;
			var zgjb= Number(regs.exec(zgjinbi));
			//算出新的总价格
			var newzong=dqjb+zgjb;
			
			$('.jine').find('h4 span').html(newzong);
			}
		//商品个数
		var gs=Number($('.zg h5 span').text());
		var newgeshu=gs+1;
		// 小计
		var xiao=$(this).parents('.zhanshi1').find('.xiaoji').text();
		var rega=/\d+/;
		var xiaojishu=Number(rega.exec(xiao));	
		var xinxiaoji=xiaojishu+dqjb;
		$(this).parents('.zhanshi1').find('.xiaoji').html(xinxiaoji);



	})	
	//jian点击事件
	$('.jian').click(function(){
		// 获取class值
		var fzhi=$(this).attr('class');
		var reg=/f\d/;
		//找出是f几
		var newf=reg.exec(fzhi);
		console.log(newf);
		//获取值并减1
		var shu=Number($(this).parent('.'+newf).find('.yi1').text());
		if (shu<=1) {shu=1};
		if(shu>1){var newshu=shu-1};
		$(this).parent('.'+newf).find('.yi1').html(newshu);
		if (shu>1) {
			//获取当前价格
		var dqjinbi=$(this).parents('.zhanshi1').find('.jiage').text();
		var reg=/\d+/;
		var dqjb=Number(reg.exec(dqjinbi));
		//获取总和价格
		if(aa){
			var zgjinbi=$('.jine').find('h4 span').text();
			var regs=/\d+/;
			var zgjb= Number(regs.exec(zgjinbi));
			console.log(dqjb);
			console.log(typeof(dqjb));
			//算出新的总价格
			if (shu>0) {
				var newzong=zgjb-dqjb;
			}
					$('.jine').find('h4 span').html(newzong);
			}
		//商品个数
		// var gs=Number($('.zg h5 span').text());
		// 	var newgeshu=gs-1;
		// //赋值给总个数
		// $('.zg h4 span').html(newgeshu);
		// $('.zg h5 span').html(newgeshu)
		// 小计
		var xiao=$(this).parents('.zhanshi1').find('.xiaoji').text();
		var rega=/\d+/;
		var xiaojishu=Number(rega.exec(xiao));
		console.log(xiaojishu);
		var xinxiaoji=xiaojishu-dqjb;
		$(this).parents('.zhanshi1').find('.xiaoji').html(xinxiaoji);


		}
		


	})

	//叉号删除
	// $('.caozuotu').click(function(){
	// 	//获取商品个数
	// 	var geshu=Number($(this).parents('.zhanshi1').find('.yi1').text());
	// 	//获取商品价格
	// 	var dqjinbi=$(this).parents('.zhanshi1').find('.jiage').text();
	// 	var reg=/\d+/;
	// 	var dqjb=Number(reg.exec(dqjinbi));
	// 	//获取总共价格
	// 	var zgjinbi=$('.jine').find('h4 span').text();
	// 	var regs=/\d+/;
	// 	var zgjb=Number(regs.exec(zgjinbi));
	// 	//求出新的价格
	// 	var newjinbi=zgjb-dqjb*geshu;
	// 	//赋值
	// 	$('.jine').find('h4 span').html(newjinbi+'.00');
	// 	//求出商品个数
	// 	var gs=Number($('.zg h5 span').text());
	// 	var newgs=gs-geshu;
	// 	$('.zg h4 span').html(newgs);
	// 	$('.zg h5 span').html(newgs);
	// 	$(this).parents('.zhanshi1').remove();
	// })



	// 返回顶部
	$('.fding').click(function(){
		$('body').animate({scrollTop:0+'px'},1500);
	})



	// 是否添加对勾
		// var duigou = 0;
		// sum=0;
		 aa=false;
		$('.quan').click(function(){
			var a =$(this).css('background-position-y');
			if (a=='-18px'){
				$(this).css({background:'url('+'/static/myweb/img/dl/5.png'+') 0px 2px '})
				aa=true;
				$(this).addClass('gou')
				// duigou++;
				// a=$(this).parents('.zhanshi1').find('.xiaoji').text()
				// var reg=/\d+/;
				// var b=Number(reg.exec(a));
				// sum+=b;
			}else if(a=='2px'){
				$(this).css({background:'url('+'/static/myweb/img/dl/5.png'+') 0px -18px '})
				// duigou--;
				$(this).removeClass('gou')
				// a=$(this).parents('.zhanshi1').find('.xiaoji').text()
				// var reg=/\d+/;
				// var b=Number(reg.exec(a));
				// sum-=b;
			}
			
			// $('.zg h4 span').html(duigou);
			// $('.jine').find('h4 span').text(sum);
			loadTotal()
		})
	//全选
	var cc=false;
	$('.quanx .quans').click(function(){
		if (cc==false) {
			$('.quan').css({background:'url('+'/static/myweb/img/dl/5.png'+') 0px 2px'})
			$('.fans').css({background:'url('+'/static/myweb/img/dl/5.png'+') 0px -18px'})
			cc=true;
			$('.quan').addClass('gou')
		}else if(cc==true){
			$('.quan').css({background:'url('+'/static/myweb/img/dl/5.png'+') 0px -18px'})
			cc=false;
			$('.quan').removeClass('gou')
		}
		loadTotal()
	})
	//反选
	 fanxuan=false;
	$('.fans').click(function(){
		if(fanxuan==false){
			for (var i = 0; i <($('.aa1').length); i++) {
				//获取每个按钮的y值
				var a =$('.aa1').eq(i).css('background-position-y');
				// alert(a)
				if (a=='-18px'){
					$('.aa1').eq(i).css({background:'url('+'/static/myweb/img/dl/5.png'+') 0px 2px '})
					
					$('.aa1').eq(i).addClass('gou')
				}else if(a=='2px'){
					$('.aa1').eq(i).css({background:'url('+'/static/myweb/img/dl/5.png'+') 0px -18px '})
				}
				$('.aa1').eq(i).removeClass('gou')
			}
			fanxuan=true;
		}else if(fanxuan==true){
			$('.fans').css({background:'url('+'/static/myweb/img/dl/5.png'+') 0px -18px'})
			for (var i = 0; i <($('.aa1').length); i++) {
				//获取每个按钮的y值
				var a =$('.aa1').eq(i).css('background-position-y')
				// alert(a)
				if (a=='-18px'){
					$('.aa1').eq(i).css({background:'url('+'/static/myweb/img/dl/5.png'+') 0px 2px '})
					$('.aa1').eq(i).addClass('gou')
				}else if(a=='2px'){
					$('.aa1').eq(i).css({background:'url('+'/static/myweb/img/dl/5.png'+') 0px -18px '})
					$('.aa1').eq(i).removeClass('gou')
				}
			}
			fanxuan=false;

		}
		loadTotal()
	})

function loadTotal(){
	var ids = [];
	var list = $('.aa1').filter('.gou')
	// alert(list)
	// alert(list.length);
	$('.zg h4 span').html(list.length);
	var total =0;
	for (var i = 0; i < list.length; i++) {
		total+=parseFloat($(list[i]).attr('price'));
		ids.push($(list[i]).attr('gid'));

	}
	$('.jine').find('h4 span').text(total);
	return ids;
}