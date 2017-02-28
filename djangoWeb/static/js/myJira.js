var opts = {
    lines: 13, // 花瓣数目
    length: 20, // 花瓣长度
    width: 10, // 花瓣宽度
    radius: 30, // 花瓣距中心半径
    corners: 1, // 花瓣圆滑度 (0-1)
    rotate: 0, // 花瓣旋转角度
    direction: 1, // 花瓣旋转方向 1: 顺时针, -1: 逆时针
    color: '#5882FA', // 花瓣颜色
    speed: 1, // 花瓣旋转速度
    trail: 60, // 花瓣旋转时的拖影(百分比)
    shadow: false, // 花瓣是否显示阴影
    hwaccel: false, //spinner 是否启用硬件加速及高速旋转
    className: 'spinner', // spinner css 样式名称
    zIndex: 2e9, // spinner的z轴 (默认是2000000000)
    top: 'auto', // spinner 相对父容器Top定位 单位 px
    left: 'auto'// spinner 相对父容器Left定位 单位 px
};
var spinner = new Spinner(opts);
var downloadId

var $window, availableWidth, availableHeight;
var calculateSize = function () {
    availableWidth = Math.max($window.width() - 100,200);
    availableHeight = Math.max($window.height() - 150, 100);
//  document.getElementById("hot").style.width=availableWidth + 50;
//  document.getElementById("hot").style.height=availableHeight + 50;
};

$(function() {
    $window = $(window);
    $window.on('resize', calculateSize);

    $("#btn-search").click(function() {
        var username = $('#input-username').val();
        var code = $('#input-code').val();
        var projectid = $('#input-id').val();
        var model = $('#input-model').val();
        var hot1;
		if(username == ""){
            alertify.alert('数据查询', "请输入JIRA账号");
        }else if(code == ""){
            alertify.alert('数据查询', "请输入JIRA密码");
        }else if(projectid == ""){
            alertify.alert('数据查询', "请输入项目编号");
        }else{
            downloadId = ""
            calculateSize();
            $.ajax({
                type:"POST",
                url:"/jira/search-data/",
                timeout:60000,
                data:{JIRAId: username, JIRACode: code, ProjectId: projectid ,Model: model},
                beforeSend: function() {
                	//异步请求时spinner出现
                    $("#hot").text("");
                    var target = $("#hot").get(0);
                    spinner.spin(target);

                },
                success: function(data,status) {
                    var resultData = $.parseJSON(data);
                    if(resultData.success == false){
                        alertify.alert("上传数据1", resultData.message);
                    }else{
                        //var t = JSON.stringify(resultData.data);
                        downloadId = resultData.downloadId
                    	hot1 = new Handsontable(document.getElementById('hot'),{
                            data: resultData.data,
                            readOnly: true,
                            renderAllRows: true,
//                            width: 404,
//                            height: 320,
                            manualColumnResize: true,
                            manualRowResize: true,
                            stretchH: 'all',
                            //manualColumnMove: true,
                            //manualRowMove: true,
                            rowHeaders: true,   //每一行会有一个id
                            colHeaders: ['项目', '问题类型', '标识', '主题', '经办人', '报告人',
                                '优先级', '状态', '解决结果', '创建', '更新', '模块', 'DI统计', '标签', '产品机型'],
                            columns: [
                                {data: '项目'},
                                {data: '问题类型'},
                                {data: '标识'},
                                {data: '主题'},
                                {data: '经办人'},
                                {data: '报告人'},
                                {data: '优先级'},
                                {data: '状态'},
                                {data: '解决结果'},
                                {data: '创建'},
                                {data: '更新'},
                                {data: '模块'},
                                {data: 'DI统计'},
                                {data: '标签'},
                                {data: '产品机型'},
                            ],
                            colWidths: [90, 80, 80, 200, 80, 80, 80, 80, 80, 90, 90, 80, 80, 80, 200],//每一列的宽度
                            //contextMenu: true,
                            width: function () { return availableWidth; },
                            height: function () { return availableHeight; },
                            stretchH: 'all'
                         });
                        $('#btn-export').attr("disabled",false);
                    }
                    //关闭spinner
                    spinner.spin();
                },
                error: function(data) {
                    alertify.alert("上传数据3", '请求发生错误...');
                    //关闭spinner
                    spinner.spin();
                }
            });
        }
    });

    $("#btn-export").click(function() {
//        var username = $('#input-username').val();
        location.href = "/jira/download/?downloadId=" + downloadId
        $('#btn-export').attr("disabled",true);
    });
});