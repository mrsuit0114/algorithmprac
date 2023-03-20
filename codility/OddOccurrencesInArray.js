function solution(A) {
  let stack = {};
  for (let i = 0; i < A.length; i++) {
    if (typeof stack[A[i]] === "undefined") {
      stack[A[i]] = true;
    } else {
      delete stack[A[i]];
    }
  }

  return +Object.keys(stack)[0];
}

// 삭제하고 넣고 해서 남은게 페어없는것

// function solution(A) {
//   // Implement your solution here
//   ans = {};
//   for (let i = 0; i < A.length; i++) {
//     if (A[i] in ans) {
//       ans[A[i]] += 1;
//     } else {
//       ans[A[i]] = 1;
//     }
//   }
//   for (let i in ans) {
//     if (ans[i] % 2) {
//       console.log(i);
//       return i;
//     }
//   }
// }

solution([9, 3, 9, 3, 9, 7, 9]);
