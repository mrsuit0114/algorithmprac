function solution(H) {
  // Implement your solution here
  stk = [];
  block = 0;
  hlen = H.length;
  for (let i = 0; i < hlen; i++) {
    if (stk.length == 0) {
      stk.push(H[i]);
      block++;
    } else {
      while (stk.length && stk[stk.length - 1] > H[i]) {
        stk.pop();
      }
      if (stk.length) {
        if (stk[stk.length - 1] == H[i]) {
          continue;
        } else {
          stk.push(H[i]);
          block++;
        }
      } else {
        stk.push(H[i]);
        block++;
      }
    }
  }
  console.log(block);
  return block;
}

solution([8, 8, 5, 7, 9, 8, 7, 4, 8]);

// 스택에 넣고 스택보다 현재가 작을때마다 스택에서 하나씩 빼고 같으면 넘어가고 크거나 len 0 이면 다시 넣고
