$(document).ready(function(){
    var ParseApplicationID = "你的AppID";
    var ParseJavaScriptKey = "你的JS Key";
    //因为引入了Parse.com的库，所以使用全局变量Parse来初始化一个连接并且创建了一个叫做Test的集合
    Parse.initialize(ParseApplicationID,ParseJavaScriptKey);
    var Test = Parse.Object.extend("Test");
    var test = new Test();
    //向Test集合中保存两个字段和值
    test.save({
        name : "Zhe13",
        text : "hello"
    },{
        //save()函数和ajax（）一样接受回调参数success和error，我们将其显示在控制台中
        success : function(object){
            console.log("Parse.com object is saved:" + object);
        },
        error   : function(object){
            console.log("Error!Parse.com object is not saved:" + object);
        }
    });

})

getMessage();

 $("#send").click(function () {
     var username = $('input[name=username]').val();
     var message = $('input[name=message]').val();
     console.log(username);
     console.log('!');
     // 当提交消息时，ajax发送了一个post请求
     $.ajax(
         {
             url:"http:127.0",
             headers:{
                 'X-Parse-Application-Id' : ParseApplicationID,
                 'X-Parse-REST-API-Key'   : ParseRESTKey
             },
             contentType:'application/json',
             dataType:'json',
             processData:'false',
             data:JSON.stringify({
                 'username':username,
                 'message':message
             }),
             type:'POST',
             success :function () {
                 console.log('send');
                 getMessage();


             },
             error  : function () {
                 console.log('error');
             }

         }
     )


 })






//使用同样的ajax方法获取远程REST API的消息列表
function getMessage(){
    $.ajax({
        url : 'https://api.parse.com/1/classes/MessageBoard',
        headers:{
            'X-Parse-Application-Id' : ParseApplicationID,
            'X-Parse-REST-API-Key'   : ParseRESTKey
        },
        contentType : 'application/json',
        dataType    : 'json',
        type        : 'GET',
        //如果请求成功（返回200OK的消息）调用updateView
        success     : function(data){
            console.log('get');
            updateView(data);
        },
        error       : function(){
            console.log('error');
        }
    });
}
//显示得到的消息
function updateView(message){
    var table=$('.table tbody');//使用选择器选中元素并且创建一个引用
    table.html('');//清空这个元素的inner HTML
    //使用jQuery.each便利消息
    $.each(message.results,function (index,value){
        var trEl =
            $('<tr><td>'
                + value.username
                + '</td><td>'
                + value.message
                + '</td><td>'
                + value.objectId
                + '</td></tr>');
        //追加表格
        table.append(trEl);
    });
    console.log(message);
}