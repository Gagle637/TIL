# Project 03 - HTML/CSS를 활용한 웹 사이트 구성

## 1. 프로젝트 목적 

- HTML를 통한 웹 페이지 마크업

- CSS를 통한 선택자 활용 및 속성 부여

- 시맨틱 태그를 활용한 기본 레이아웃 구성 

- 영화 추천 사이트 메인 레이아웃 구성 



## 2. 프로젝트 소개

### 2.1 header

HTML/CSS를 활용한 웹 사이트(영화 추천)를 구성하는 프로젝트입니다. 사이트의 제일 상단에 있는 웹 사이트의 헤더 부분에는 로고 이미지와 네비게이션 바를 구성했습니다.



```css
header {
  position: fixed;
  top: 0;
  z-index: 1000;
}
```

 다음과 같은 코드를 이용하여 `header`는 항상 사이트의 제일 상단에 위치하며 제일 위에 표시되며 다른 영역보다 우선하여 볼 수 있습니다.



```css
nav {
  float: right;
}

.nav-items>li {
  display: inline-block;
  margin: 0 1rem;
  list-style: none;
}
```

 네비게이션 바의 경우 HTML을 이용하여 리스트로 생성하고 위의 코드를 이용해 리스트 항목들을 한 줄로 만들어주고 리스트의 태그를 지우고 오른쪽으로 정렬이 됩니다.



```css
.nav-items>li>a:hover {
  color: crimson;
  text-decoration: none;
}
```

  네비게이션바의 항목들은 a태그로 인해 각각 임이의링크(#)에 연결되어 있습니다. 위 코드를 적용한다면 마우스를 오버시킬 때 항목들이 `crimson`의 색으로 변하는것을 볼 수 있습니다.

![nav1](/uploads/4ddc2178ff474bcb23343c1423a30292/nav1.PNG)

기본형

![nav2](/uploads/2dd16c832e6203f320ae5f47c2c88c4f/nav2.PNG)

마우스 오버 시



### 2.2 title section

```css 
#section-title {
  background-image: url('images/background.jpg');
  background-size: cover;
  background-position: center;
  text-align: center;
  line-height: 300px;
}
```

 서비스를 소개하는 문구와 배경 이미지가 있는 섹션을 구성합니다. 위의 코드는 배경이미지의 위치와 반복, 문구를 제어합니다.



### 2.3 aside

```css
aside {
  position: absolute;
  top : 0;
}

.aside-items {
  padding: 0;
}
```

 좌측 레이아웃에 장르 목록을 구성합니다. 자신이 속한 div의 상단에 고정어 나타날 것입니다.



### 2.4 movie section

 우측 레이아웃에 제공된 화 포스터를 활용하여 실시간 화 순위 목록을 구성할것입니다. 현재는 폴더(images)의 주어진 이미지를 활용하여 순위 목록을 구성 할 것입니다. aside의 너비를 제외한 너비를 가집니다.



### 2.5 footer

연도와 이름이 작성된 푸터를 구성합니다.  footer는 항상 하단에 위치합니다.

```css
footer {
  position: fixed;
  bottom: 0;
  text-align: center;
  line-height: 50px;
}
```



### 3.결과

![결과물1](/uploads/41017bb36fda36e21a73752c2dd9f39d/결과물1.PNG)



![결과물2](/uploads/20ecbe9dba448f5b86c42735d1dfe320/결과물2.PNG)





