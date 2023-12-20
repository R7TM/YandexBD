// Конструктор, формирующий поля класс по объекту JSON
function Route(obj) {
    this.route = obj.route; 
}

// Реализация класса 
Route.prototype = {
    constructor: Route,
    print: function(){
        console.log(this.to_string());
    },
    to_string: function() {
      //  return "number: " + this.number + ", number: " + this.number + ", number: " + this.number;
    },
    // Используемый ранее метод, возвращающий форматированные поля класса
    to_list_entry: function() {
	return '<option id="route'+this.route+'">'+this.route+'</option>'
    }
}