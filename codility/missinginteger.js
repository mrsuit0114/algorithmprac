function solution(A) {
  // Implement your solution here
  const sorted = A.sort((a, b) => a - b)
  count = 1;
  for (let i = 0; i < sorted.length; i++) {
    if (sorted[i] < count) {
      continue;
    } else if (sorted[i] > count) {  //
      return count;
    }
    count++;
  }
  // console.log(count);
  return count;
}

// function solution(A) {
//   const sorted = A.sort((a, b) => a - b)  //오름차순

//   let current = 0
//   for (let i = 0; i < sorted.length; i++) {
//     if (sorted[i] - current > 1) {  // 
//       return current + 1
//     }
//     if (sorted[i] > 0) {  //
//       current = sorted[i]
//     }
//   }

//   return current < 0 ? 1 : current + 1
// }

solution([2, 2, 8, 3, 4, 7, 7, 7, 7]);
