

/**
 * Ajax 请求数据接口，并通过 Highcharts 提供的函数进行动态更新
 * 接口调用完毕后间隔 1 s 继续调用本函数，以达到实时请求数据，实时更新的效果
 */


$function(){
    $.ajax({
        url:'http://127.0.0.1:5000/data',
        success:function(response){
            if(response.status==0){
                var DT = response.data;
                var chart = Highcharts.chart('container',{
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
                        data:DT
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
                    }

                })

            }
        }
    })
}

// 用到了each，暂时没有参透！可以思考在common.js中设置一个间隔３秒钟的请求机制


