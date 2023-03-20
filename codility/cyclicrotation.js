function solution(A, K) {
  const index = K % A.length;
  return A.splice(A.length - index, index).concat(A);
}

// function solution(A, K) {
//   answer = [];
//   let t = K % A.length; //한번 다 도는 거 처리
//   let count = 0;
//   while (count != A.length) {
//     answer.push(A[(A.length - t + count) % A.length]);
//     count++;
//   }

//   console.log(answer);
//   return answer;
// }

a = solution([3, 8, 9, 6, 7], 3);
