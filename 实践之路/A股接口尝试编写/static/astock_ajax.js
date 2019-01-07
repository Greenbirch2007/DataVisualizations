// 尝试写一个异步请求,应该是获取接口的数组数据之后,
//还需要再重新遍历一次
//遍历一个数组(请求一次,遍历一次,过了一道,这才好同步)
$(function () {
    $.ajax({
        url:"http://127.0.0.1:5000/astock",
        success:function (content) {
                       //请求成功
                 Nums = content.data;
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
                    data:eval( "["+Nums+"]" ),
                    //　数据量太大这种方法就失效了！
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




            };

        }
    })
})