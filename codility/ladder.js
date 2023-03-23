function solution(A, B) {
  // Implement your solution here
  Alen = A.length;

  const max = Math.pow(2, 30);
  dp = new Array(Alen + 1).fill(0);
  dp[1] = 1;
  dp[2] = 2;

  for (let i = 2; i < Alen; i++) {
    dp[i + 1] = (dp[i] + dp[i - 1]) % max;
  }

  answer = [];

  for (let i = 0; i < Alen; i++) {
    answer.push(dp[A[i]] % 2 ** B[i]);
  }

  return answer;
}

solution([4, 4, 5, 5, 1], [3, 2, 4, 3, 1]);
