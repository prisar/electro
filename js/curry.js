var curry = require('./')

function add(a, b) {
    return a + b;
  }
  
  var curried = curry(add);
  console.log(  curried(1)(2)  ); // 3