// const nothing = () => {
//   console.log('')
// }

// console.log('start')
// setTimeout(nothing, 300)
// console.log(end)

function sleep_3s() {
  setTimeout(() =>  console.log('wake up'), 3000)

  
console.log('start')
sleep_3s() //
console.log(end)

}
function first() {
  console.log('frist')
}
function second() {
  console.log('second')
}
function third() {
  console.log('third')
}

first()
setTimeout(second, 1000)
third()

console.log('Hi')

setTimeout(function ssafy() {
  console.log('ssafy')
}, 100)
console.log('bye')

function printHello () {
  console.log('hello from baz')
}

function baz() {
  setTimeout(printHello, 3000) // 0초라도 먼저 돌아가지 않습니다.
}

function bar () {
  baz()
}

function foo() {
  bar()
}
foo()