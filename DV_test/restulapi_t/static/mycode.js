//
//    $(function(){
//
//    　　　//页面初始化过程
//                 //声明报表对象
//        var chart = new Highcharts.Chart({
//            chart: {
//                //将报表对象渲染到层上
//            renderTo: 'container'
//        },
//                //设定报表对象的初始数据
//        series: [{
//            data: [29.9, 71.5, 106.4, 129.2, 1404.0, 176.0, 135.6, 148.5]
//        }]
//    });
//
//　　　　　//　页面过去数据的过程
//
//　　　　　$jquery.ajax({
//    url: 'http://127.0.0.1:5000/data',
//    type: 'GET',     // 请求类型，常用的有 GET 和 POST
//    data: {
//        data// 请求参数
//    },
//    success: function(data) { // 接口调用成功回调函数
//        // data 为服务器返回的数据
//    }
//});
//
//        }
//
//        //刷新页面使用
//        $(document).ready(function() {
//            //每隔3秒自动调用方法，实现图表的实时更新
//            window.setInterval(getForm,3000);
//
//        });
//
//
//    });

//尝试自己写一个最简单的调用

var chart = null;

$.getJson('http://127.0.0.1:5000/data',function(data){
 chart = Highcharts.chart('container',{
 chart:{zoomType:'x'},

 series:[{
  type:'area',
     data:data
 }]

 });
});