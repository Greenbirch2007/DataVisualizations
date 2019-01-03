$(function () {
var flag = 1;
        $.ajax({
                url:"http://localhost:8088/TestImage5/org/transf.do",
                type:"post",
                data:{"flag":flag},        //提交服务器的数据
                dataType:"json",        //预期服务器返回的结果
                success:function(result){
                        if(result.status==0){//成功
                                var cities= result.data;
                                var x = new Array();         //x轴坐标
                                var datas = [];         //数据
                                for(var i=0; i<cities.length; i++){
                                        x[i] = cities[i].cityname;
                                        datas[i] = cities[i].percent;
                                }
                                $("#s1").text(x);
                                $("#s2").text(datas);

                                $('#container').highcharts({
                                chart: {
                                    type: 'column'
                                },
                                title: {
                                    text: '数据质量动态查询'
                                },
                                subtitle: {
                                    text: '子标题'
                                },
                                xAxis: {
                                    categories: x,   //这个可以
                                    crosshair: true
                                },
                                yAxis: {
                                    min: 0,
                                    max:100,
                                    title: {
                                        text: '合格率 (%)'
                                    }
                                },
                                tooltip: {

                                },
                                plotOptions: {
                                    column: {
                                        pointPadding: 0.2,
                                        borderWidth: 0
                                    }
                                },
                                series: [{
                                        name:'城市',
                                        //data: [90,80,70],
                                        data:[datas]   //这样引用数据行不通，求解决！！！
                                }]
                            });

                        }
                }
        });
});
</script>



//
//改为datas也不行，最后改成了
//data: eval( "["+datas+"]" );才行，但是我数据就是以JSON的形式传过来的，对前辈所说的数据的类型有什么要求吗？求解
//复制代码