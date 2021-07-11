var breakfastMenu;
(function (breakfastMenu) {
    breakfastMenu[breakfastMenu["Cereal"] = 2.99] = "Cereal";
    breakfastMenu[breakfastMenu["Toast"] = 1.5] = "Toast";
})(breakfastMenu || (breakfastMenu = {}));
var lunchMenu;
(function (lunchMenu) {
    lunchMenu[lunchMenu["Tuna"] = 5.99] = "Tuna";
    lunchMenu[lunchMenu["Ham"] = 4.99] = "Ham";
})(lunchMenu || (lunchMenu = {}));
var dinnerMenu;
(function (dinnerMenu) {
    dinnerMenu[dinnerMenu["Beef"] = 8.99] = "Beef";
    dinnerMenu[dinnerMenu["Steak"] = 9.99] = "Steak";
})(dinnerMenu || (dinnerMenu = {}));
var dessertMenu;
(function (dessertMenu) {
    dessertMenu[dessertMenu["Cake"] = 7.99] = "Cake";
    dessertMenu[dessertMenu["IceCream"] = 5.99] = "IceCream";
})(dessertMenu || (dessertMenu = {}));
var Restaurant = /** @class */ (function () {
    function Restaurant(breakfast, lunch, dinner, dessert) {
        this.breakfast = breakfast;
        this.lunch = lunch;
        this.dinner = dinner;
        this.dessert = dessert;
    }
    Restaurant.prototype.printOrder = function () {
        var breakfastItem = breakfastMenu[this.breakfast];
        var lunchItem = lunchMenu[this.lunch];
        var dinnerItem = dinnerMenu[this.dinner];
        var dessertItem = dessertMenu[this.dessert];
        console.log("Order = " + breakfastItem + ", " + lunchItem + ", " + dinnerItem + ", " + dessertItem);
    };
    ;
    Restaurant.prototype.breakfastBill = function () {
        var prices = [];
        prices.push(this.breakfast, this.lunch, this.dinner, this.dessert);
        var sum = prices.reduce(function (a, b) { return a + b; }, 0);
        console.log("Total = \u00A3" + sum);
    };
    return Restaurant;
}());
var customer1 = new Restaurant(breakfastMenu.Cereal, lunchMenu.Tuna, dinnerMenu.Steak, dessertMenu.Cake);
customer1.printOrder();
customer1.breakfastBill();
