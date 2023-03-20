// function solution(X, Y, D) {
//   // Implement your solution here
//   answer = 0;

//   let distance = Y - X;

//   answer =
//     distance % D ? Math.floor(distance / D) + 1 : Math.floor(distance / D);
//   return answer;
// }

function solution(X, Y, D) {
  return Math.ceil((Y - X) / D);
}
