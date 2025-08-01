console.log('후츠릿');

/* 자바스크립트 필수 개념
1. 변수
2. 연산자
3. 조건문
4. 함수
5. 반복문
 */

// 변수와 상수 (const / let)
const username = 'TeaCa'; // 상수: 불변
let  userMBTI = 'ENTJ'; // 변수: 가변
console.log('userMBTI', userMBTI);
console.log('username', username);

userMBTI ="TeaCat"
console.log('userMBTI22', userMBTI)

// 데이터타입
/*
1. 숫자
2. 문자열
3. boolean
4. null/undefined
*/
const num = 1
const str = 'string'
const bool = true; //  or false
const data = null; // 개발자가 의도를 가지고 값을 비움
let empty;

console.log(num)
console.log(str)
console.log(bool)
console.log(data)
console.log(empty)
console.log('str:',typeof str)

// 조건문
const score = 70;

if (score>=60) {
  // true인 경우 실행
  console.log('✅합격')
} else {
  // false인 경우 실행
  console.log('❌불합격')
}

/* 조건문 축약 방법 -> 파이썬의 if else 내포문법이랑 비슷함.*/
// 삼항 연산자
// 문법=> 조건식 ? true인경우실행문 : false인경우실행문
score >= 60 ? console.log('합격') : console.log('불합격')

// 함수

// 함수 정의
function sayhello() {
  // 실행 로직
  console.log(username,'hello world!')
  return username + 'fire'
}

// 함수 호출 및 함수 확인하기
console.log(`${sayhello}`)
sayhello()
// 함수 호출2
const result = sayhello('dasom');
console.log('result:',result);

// 객체와 배열
// 배열 py=>list
const numbers = [1, 2, 3, 4, 5]
console.log('numbers:',numbers[2]);

//객체 py=>dict
const person = {
  name: '후츠릿',
  mbti: 'ENTJ',
};

console.log('name',person['name']);
console.log('name',person.name);

for (let i = 0; i < numbers.length; i++) {
  console.log('i',i);
  console.log('값',numbers[i]);
}

// 배열함수
numbers.forEach((value, index) => {
  // 실행 로직
  console.log('index:',index);
  console.log('value:',value);
})