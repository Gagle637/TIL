// 배열로 이루어진 숫자들을 모두 더하는 함수
const numberAddEach = number => {
  let sum = 0
  for (const number of numbers) {
    sum += number
  }
  return sum
}

// 배열로 이루어진 숫자들을 모두 빼는 함수
const numberSubEach = number => {
  let sub = 0
  for (const number of numbers) {
    sub += number
  }
  return sub
}

// 배열로 이루어진 숫자들을 모두 빼는 함수
const numberMuleach = number => {
  let mul = 0
  for (const number of numbers) {
    mul *= number
  }
  return mul
}
// 그런데 매번 이렇게 함수를 새로 정의해야 하나??
// 공통점 : 숫자로 이루어진 배열의 요소들을 각각 [??] 한다.
// [??] 를 callback 함수에서 처리하는 일로 바꿔보자.

// base 템플릿 역할
const numberEach  = (numbers, callback) => {
  let acc 
  for (const number of numbers) {
    acc = callback(number, acc)
  }
  return acc
}

// 더한다.
const addEach = (number, acc = 0) => {
  return acc + number
}

// 뺀다.
const subEach = (number, acc = 0) => {
  return acc - number
}

// 곱한다.
const mulEach = (number, acc = 1) => {
  return acc * number
}

const NUMBERS = [1,2,3,4,5]
console.log(numberEach(NUMBERS, addEach))
console.log(numberEach(NUMBERS, subEach))
console.log(numberEach(NUMBERS, mulEach))

//  그런데 addEach, subEach, mulEach 얘네들 다시 사용안할것같은데..??
// numbersEach 이후의 제어를 함수 정의 없이 매번 자유롭게 하려면 어떻게 해야 할까?
console.log(numberEach(NUMBERS, (number, acc=0) => acc+number ))
console.log(numberEach(NUMBERS, (number, acc=0) => acc-number ))
console.log(numberEach(NUMBERS, (number, acc=1) => acc*number ))
