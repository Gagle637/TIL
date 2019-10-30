const me = {
  name: 'ssafy', // key 가 한단어 일 때
  'phone number': '01012345678', // key 가 여러 단어 일 때
  appleProducts: {
    ipad: '2018pro',
    iphon: '7',
    macbook: '2019pro',
  }
}

console.log(me.name) // ssafy
console.log(me['name']) // ssafy
console.log(me['phone number']) // key가 여러 단어인 경우 반드시 []로 접근

console.log(me.appleProducts)
console.log(me.appleProducts.ipad)

// Object Literal(객체 표현법)
// ES5
var books = ['Learning JS', 'Eloquent Js']

var comics = {
  'DC': ['Joker', 'Aquaman'],
  'Marvel': ['Captain Marvel', 'Avergers'],
}

var megazines = null

var bookShop = {
  books: books,
  comics: comics,
  megazines: megazines,
}
console.log(typeof bookShop)
console.log(bookShop.books[0])

// ES6+
// object의 key 와 value 가 같다면, 마치 배열처럼 한번만 작성 가능
let bookShopTwo = {
  books,
  comics,
  megazines,
}
console.log(bookShopTwo)

////////////////////////////
// JSON(JavaScript Object Notation, JS 객체 표기법)
const jsonDate = JSON.stringify({ //JSON -> String
  coffe: 'Americano',
  iceCream: 'Mint Choco',
})
console.log(jsonDate) // {"coffe":"Americano","iceCream":"Mint Choco"}
console.log(typeof jsonDate)

const parseData = JSON.parse(jsonDate)
console.log(parseData)
console.log(typeof parseData)