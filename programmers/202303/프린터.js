function solution(priorities, location) {
  let max;
  let cnt = 0;

  while (true) {
    max = Math.max.apply(null, priorities);
    let n = priorities.shift(); //맨 앞의 요소를 빼낸다

    if (n === max) {
      //꺼낸 요소가 max와 같으면
      cnt++; //pop하므로 cnt 1증가
      if (location === 0) {
        //만약 location이 0이되면
        return cnt; //cnt를 return
      }
    } else {
      //꺼낸 요소가 max와 다르면
      priorities.push(n); //배열 맨 끝에 꺼낸 요소를 추가
    }
    location--; //한 차례마다 location값을 계속 줄여나간다

    if (location == -1) {
      //만약 -1이 되어버리면 다시 배열의 맨끝으로 보낸다
      location = priorities.length - 1;
    }
  }
  return cnt;
}

solution([1, 1, 9, 1, 1, 1], 0);
