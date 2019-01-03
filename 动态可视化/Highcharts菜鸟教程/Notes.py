# # Highcharts 是一个用纯JavaScript编写的一个图表库。
# #
# # Highcharts 能够很简单便捷的在web网站或是web应用程序添加有交互性的图表
# #
# # Highcharts 免费提供给个人学习、个人网站和非商业用途使用。
#
# # highcharts的特性：兼容性，多设备，免费使用，轻量，配置简单，多态，多维，配置提示工具，
# # 时间轴，导出，输出，可变焦，外部数据，文字旋转
#
#
# # HighCharts 特性
# # 兼容性 - 支持所有主流浏览器和移动平台（android、iOS等）。
# # 多设备 - 支持多种设备，如手持设备 iPhone/iPad、平板等。
# # 免费使用 - 开源免费。
# # 轻量 - highcharts.js 内核库大小只有 35KB 左右。
# # 配置简单 - 使用 json 格式配置
# # 动态 - 可以在图表生成后修改。
# # 多维 - 支持多维图表
# # 配置提示工具 - 鼠标移动到图表的某一点上有提示信息。
# # 时间轴 - 可以精确到毫秒。
# # 导出 - 表格可导出为 PDF/ PNG/ JPG / SVG 格式
# # 输出 - 网页输出图表。
# # 可变焦 - 选中图表部分放大，近距离观察图表；
# # 外部数据 - 从服务器载入动态数据。
# # 文字旋转 - 支持在任意方向的标签旋转。
#
# # 支持的图表类型:1.曲线型2. 区域图 3. 饼图  4. 散点图 5. 气泡图 6. 动态图表 7. 组合图表
# #  8. 3d图 9. 测量图 10. 热点图  11. 树状图(Treemap)
#
# # Highcharts环境配置　　
# # 安装jquery
#
#
# # Query 安装可以使用以下两种方式：
# #
# # 1、访问 jquery.com 下载jQuery包。
# # 2、使用 Staticfile CDN 静态资源库的jQuery资源：
# #
# # http://cdn.staticfile.org/jquery/2.1.4/jquery.min.js
# # 3、使用百度静态资源库的jQuery资源：
# #
# # http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js
#
# # 使用下载的方式
# # 使用下载的方式，在 HTML 页面引入 jQuery 代码:
# #
# # <head>
# #    <script src="/jquery/jquery.min.js"></script>
# # </head>
# # 使用 CDN（推荐）
# # 使用 Staticfile CDN 静态资源库来加载jQuery库：
# #
# # <head>
# #    <script src="http://cdn.staticfile.org/jquery/2.1.4/jquery.min.js"></script>
# # </head>
#
# # 安装 Highcharts
# # Highcharts 安装可以使用以下两种方式：
# #
# # 1、访问 highcharts.com 下载 Highcharts 包。
# # 2、使用官方提供的 CDN 地址：http://code.highcharts.com/highcharts.js
# # 使用下载的方式（推荐）
# # 使用下载的方式，在 HTML 页面引入 Highcharts 代码:
# #
# # <head>
# #    <script src="/highcharts/highcharts.js"></script>
# # </head>
# # 使用 CDN
# # 使用官方提供的 CDN 地址：
# #
# # <head>
# #    <script src="http://code.highcharts.com/highcharts.js"></script>
# # </head>
#
#
# # highcharts配置语法
#
# #  第一步:创建html页面
#
# # 创建一个 HTML 页面，引入 jQuery 和 Highcharts 库：
#
# # 文件名：HighchartsTest.htm
#
# # 实例中id为container的div用于包含Highcharts绘制的图表
#
# #　２．第二部，创建配置文件
#
# # highcharts库使用json格式来配置
#
# #   $('#container').highcharts(json);
# # 这里json表示使用json数据格式和json格式的配置绘制图表,步骤如下
#
# #　　标题　　为图片配置标题
#
# var title = {
#     text:'月平均气温'
# };
#
# #  副标题　　为图表配置副标题
# var subtitle = {
#     text:"Source:runoob.com"
# };
#
# # x轴　　配置要在x轴显示的项
#
# var xAxis = {
#     categories:[
#         '1月',"2月","３月","４月","５月","６月","７月","８月","９月","１０月","１１月","１２月"
#     ]
#
# }
#
# # y轴　　配置要在ｙ轴显示的项
#
# var yAxis = {
#     title:{
#         text:'Temperatur (\xBOC)'
#     },
#     plotLines:[
#         {
#             value:0,
#             width:1,
#             color:'#808080'
#         }
#     ]
# };
#
#
# # 提示信息　　配置提示信息
#
# var tooltip = {
#    valueSuffix: '\xB0C'
# }
#
# 展示方式
# 配置图表向右对齐：
#
# var legend = {
#    layout: 'vertical',
#    align: 'right',
#    verticalAlign: 'middle',
#    borderWidth: 0
# };
#
#
# # 数据
# # 配置图表要展示的数据.每个系列是个数组,每一项图片中都会生成一条曲线
#
# var
#
# # 3.第三步,创建json数据  组合是由配置信息
# # var json = {};
#
# # json.title = title;
# # json.subtitle = subtitle;
# # json.xAxis = xAxis;
# # json.yAxis = yAxis;
# # json.tooltip = tooltip;
# # json.legend = legend;
# # json.series = series;
#
#
# #　４．第四步，　画图
#
# $('#container').highcharts(json);
#
#
# # 是否有一个先后，要先导入jquery，后导入highcharts
#
#
# # highcharts配置选项详情
#
# # 参数配置　
# chart:图表区选项　　设置图表区相关属性

#  color:颜色选项
# highcharts已经默认提供多种颜色方案,当要显示的图形多余颜色种类时,多出的
# 图形会自动从第一种颜色方案开始选取

# Title:标题选取

# Subtitle：副标题选项
# 副标题提供的属性选项与标题title大致相同，可参照上述标题选项，值得一提的是副标题的text选项默认为''，即空的，所以默认情况下副标题不显示。

# xAxis：X轴选项
# X轴选项用于设置图表X轴相关属性。


# yAxis：Y轴选项
# Y轴选项与上述xAxis选项基本一致，请参照上表中的参数设置，不再单独列出。


#　series:数据列选项

#　数据列选项用于设置图表中要展示的数据相关的属性

#　参数　　　　描述
#　data    显示在图表中的数据列，可以为数组或json格式的数据．如data:[0,5,3,5],
#　        或　　data:[{name:'Point 1',y:0},{name:'Point 2 ',y:5}]

# name  显示数据列的名称
#　type  数据列类型，支持area,areaspine,bar,column,line,pie,scatter or spine

# plotOptions:数据点选项

#　plotOptions用于设置图表中的数据点相关属性．plotOptions根据各种图表类型，其属性设置有
# 差异,现将常用选项列出来


# 参数  描述   默认值

#　enabled   是否在数据点上直接显示数据　　　　false
#　 allowPointSelect 是否允许使用鼠标选中数据点　　　false
#　formatter  回调函数，格式化数据显示内容　　　formatter: function() {return this.y;}

#　Tooltip:数据点提示框

#　Tooltip用于设置当鼠标滑向数据点时显示的提示框信息



#　Legend：图例选项
#legend用于设置图例相关属性。


#  Highcharts曲线图　　（8个）
#
# 基本曲线图表
# 带有数据标签图表
# 图表异步加载数据
# 时间序列，可缩放的图表
# X轴翻转曲线图
# 带标记曲线图
# 标示区曲线图
# 不规则时间间隔图表
# 对数 x 轴

#  示例中通过jquery.getJSON()方法从异步加载csv文件：
# 导入data.js文件
# 异步加载数据需要导入以下js文件

# <script src="http://code.highcharts.com/modules/data.js"></script>
# 时间序列,可缩放的图表

#  配置
#  图表
#  配置可缩放图表 chart.zoomType 指定了用户可以拖放的尺寸，用户可以通过拖动鼠标来放大，可能值是x，y或xy：
#
# plotOptions
# 使用 plotOptions 配置图表区域：
#
# 配置两个 Y 轴：


# plotOptions
# plotOptions用于设置图表中的数据点相关属性。



			#
			# Highcharts 曲线图
			#
			# Highcharts 区域图
			#
			# Highcharts 条形图
			#
			# Highcharts 柱形图
			#
			# Highcharts 饼图
			#
			# Highcharts 散点图
			#
			# Highcharts 气泡图
			#
			# Highcharts 动态图
			#
			# Highcharts 组合图
			#
			# Highcharts 3D图
			#
			# Highcharts 测量图
			#
			# Highcharts 树状图(Treemap)