const maior = (...args) => {
  let max = count = 0   
  for (let x of args) {
    count += 1
    if (x > max) {
      max = x
    }   
  }
  console.log(`Foram informados ${count} valores ao todo.`)
  console.log(`O maior valor é ${max}`);
}

maior(2, 9, 4, 5, 7, 1)

