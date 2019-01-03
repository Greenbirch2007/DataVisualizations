// 初始化作图


// var chart = null; // 定义全局变量
//
//
// $(document).ready(function() {
//     chart = Highcharts.chart('container', {
//         chart: {
//             type: 'spline',
//             events: {
//                 load: requestData // 图表加载完毕后执行的回调函数
//             }
//         },
//         title: {
//             text: 'Live random data'
//         },
//         xAxis: {
//             type: 'datetime',
//             tickPixelInterval: 150,
//             maxZoom: 20 * 1000
//         },
//         yAxis: {
//             minPadding: 0.2,
//             maxPadding: 0.2,
//             title: {
//                 text: 'Value',
//                 margin: 80
//             }
//         },
//         series: [{
//             name: '随机数据',
//             data: []
//         }]
//     });
// });


// 调动数据接口并跟新图表　　是用jquery请求接口数据，保存成javacript对象之后塞进上面的作图函数中

/**
 * Ajax 请求数据接口，并通过 Highcharts 提供的函数进行动态更新
 * 接口调用完毕后间隔 1 s 继续调用本函数，以达到实时请求数据，实时更新的效果
 */
//　单独把异步请求写一个函数，便于扩展迁移
// eval 将字符串转换为数组，怎么保存？
// var json = {"id":"10086","data":[12,13,12.1,13.6,16,18],"email":"24werw@qq.com"}

// 用jquery请求，返回给谁？如果传给highcharts，它怎么接收？



// 详见锋利的jquery　ｐ186
//  jquery提供了一个通用的遍历方法$.each(),可以用于遍历对象和数组
//  $.each()函数不同于jquery对象的each()方法，它是一个全局函数，不操作jquery对象，而是以一个数组或对象作为第１个参数，以一个
//　回调函数作为第２个参数．回调函数拥有两个参数：
// 第１个为对象的成员或数组的索引，第２个为对应变量或内容
// function requestData() {
//     $.ajax({
//         url: 'http://127.0.0.1:5000/data',
//         type:'get',
//         // data:  提交服务器的数据　　这个部分可以用来写接口名
//         dataTye:"json",  // 预期服务器返回的结果
//         // 如果请求成功
//         success:function (result) {  // 爬虫返回的是一个json格式，怎么取数？
//             if(result.status==0){
//                 var a = result.d
//             }
//
//         }
//
//
//
//
//             // 一秒后继续调用本函数
//             setTimeout(requestData, 1000);
//         },
//         cache: false
//     });
// }





// 一般的请求数据
//
// // getJSON(url,作用的返回内容)
// $.getJSON('http://127.0.0.1:5000/data',function (cotent) {
//     data = content.data; //这里请求数据已经完成，要的是数组！
//     // 下面开始作图
//     Highcharts.chart('container',{
//         chart:{
//             type:'spilne',
//             // events:{
//             //    load: requestData // 图表加载完毕后执行的回调函数
//             // }
//         },
//         title :{
//             text:'第一个可视化测试应用'
//         },
//
//         },
//         series:[{
//             name:'第一个数据接口',
//             data:data
//         }]
//
//     });
//
// });.



var chart = Highcharts.chart('container', {
    title: {
        text: '可视化测试'
    },
    subtitle: {
        text: '数据来源：本地mysql'
    },
    yAxis: {
        title: {
            text: '收益率'
        }
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },
    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            }
            // pointStart: 2010
        }
    },
    series: [{
        name: '可视化测试',
        data: [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]  //　数据量太大这种方法就失效了！
    }],
    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
});