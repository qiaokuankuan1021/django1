		// 手机移入事件
	 $('.shouji').mouseover(function(){
		$('.cftu').slideDown(600);
		return false;
		
	})
	 // 手机移除事件
	$('.shouji').mouseout(function(){
		$('.cftu').slideUp(600);
	})
	
	//热门商品的移入移出事件
	$('.nrkg').mouseover(function(){
		$(this).find('.anniu').css({display:'block'});
		$(this).find('.nbi').css({display:'none'});
	})
	$('.nrkg').mouseout(function(){
		$(this).find('.anniu').css({display:'none'});
		$(this).find('.nbi').css({display:'block'});
	})
	// 返回顶部
	$('.fding').click(function(){
		$('body').animate({scrollTop:0+'px'},1500);
	})

