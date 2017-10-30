// 返回顶部事件
$('.fding').click(function(){
	$('body').animate({scrollTop:0+'px'},1500);
})
//jia1点击事件

$('.jia1').click(function(){
	var a =$('.kucui').text();
	var c = Number($('input[name=m]').val());
	// alert(c);
	var reg = /\d+/;
	var b = Number(reg.exec(a));
	if(c < b){
	// if()
		var i=$("input[name=m]").val();
		i++;
		$("input[name=m]").val(i);
	}else{
		alert('没有货了,老铁')
	}
	// var xinjia=i*199.00;
	// $('.jieshao h4:eq(1)').html('¥'+xinjia+'.00');

})
//jian1点击事件
$('.jian1').click(function(){
	var i=$("input[name=m]").val();
	i--;
	if (i<=1) {i=1};
	$("input[name=m]").val(i);
	// var xinjia=i*199.00;
	// $('.jieshao h4:eq(1)').html('¥'+xinjia+'.00');
})


//放大镜 ----------------------
var newl=0;
var newt=0;
// 放大镜
// 绑定鼠标移动事件
$('.small').mousemove(function(e){
	// 显示大小图
	yi(e);

	// 设置大图移动--------------------------------------------
	
	//求左侧small的宽高
	var sw=$('.small').width();
	var sh=$('.small').height();
	//当前小div移动的距离 计算比例
	var bix=newl/sw;
	var biy=newt/sh;
	//右图未缩放的大图宽高
	var imgw=$('.bimg').width();
	var imgh=$('.bimg').height();
	var imgLeft=imgw*bix;
	var imgTop=imgh*biy;
	//设置右侧大图的移动
	$('.bimg').css({top:-imgTop+'px',left:-imgLeft+'px'});
	//大小图比例--------------------------------------------
	var biliw=$('.big').width()/$('.bimg').width();
	var bilih=$('.big').height()/$('bimg').height();
	//move大小
	var movew=$('.small').width()*biliw;
	var moveh=$('.small').height()*bilih;
	$('.move').css({width:movew+'px',height:moveh+'px'});
	
})

//绑定鼠标离开事件
$('.small').mouseout(function(){
// 显示小块和大图
$('.move').hide();
$('.big').hide();
})
// 封装函数 进行div移动设置
function yi(e){
	$('.move').show();
	$('.big').show();
	var x=e.clientX;
	var y=e.clientY;
	var sl=$('.small').position().left;
	var st=$('.small').position().top;
	//求出新的左偏移与上偏移
	newl=x-sl-$('.move').width()/2;
	newt=y-st-$('.move').height()/2;
	
	// 越界判断
	if (newt<=0) {newt=0};
	if (newl<=0) {newl=0};
	//最大的left与top
	var maxLeft=$('.small').width()-$('.move').width();
	var maxTop=$('.small').height()-$('.move').height();
	if(newt>=maxTop){newt=maxTop};
	if(newl>=maxLeft){newl=maxLeft};
	//设置新的左与高
	$('.move').css({top:newt+'px',left:newl+'px'});
}