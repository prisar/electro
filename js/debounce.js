var debounce = require('./')

var sayHi = function() {
    console.log('hi');
  };
  
  var debounced = debounce(sayHi, 100);
  
  debounced();
  debounced();
  debounced();
  debounced();
  