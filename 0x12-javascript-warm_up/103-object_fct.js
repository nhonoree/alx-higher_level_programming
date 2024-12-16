#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value++;
  }
};

console.log(myObject); // { type: 'object', value: 12 }

myObject.incr();
console.log(myObject); // { type: 'object', value: 13, incr: [Function] }

myObject.incr();
console.log(myObject); // { type: 'object', value: 14, incr: [Function] }

myObject.incr();
console.log(myObject); // { type: 'object', value: 15, incr: [Function] }
