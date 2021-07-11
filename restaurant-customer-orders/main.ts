enum breakfastMenu {
    Cereal = 2.99,
    Toast = 1.50,
}
enum lunchMenu {
    Tuna = 5.99,
    Ham = 4.99
}
enum dinnerMenu {
    Beef = 8.99,
    Steak = 9.99
}
enum dessertMenu {
    Cake = 7.99,
    IceCream = 5.99
}

class Restaurant {

    breakfast: breakfastMenu;
    lunch: lunchMenu;
    dinner: dinnerMenu;
    dessert: dessertMenu;

    constructor(breakfast, lunch, dinner, dessert){
        this.breakfast = breakfast;
        this.lunch = lunch;
        this.dinner = dinner;
        this.dessert = dessert;
    }

    printOrder(){
        let breakfastItem = breakfastMenu[this.breakfast];
        let lunchItem = lunchMenu[this.lunch];
        let dinnerItem = dinnerMenu[this.dinner];
        let dessertItem = dessertMenu[this.dessert];
        console.log(`Order = ${breakfastItem}, ${lunchItem}, ${dinnerItem}, ${dessertItem}`)
    };

    breakfastBill(){
        let prices = [];
        prices.push(this.breakfast, this.lunch, this.dinner, this.dessert)
        var sum = prices.reduce((a, b) => a + b, 0);
        console.log(`Total = £${sum}`)
    }
}

var customer1 = new Restaurant (breakfastMenu.Cereal, lunchMenu.Tuna, dinnerMenu.Steak, dessertMenu.Cake)
customer1.printOrder()
customer1.breakfastBill()