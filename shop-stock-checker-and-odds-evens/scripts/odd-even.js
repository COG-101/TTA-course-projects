// MOST CONCISE SOLUTION
// ---------------------
function oddEven() {
    var message = [];
    for (let i = 0; i < 16; i++) {
        (i % 2 == 0) ? message.push( i + ' is even') : message.push( i + ' is odd');
    }
    return alert('Odds & Evens Between 0-15:\n\n' + message.join('\n'));
}



// SOLUTION B (USING IF ELSE)
// ---------------------------
// function oddEven() {
//     var message = [];
//     for (let i = 0; i < 16; i++){
//         if (i % 2 == 0){
//             message.push( i + ' is even');
//         } else {
//             message.push( i + ' is odd');
//         }
//     }
//     return alert('Odds & Evens Between 0-15:\n\n' + message.join('\n'))
// }



// SOLUTION C (USING SWITCH STATEMENT)
// ------------------------------------
// function oddEven() {
//     var message = [];
//     for (let i = 0; i < 16; i++){
//         switch (i % 2){
//             case 0:
//                 message.push( i + ' is even');
//                 break;
//             case 1:
//                 message.push( i + ' is odd');
//                 break;
//         }
//     }
//     return alert('Odds & Evens Between 0-15:\n\n' + message.join('\n'))
// }