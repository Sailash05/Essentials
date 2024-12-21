console.log(__dirname);
console.log(__filename);
var a = 10;
module.exports = a;
console.log(module.exports);

const sayHello = require('./greetings');
console.log(sayHello('Alice'));