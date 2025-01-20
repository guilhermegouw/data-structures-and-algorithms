/*
1 - 2
-----
10, 4
3, 9

Day 1. f1 = 10, f2 = 3 => 13 / 13 = 1
Day 2. f1 = 4, f2 = 9 => 13 / 13 = 1



**/

function getTotalBonus(franchises, days, sales) { // [[10, 4], [3, 9]]
    let totalBonus = 0;
    for (let i = 0; i < franchises; i++) { // [10, 4]
        for (let j = 0; j < days; j++) {
            let dailySales = sales[i][j] // sales[0][0]
            totalBonus += Math.floor(dailySales / 13)
        }
    }
    return totalBonus;
}

function getBonusByDay(franchises, days, sales) {
  let totalBonus = 0;
  let daySales = {}
  for (let i = 0; i < franchises; i++) {
    for (let j = 0; j < days; j++){
      let dayKey = "day" + j;
      if (!daySales[dayKey]) {
        daySales[dayKey] = 0;
      }
      daySales[dayKey] += sales[i][j]
    }
  }
  for (let z = 0; z < franchises; z++) {
    sum = sales[z].reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    let franchiseKey = "franchise" + z;
    if (!daySales[franchiseKey]) {
      daySales[franchiseKey] = 0;
    }
    daySales[franchiseKey] += sum
  }
  
  for (let key in daySales) {
    totalBonus += Math.floor(daySales[key] / 13)
  }
  console.log(totalBonus)
  return totalBonus
}

getBonusByDay(2, 2, [[10, 4], [3, 9]])
