function solution(A) {
  // Implement your solution here

  let ret = A.reduce((a, b) => a + b, 0);
  let n = A.length;
  const sum = Math.floor((n * (n + 1)) / 2);
  return sum - ret;
}
