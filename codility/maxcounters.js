// function solution(N, A) {
//   // Implement your solution here
//   answer = new Array(N).fill(0);

//   for (let i = 0; i < A.length; i++) {
//     if (A[i] != N + 1) {
//       answer[A[i] - 1] += 1;
//     } else {
//       for (let j = 0; j < N; j++) {
//         answer[j] = Math.max(...answer);
//       }
//     }
//   }
//   return answer;
// }  // N*M

function solution(N, A) {
  const counters = new Array(N).fill(0);
  let min = 0;
  let max = 0;
  for (let i = 0; i < A.length; i++) {
    if (A[i] === N + 1) {
      min = max; //맥스값 갱신하면서
    } else if (A[i] >= 1 && A[i] <= N) {
      const newValue = Math.max(min, counters[A[i] - 1]) + 1;
      counters[A[i] - 1] = newValue; // 입력할때 갱신해준다
      max = Math.max(max, newValue); // max 갱신
    }
  }

  for (let j = 0; j < N; j++) {
    counters[j] = Math.max(counters[j], min); // 갱신이후 한번도 입력안했을 경우 처리
  }

  return counters;
} //N+M

solution(5, [3, 4, 4, 6, 1, 4, 4]);
