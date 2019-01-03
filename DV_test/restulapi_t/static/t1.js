$.getJSON('https://data.jianshukeji.com/stock/history/000001', function (data) {
    if(data.code !== 1) {
        alert('读取股票数据失败！');
        return false;
    }
    data = data.data;
    // 去掉多余的数据
    Highcharts.each(data, function(d) {
        d.length = 2;
    });
    Highcharts.stockChart('container', {
        rangeSelector: {
            selected: 2
        },
        title: {
            text: '平安银行历史股价'
        },
        plotOptions: {
            series: {
                showInLegend: true
            }
        },
        tooltip: {
            split: false,
            shared: true
        },
        series: [{
            // type: 'line',
            id: '000001',
            name: '平安银行',
            data: data
        }]
    });
});
