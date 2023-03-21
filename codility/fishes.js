function solution(A, B) {
  // Implement your solution here
  upfish = 0;
  downfishes = [];
  for (let i = 0; i < A.length; i++) {
    if (B[i] == 1) {
      downfishes.push([A[i]]);
    } else {
      if (downfishes.length == 0) {
        // 내려오는놈이 없는 경우
        upfish++;
      } else {
        // 있는경우
        while (downfishes && downfishes[downfishes.length - 1] < A[i]) {
          downfishes.pop();
        }
        if (downfishes.length == 0) {
          upfish++;
        }
      }
    }
  }

  let answer = upfish + downfishes.length;
  console.log(answer);
  return answer;
}

solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]);

// 앞순서에서0이나오는놈은 만나는게 불가능
// 이후 1이 나오는 순간부터 시작 1이나올때마다 스택에 넣고 0을만나면 비교하고 죽으면 스택에서 빼면서 계속 진행하다가
// 살면 다음차례 이어서하기
// 남아있는 물고기는 스택의 크기와 어떻게든 위로 빠져나간 물고기수의 합
