// Конструктор, формирующий поля класс по объекту JSON
function Car(obj) {
    this.number = obj.number;
    this.model = obj.model;
    this.route = obj.route;
    this.line = obj.line;
  
}

// Реализация класса 
Car.prototype = {
    constructor: Car,
    print: function(){
        console.log(this.to_string());
    },
    to_string: function() {
        return "number: " + this.number + ", number: " + this.number + ", number: " + this.number;
    },
    // Используемый ранее метод, возвращающий форматированные поля класса
    to_table_entry: function(i) {
        return '<tr><td>' + 
        this.number + ' <button type="button" onclick="deletetroll('+this.number+','+i+')"> del </button></td><td>' + 
        this.model + '</td><td>' +
        this.route + '</td><td>' + 
        this.line + '</td></tr>'
    }
}