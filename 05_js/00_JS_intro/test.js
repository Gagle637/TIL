function concat(str1, str2) {
  return `${str1} - ${str2}`
}

function checkLongStr(string) {
  return string.length > 10 
}

if (checkLongStr(concat('Happy', 'Hacking'))) {
  console.log('LONG STRING')
} else {
  console.log('SHORT STRING')
}