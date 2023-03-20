// function solution(X, A) {
//   // Implement your solution here
//   let answer = -1;
//   let leaves = {};

//   for (let i = 0; i <= A.length; i++) {
//     if (X >= A[i]) {
//       leaves[A[i]] = 1;
//     }
//     if (Object.keys(leaves).length == X) {
//       answer = i;
//       break;
//     }
//   }

//   return answer;
// }

// 키값들을 구하는게 내부적으로 O(n)인가봐..

function solution(X, A) {
  const realSum = (X * (X + 1)) / 2;
  const leaves = new Array(X).fill(false);
  let actualSum = 0;
  for (let i = 0; i < A.length; i++) {
    if (leaves[A[i] - 1] === false) {
      actualSum += A[i];
      leaves[A[i] - 1] = true;
    }

    if (actualSum === realSum) {
      return i;
    }
  }
  return -1;
}
