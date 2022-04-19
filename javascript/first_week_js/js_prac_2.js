// javascript 연습_2

// 변수 더하기
let a = 3;
let b = 2;
console.log(a + b);
//5

// 문자열 더하기
let first_name = 'Gahyeon';
let last_name = 'Yun';
console.log(first_name + last_name);
// GahyeonYun

// list 만들기
let a_list = ['수박', '참외', '배'];
console.log(a_list[1]);
// 참외

// list 내용 추가
let a_list_push = a_list.push('감');
console.log(a_list_push);
//['수박','참외','배','감']

// list에 list추가
let b_list = ['x', 'y'];
let b_list_push = a_list.push(b_list);
console.log(b_list_push);
//['수박','참외','배','감',['x', 'y']]
console.log(b_list_push[4][0]); //타고타고 들어가는 형식
//x

//딕셔너리 : key-value
let c_dict = { name: 'bob', age: 27 };
console.log(c_dict['name']);
c_dict['height'] = 180; // 딕셔너리 추가
//bob

//js 내장 함수. 문자열자르기
let myemail = 'sparta@gmail.com';
let cut = myemail.split('@');
let cut_2 = myemail.split('@')[1];
let cut_3 = myemail.split('@')[1].split('.')[0]; //gmail

//남은 문법은 여기로!
//https://www.notion.so/tangy-note/AI-d7f4c9a1231e42848f23c3583b0be8d0#5d6aecee1a7140c8b8f3fb4e61e62679
