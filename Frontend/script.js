var yandex_function_url = 'https://functions.yandexcloud.net/d4e36n5kqks4eglfptc0'
// Метод для конвертации формата python в воспринимаемую js строку
function preconvert_json(string) {
    let json = string.split('\'').join("\"");
    return json.split('b\"').join("\"");
}

// Метод, который будет заполнять таблицу пришедшими данными
function update_car_list(data) 
{

    $("#car_table td").parent().remove();
    let received_cars = JSON.parse(preconvert_json(data));
    if(received_cars.length > 0)
    {
        for(let i = 0; i < received_cars.length; ++i) {
            // Создаем объект класса для каждой пришедшей сущности
            let car = new Car(received_cars[i]);
            // Выполняем поиск элемента по ID, выбираем из него последний
            // элемент с тегом tr - table row
            $('#car_table tr:last').after(car.to_table_entry(i));
        }
        $("#car_table").show();
    } else {
        output_error("Incorrect data received")
    }
}


function update_route_list(data) 
{

    //$("#route_list option").parent().remove();
    let received_routes = JSON.parse(preconvert_json(data));
    if(received_routes.length > 0)
    {
        for(let i = 0; i < received_routes.length; ++i) {
            // Создаем объект класса для каждой пришедшей сущности
            let route = new Route(received_routes[i]);
            // Выполняем поиск элемента по ID, выбираем из него последний
            // элемент с тегом tr - table row
            $('#route_list').append(route.to_list_entry());
        }
        $("#route_list").show();
    } else {
        output_error("Incorrect data received")
    }
}

// Метод, который покажет сообщение об ошибке и скроет её через пару секунд 
function output_error(message, timeout = 60000) 
{
    $('.error_message').show();
    $('.error_message').text(message);
    setTimeout(function() {
        $('.error_message').hide();
    }, timeout);
}
