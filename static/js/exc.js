
function rangeSlider1(value){
    document.getElementById('rangeValue1').innerHTML = value;
    document.getElementById('fillRangeValue1').style.width = +value+"%";
    console.log(value);
    value1=value
}


function rangeSlider2(value){
    document.getElementById('rangeValue2').innerHTML = value;
    document.getElementById('fillRangeValue2').style.width = +value+"%";
    console.log("море"+ value);
    value2=value
}


function rangeSlider3(value){
    document.getElementById('rangeValue3').innerHTML = value;
    document.getElementById('fillRangeValue3').style.width = +value+"%";
    console.log(value);
    value3=value
}


function rangeSlider4(value){
   
    document.getElementById('rangeValue4').innerHTML = value;
    document.getElementById('fillRangeValue4').style.width = +value+"%";
    console.log(value);
    value4=value
}
$(document).ready(function() {
    $("#generateBtn").click(function() {
        var value1 = parseInt($("#rangeValue1").text(), 10);
        var value2 = parseInt($("#rangeValue2").text(), 10);
        var value3 = parseInt($("#rangeValue3").text(), 10);
        var value4 = parseInt($("#rangeValue4").text(), 10);
        

        // Получаем CSRF-токен из мета-тега в вашем HTML-документе
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

        $.ajax({
            url: "/generate_excursion/",  // URL для отправки данных
            method: "POST",
            headers: { "X-CSRFToken": csrfToken },  // Передаем CSRF-токен в заголовках запроса
            data: {
                value1: value1,
                value2: value2,
                value3: value3,
                value4: value4
            },
            success: function(response) {
                // Перенаправляем пользователя на страницу с экскурсией
                window.location.href = response.excursion_url;
            },
            error: function(xhr, status, error) {
                console.error("Ошибка AJAX-запроса:", status, error);
            }
        });
    });
});