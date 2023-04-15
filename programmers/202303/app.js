function solution(progresses, speeds) {
  // answer: 각 배포마다 배포되는 기능의 수가 적힌 정수 배열
  var answer = [];
  // days: 배포일
  let days = 1;
  // cnt: 오늘 배포되는 기능의 수
  let cnt = 0;
  // progress: 현재 기능의 작업 진도
  let progress = 0;

  // 모든 작업이 다 배포될 때까지 반복
  while (progresses[0]) {
    // 첫 번째 기능의 작업 진도
    progress = progresses[0] + speeds[0] * days;
    // 첫 번째 기능의 작업 진도가 100 이상인 경우 배포 완료
    if (progress >= 100) {
      // 배포 완료된 기능 개수 추가
      cnt++;
      // 배포 완료된 작업 제거
      progresses.shift();
      // 배포 완료된 작업의 속도 제거
      speeds.shift();
    }
    // 첫 번째 기능의 작업 진도가 100 미만일 경우 배포 불가능
    else {
      // 배포 완료된 기능이 있는 경우, answer에 push
      if (cnt > 0) {
        answer.push(cnt);
      }
      // 배포일 증가 (다음날)
      days++;
      // 배포 완료된 기능 개수 초기화
      cnt = 0;
    }
  }
  // 모든 작업이 다 배포되고 나면, 마지막으로 카운트된 배포 완료 기능 개수 push
  answer.push(cnt);

  return answer;
}

// function solution(progresses, speeds) {
//   var answer = [];
//   let days = [];
//   for (let i = 0; i < progresses.length; i++) {
//     let day = 0;
//     while (progresses[i] < 100) {
//       progresses[i] += speeds[i];
//       day++;
//     }
//     days.push(day);
//   }

//   cur = 0;

//   for (let i = 0; i < progresses.length; i++) {
//     count = 1;
//     i++;
//     while (days[i] >= cur) {
//       cur = days[i];
//       i++;
//       count++;
//       if (cur > days[i]) {
//         count--;
//       }
//     }
//     answer.push(count);
//   }

//   console.log(days);
//   return answer;
// }

solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1]);

// function solution(genres, plays) {
//   let answer = [];

//   // 1번 과정
//   let playCntByGenre = {};
//   for (let i = 0; i < genres.length; i++) {
//     playCntByGenre[genres[i]] = playCntByGenre[genres[i]]
//       ? playCntByGenre[genres[i]] + plays[i]
//       : plays[i];
//   }
//   // 여기서 playCntByGenre는 {classic:1450,pop:3100} 형태

//   // 재생횟수로 내림차순 정렬하기 위해, [키,밸류]의 배열 형태로 만들어준다
//   let keyValueArr = Object.entries(playCntByGenre);
//   keyValueArr.sort((a, b) => b[1] - a[1]);
//   // 정렬함수의 compareFunc 작성시, return 값이 양수면 앞뒤순서가 바뀐다는 점을 기억하면 쉽다!

//   // 여기서 keyValueArr는 [ [ 'pop', 3100 ], [ 'classic', 1450 ] ] 형태

//   // 2번 과정
//   let allInfoObj = genres.map((g, i) => ({
//     genre: g,
//     index: i,
//     playCnt: plays[i],
//   }));

//   // 3번 과정
//   keyValueArr.forEach((k, i) => {
//     let current = [];
//     for (let j = 0; j < allInfoObj.length; j++) {
//       if (k[0] === allInfoObj[j].genre) {
//         current.push(allInfoObj[j]);
//       }
//     }
//     current.sort((a, b) => b.playCnt - a.playCnt);
//     current.forEach((c, i) => {
//       if (i < 2) {
//         // 2개만 뽑아야 하기 때문에 index가 2보다 작을때까지만 answer.push 수행
//         answer.push(c.index);
//       }
//     });
//   });

//   console.log(answer);
//   return answer;
// }

// solution(
//   ["classic", "pop", "classic", "classic", "pop"],
//   [500, 600, 150, 800, 2500]
// );

// function solution(n)
// {
//     var answer = 0;
//     n = String(n)
//     for(let i =0; i<n.length; i++){
//         answer+= parseInt(n[i])
//     }

//     // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
//     console.log('Hello Javascript')

//     return answer;
// }

// function solution(angle) {
//   var answer = 0;
//   if (0 < angle && angle < 90) {
//     answer = 1;
//   } else if (angle == 90) {
//     answer = 2;
//   } else if (90 < angle && angle < 180) {
//     answer = 3;
//   } else if (angle == 180) {
//     answer = 4;
//   }
//   return answer;
// }

// console.log(solution(180));

// function solution(angle) {
//     return [0, 90, 91, 180].filter(x => angle>=x).length;
// }  오호..

//js에서 한번에 세개의 비교연산은 지원안하는군
