function shopStock(stockList) {
    while (true) {
        
        while (true) { //Inputting item
            let shoppingItem = prompt("What item are you looking for?");
            let shoppingItemLower = shoppingItem.toLowerCase(); //Standardising inputs

            let pluralCheck = shoppingItemLower.endsWith('s'); 
            var [verb1, verb2] = pluralCheck === true ? [' have', ' are'] : [' has', ' is'];

            if (/[a-zA-Z]/.test(shoppingItemLower) === false) { //Regex to ensure input is one character minimum
                alert('Input must contain at least one letter!')
            } else if (stockList.includes(shoppingItem)) {
                alert("'" + shoppingItemLower + "'" + verb2 + ' currently in stock');
                break;
            } else {

                while (true) { //Adding item to list
                    let orderBool = window.prompt("'" + shoppingItemLower + "'" + verb2 + ' not in stock\nWould you like to order the item?\n\nEnter Y or N');
                    let orderBoolLower = orderBool.toLowerCase();

                    if (orderBoolLower === 'y')  {
                        stockList.push(shoppingItem);
                        let printList = stockList.join(', ');
                        alert("'" + shoppingItemLower + "'" + verb1 + ' been added!\n\nStock List:\n' + printList);
                        break;
                    } else if (orderBoolLower === 'n') {
                        break;
                    } else {
                        alert('Invalid Input!\nPlease enter either Y or N');
                    }
                } 
            break;
            }
        }

        while (true) { //Repeat Loop Prompt  
        let repeatBool = prompt('Would you like to check another item?\n\nEnter Y or N');
            let repeatBoolLower = repeatBool.toLowerCase();

            if (repeatBoolLower === 'n') {
                return alert('Noted. I\'ll remember this list until you close the site.\nHave a good day!');
            } else if (repeatBoolLower === 'y'){
                break;
            } else {
                alert('Invalid Input!\nPlease enter either Y or N');
            }
        }
    }
}