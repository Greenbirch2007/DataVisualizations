# #  开始学习使用Hightcharts
#
# # 获取Highcharts的几种方式 (3种)
# #
# # 直接引用我们提供的 CDN 服务，无需下载，高速稳定
# # 通过 官网下载页面 获取资源包，资源包包含所有相关文件的源代码及压缩版本，丰富的实例及使用说明文档，关于下载包的详细文件说明请参考 资源包下载及使用
# # 通过 Npm， Bower 等第三方包管理工具下载
#
# # 引入highcharts
#
#
# # Highcharts 最基本的运行只需要一个 JS 文件，即 highcharts.js，以使用 CDN 文件为例，对应的代码是：
#
# # <script src="http://cdn.hcharts.cn/highcharts/highcharts.js"></script>
#
# # 创建一个简单的图表
#
# #　在绘图前我们需要为highcharts准备一个dom容器，并指定其大小
#
# # <div id="container" style="width: 600px;height:400px;"></div>
#
# # 然后通过highcharts的初始化函数 Highcharts.chart来创建图表，该函数接受两个参数，第一个是
# # DOM容器的id，第二个参数是图片配置
#
# # 文件下载与使用
#
# # 一, 文件下载
#
# # 1. 资源包
# #　２．　在线CDN服务
# # 3. 在线实例
#
#
# #  二, 文件的使用
#
# # 1. 基础使用
# # 2. 功能模块
# #
# # 功能模块是在 Highcharts 主要功能的基础做的扩展，是由官方发布的功能包，常用功能模块有：
# #
# # 更多图表类型扩展模块（highcharts-more.js）
# # 3D 图表模块 （highcharts-3d.js）
# # 导出功能模块（modules/exporting.js）
# # 金字塔图表类型（modules/funnel.js）
# # 钻取功能模块（modules/drilldown.js）
# # 数据加载功能模块（modules/data.js）
#
# #  3. Highstock 和 Highmaps
#
# # 通过 npm 安装
#
# # 通过 Bower 安装
#
# # 如何设置图表配置选项
# #  highcharts是通过javascript对象的形式(json)来定义图表的配置参数
#
# #  一. 图表配置对象
# #  当使用图表构造函数highcharts.chart来初始化图表时,图表的配置对象是以第二个参数传递
# #  给该构造函数
# #javascript基础知识
#
# #  １．　对象的创建以及赋值
#
# var options = {
#     charts:{
#         renderTo:'container',
#         type:'line'
#     },
#     series:[
#         {
#             name:'小明',
#             data:[1,0,4]
#         }
#     ]
# }
#
# # 因为后面的方式更简单易读，这也是json的优势，创建配置对象后，我们就可以通过构造函数创建图表
#
# var chart = Highcharts.chart('container',options)
#
#
# #  2.对象取值
# #  在js中可以通过逗号或中括号的形式取对象的值，另外可以通过delete删除对象属性
#
#  options.chart.type  // js对象取值
#  options.chart['type']  ／／js对象取值
# delete options.chart.type  //删除属性
#
#
# #  ３．　数组相关操作
#
# # js数组的创建可以用 new Array()或更简单的[]来创建,其中length属性为数组的长度,push()函数
# #  可以添加数组元素;join()可以将数组转换成字符串,相应字符串可以通过的split()函数将其
# #  分隔成数组,
#
# var series = [{
#     name:'小明',
#     data:[]
# }];
#
# series.push({
#     name:'小红',
#     data:[]
# });
#
# series[2].name;
#
# var arr = [1,2,4,10,20]
# var arrJoin = arr.join() //  结果"1,2,4,10,20",默认的分隔符是,
# arrJoin.split(',');   //将字符串按照,分隔,结果是[1,2,4,10,20]
#
# # 二. 全局配置
#
# # 全局配置是针对同一个页面多个图表有效的配置,我们将多个图表的相同配置提取出来
# #　并配置在全局配置中(这样就可以省去在每个图表中配置一样的参数)
#
# # 图表主要组成
#
# # 一般情况下，Highcharts 包含标题（Title）、坐标轴（Axis）、
# # 数据列（Series）、数据提示框（Tooltip）、图例（Legend）、
# # 版权标签（Credits）等，另外还可以包括导出功能按钮（Exporting）
# # 、标示线（PlotLines）、标示区域（PlotBands）、数据标签（dataLabels）等。
#
# # Highcharts 基本组成部分如下图所示
#
# #
# # 1. 标题（Title）
# # 图表标题，包含标题和副标题（subTitle），其中副标题是非必须的。
# #
# # 2. 坐标轴（Axis）
# # 坐标轴包含x轴（xAxis）和y轴（yAxis）。通常情况下，x轴显示在图表的底部，y轴显示在图表的左侧。多个数据列可以共同使用同一个坐标轴，为了对比或区分数据，Highcharts提供了多轴的支持。
# #
# # 3. 数据列（Series）
# # 数据列即图表上一个或多个数据系列，比如曲线图中的一条曲线，柱状图中的一个柱形。
# #
# # 4. 数据提示框（Tooltip）
# # 当鼠标悬停在某点上时，以框的形式提示该点的数据，比如该点的值、数据单位等。数据提示框内提示的信息完全可以通过格式化函数动态指定。
# #
# # 5. 图例（Legend）
# # 图例是图表中用不同形状、颜色、文字等 标示不同数据列，通过点击标示可以显示或隐藏该数据列。
# #
# # 6. 版权标签（Credits）
# # 显示在图表右下方的包含链接的文字，默认是Highcharts官网地址。通过指定credits.enabled=false即可不显示该信息。
# #
# # 7. 导出功能（Exporting）
# # 通过引入 exporting.js即可增加图表导出为常见文件功能。
# #
# # 8. 标示线（PlotLines）
# # 可以在图表上增加一条标示线，比如平均值线，最高值线等。
# #
# # 9. 标示区（PlotBands）
# # 可以在图表添加不同颜色的区域带，标示出明显的范围区域。
#
#
# # 图表配置
#
# #  一，　图表容器
# #  highcharts实例化中绑定容器的方式有很多，这里列举三种
#
# #  １．　通过构造函数
#
# var charts = highcharts.chart('container',{
#     //highcharts配置
# });
#
# #  2.通过chart.renderTo来指定
#
# var charts = Highcharts.chart({
#     //highcharts配置
#     chart:{
#         renderTo:'container' // 或document.getElementById('container')
#     }
# });
#
# # 3. 如果你的页面已经引入jquery,那么可以以jquery插件的形式调用
#
# $('#container').highcharts({
#     //highcharts配置
# })
#
#
#
# # 二，图表样式
#
# #  １．　宽度，高度　
#
# # Highcharts 图表的高度和宽度是根据 DIV 容器的宽高来设定的，即
# #
# # <div id="container" style="width:400px;height:400px"></div>
# # 如果容器没有设定宽高，默认是 宽 400px， 高 400px，另外设置容器的 min-width 属性可以让 highcharts 自适应宽度，实例：
# #
# # <div id="container" style="min-width:400px;height:400px"></div>
# # 特别说明：饼图中可以通过设置宽高来让图形填充满整个容器
#
#
# # 2. 图表样式　
#
# # 图表样式属性包括 border、backgroundColor、margin、spacing、style等
# #
# # 边框：包括 borderColor、borderRadius、borderWidth
# # 背景：包括 backgroundColor
# # 外边距：包括 margin、marginTop、marginRight、marginBottom、marginLeft
# # 内边距：包括 spacing、spacingTop、spacingRight、spacingBottom、spacingLeft
# # 其他样式：其他属性例如字体等属性，实例代码
#
# #
# # 3、图表绘图区
# # 图表绘图区的可配置属性有：
# #
# # plotBackgroundColor ： 绘图区背景颜色
# # plotBackgroundImage ： 绘图区背景图片
# # plotBorderColor ： 绘图区边框颜色
# # plotBorderWidth ： 绘图区边框宽度
# # plotShadow ： 绘图投影
#
#
# # 三、事件
# # click ：图表点击事件，效果见 在线演示
# # load ：图表加载完后事件，效果见 在线演示
# # addSeries ：图表增加序列事件，效果见 在线演示
# # drilldown ：图表下钻事件，效果见 在线演示
# # drillup ： 图表上钻事件，效果见 在线演示
# # redraw ：图表重绘事件，效果见 在线演示
# # selection ： 图表范围选择事件，效果见 在线演示
# # beforePrint ： 图表打印前事件，效果见 在线演示
# # afterPrint ： 图表打印后事件,效果见 在线演示
#
# 四、其他配置
# 1、图表类型
# 通过 chart.type 来指定图表类型，表示如果默认图表类型，即如果 series 中没有指定 type， 那么图表的类型就由该属性来确定。highcharts 支持的所有图表类型见 plotOptions。
#
# 2、图表缩放
# 图表缩放包括缩放（zoom）和平移（pan），对应的属性有：
#
# zoomType ： 缩放类型，值可以是 “x”、“y”、“xy”，分别表示水平缩放、竖直缩放、平面缩放
# 缩放恢复按钮：可以指定按钮的样式、位置等，见 resetZoomButton，按钮的文字可以通过 lang 中的属性来指定
# selectionMarkerFill ：选中背景色，详细参考 API 文档
# panKey：平移键，默认是 “Shift”，即在启用平移后，按住指定的按键即可对图表进行平移操作，在线试一试
# panning ： 是否启用平移，启用平移后，按住平移键，然后就可以用鼠标对图表进行平移操作（即平移操作是平移键加鼠标拖动）
# 3、3D 属性
# Highcharts 4.0 开始支持 3D 图表类型，目前支持 3D 柱形图、3D 饼图、3D 散点图。
# 3D 相关属性见：chart.options3d ，关于 3D 图形的详细教程将以单独文章形式给出。
#
# 4、其他
# 图表反转 ： 图表反转指的是将图表的 x轴和 y轴进行对调操作，对应的只需要设置 chart.inverted = true 即可。
# 图表动画 ：chart.animation 可以设置图表的全局动画效果，这里的动画指的是图表更新时的动画效果，而图表初始化的动画是在 plotOptions.series.animation 中启用和关闭的。
# 图表自适应 ：前面说过通过设置图表容器的 min-width 可以让图表自适应，这个开关对应的属性是 chart.reflow，另外，还可以通过 API 接口 Chart.reflow 在外部对图表进行自适应操作，在线试一试


# 数据列
#　数据列配置是highcharts最复杂也是最灵活的配置，数据列配置是核心


#  一，什么是数据列

#  数据列是一组数据集合，例如一条线，一组柱形．如表中所有点的数据都来自数据列对象
#  数据列的基本构造如下

series :[
    {
        name:'',
        data:[]
    }
]

# 提示：数据列配置是个数组，也就是数据配置可以包含多个数据列
#  数据列中的name代表数据列的名字，并且会显示在数据提示框(Tooltip)以及图例(legend)中

#  二,数据列中的数据

#  在数据列的data属性中,我们可以定义图表的数据数组,通常有三种方式:

#  1. 数值数组.在这种情况下,配置数组中的数值代表y值,x值根据x的配置,要自动计算,要么
#  从0起开始自增,或根据pointStart及pointInterval自增;在分类轴中,x值就是categoies配置
#  数值数组配置如下

data:[1,2,4,6]

# 2. 包含两个值的数组集合.在这种情况下,集合中数组的第一个值代表x,第二个值代表y;
#  如果第一个值是字符串,则代表该点的名字,并且x值会如 1所说的情况决定,数组集合的实例

data:[[5,2],[6,3],[8,3]]

# 3. 数据点对象集合.在这种情况下,集合中元素都是数据点对象,对象中可以配置数据点plotOptions.series或
#  plotOptions.{图表类型}所列.


data :[
    {
        name:'point 1',
        color:'#00ff00',
        y:0
    },{
        name:'point 2 ',
        color:'#ff00ff',
        y:5
    }
]

# 三.数据点以及标记

# 在直角坐标图（即常规的包含X、Y轴的图表）中，数据点相当于图表中的一个 （x,y）点。
# 数据点的配置可以在数据列中是数据数组里指定。对于其他类型的图表（非直角坐标图），
# 数据点不仅仅表示 X，Y值，例如在范围图中，数据点包含 x，low， high值；
# 在 OHLC （蜡烛柱状图）中，数据点包含 x，open ， high， low， close；
# 在饼图或仪表图中，数据点只表示一个值。

# 数据点配置适用所有图表，下面的例子说明了如何指定某个点的颜色：


series:[{
    data:[29.9,71.5,160.4,
          {
              y:200,
              color:'#bfas11'
          }, 194.1,20
          ]
}]

# 四,数据列配置


#1、动画（Animation）
# 2、颜色（Color）
# 3、点的选择（Selection）
# 4、线条宽度（lineWidth）

series: [{
  data: [216.4, 194.1, 95.6],
  lineWidth: 5
}]

# 5、鼠标形状（cursor）

# 6、数据标签（dataLables）
# 7、线条样式（Dash Style）
# 8、数据列分区（zones）
# 标示线 (成本线)
#　标示带

# 数据处理概述

#　在highcharts的配置代码中，只需要按照规定的格式通过series.data配置给定塑化剂即可
#　另外，还可以使用Point.update, Series.setDate,  Series.update;

#　在实际使用过程中，对于数据的来源，数据怎么处理，怎么交互分析如下

#　１．　数据来源
#　highcharts是基于javascript编写的图表库，自身没有直接获取服务器(数据库)数据的能力，
#　除了内置的数据功能支持直接读取csv,html表格，，等数据外，数据来源还需要后端服务支持
#　（动态渲染或提供接口等），另外js还可以直接读取纯文本数据文件

#　总的来说，数据来源有以下方式：　（４个来源）
# 1. 服务器端直接渲染(包括直接渲染html页面，html表格)
# ２．ajax请求数据接口(来自服务器数据库的数据或其他数据)
# 3. highcharts内置的数据功能模块读取csv,html表格，gooleSpreadsheets数据
# ４．　javascript读取纯文本数据文件，例如，xml文件，json文件，csv文件


# 　２．　数据处理和交互

#　支持数据的处理，一般是用javascript针对返回的json数据，字符串数据进行数组，对象的操作，
# 最终转换成highcharts需要的格式，这个过程设计javascript对象，数组，json等基础是指

# 数据交互指的是动态的更新图表中的数据，一般是在获取并处理数据后调用highcharts相关的
# api接口进行图表动态更新，这在对交互性比较高的图表中会员，比如实时更新的图表，股票图

#  服务端动态渲染图表
# 服务端动态渲染网页是生成网页的最常用方法，该方法同样适用于动态生成包含highcharts图表的网页
# 服务器动态渲染网页的做法：后端程序读取数据库数据并按照一定的业务逻辑处理成字符串，
# 在页面对应位置输出

#　在php中可以用json_encode来将对象转换成字符串

# 动态渲染的优缺点

# 用动态渲染的方法生成 Highcharts 的优点是可以灵活的生成复杂的图表配置，缺点是无法灵活的进行数据交互。


# ajax请求数据接口
# ajax是一种不需要刷新页面就可以与服务器交换数据的方法
# 一,jquery中ajax相关的函数

# 在jquery中,有三种ajax相关的方法,分别是:ajax,get,post

# 1. jquery.ajax
# 统一的发送ajax请求函数,示例如下

$.ajax(
    {
        url:'请求地址',
        type:'get',  // 请求类型,常用的有get和post
    data:{
        // 请求参数
    },
    success:function(data){
     // 接口调用成功回调函数
    // data 为服务器返回的数据
}
    }
)


#　２．jquery.get
# 发送get请求，是ajax方法的简写

$.get(url,{
    // 参数

}, function(data) {
    //  data为服务器返回的数据
}


)


# 3. jquery.post

# 发送post方法,是ajax方法的加些

# $.post(url, {
#     // 参数
# }, function(data) {
#     // data 为服务器返回的数据
# });


# 二, 实例说明请求数据并创建图表

#　下面我们用具体的实例来说明这个过程


# 1. 创建服务器接口
# 2. 初始化图表
# 3. 调用数据接口并更新图表

# ajax请求数据接口，并通过highcharts提供的函数进行动态更新
#  接口调用完毕间隔1s继续调用本函数,以达到实时请求数据,实时更新的效果

#三，注意事项

# 1. 数据类型
# 注意请确保数据接口返回的数据是json对象的形式，如果返回的数据是json字符串，
#　我们可以用js转换易用性

# 在js中，用typeof来判断类型，字符串类型为"string",对象类型为"object";
# 我们可以用JSON.parse()来将JSON字符串转换换成json对象，用JSON.stringify()
# 来将json对象转换成json字符串

# ３．跨域问题
# 　处理文本或文本数据文件

# 在js中，可以通过发送请求的形式加载数据文件或数据接口，并按照一定的格式解析处理js
# 的格式解释处理js对象并最终创建图表

#  一，用csv数据创建图表

#  １．　csv数据
#  ２．　定义如表配置对象
#  ３．解析 csv数据
#  我们可以通过jquery.get方法来获取csv文件里的数据，并在请求成功回调函数
#  里进行数据解析；
#  注意不要在jquery.get回调函数之前创建图表，因为该函数是异步的，只有在请求返回
#  数据之后才会执行回调函数．

#  三，处理json数据

#  由于highcharts的配置本身就是json，所以json数据无需解析，只需啊哟转换成
#  需要的格式即可

#  １．　json文件内容
#  ２．　读取json并创建图表

#  数据功能模块
# 一、数据功能模块概述
# 二、 加载 CSV 数据
# 二、加载 HTML 表格数据
# 三、加载 Google SpreadSheets
#　图表导出模块概述
# 导出 Excel 数据文件 