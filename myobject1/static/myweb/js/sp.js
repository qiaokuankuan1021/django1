
	//鼠标移入事件
		$('.kuang').mouseover(function(){
			$(this).find('.goumai').css({display:'block'});
			$(this).find('.nbia').css({display:'none'});
		})
	//鼠标移除时间
		$('.kuang').mouseout(function(){
			$(this).find('.goumai').css({display:'none'});
			$(this).find('.nbia').css({display:'block'});
		})
