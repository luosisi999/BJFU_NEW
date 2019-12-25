$(".btn_box").on("click",function(){
    $(".info_medicine_title").html("")
    $(".info_list").html("")
    inputValue=$(".input_box>input").val()
    if(!inputValue){
        alert("请输入内容")
        return
    }
    $.get("search", { searchKey: inputValue},
        function(result){
        result=JSON.parse(result);
        if(result.length == 0)
        {
            errorInfo = "查找失败"
            html="<li>"+ errorInfo +"</li>"
            $(".info_list").append(html)
            return
        }
		for (index in result)
		{
            ret = result[index]
            newTitle = ret["newTitle"]
            NewId = ret["NewId"]
            html = "<a href=" + NewId + ">" + newTitle + "</a><br> "
            $(".info_list").append(html)
        }
        });
})


