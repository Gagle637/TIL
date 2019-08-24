# Project_05

## 1. 사용기술

Django를 이용한 웹페이지 제작하였습니다.

bootstrap, google font을 이용한 html 제작



## 2. 프로젝트 설명

- Django Model, ORM을 포함한 CRUD 구현

- 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작

- Template Variable을 활용한 Template 제작

- 영화 추천 사이트의 영화 정보 데이터 관리

- Python Web Framework를 통한 데이터 조작

  
  
  ### 	1. 영화 목록

![index](/uploads/c80ec2ee2c182188e8eacb9f9d56534f/index.PNG)

- 위의 페이지는 접근하는 URL /movies/ 입니다. 

- 데이터베이스에 존재하는 모든 영화목록이 표시되며, 각 영화의 Title과 Score가 표시됩니다.
- Title을 클릭하면 `영화 정보 조회` 페이지로 이동합니다. 
- 페이지 좌측상단에 새 영화등록 링크가 있으며 클릭시 `영화 정보 생성` 페이지로 이동합니다.



### 		2. 영화 정보 생성(C, Create)

![new](/uploads/88af03da9d485485e7f3224a4822b8a6/new.PNG)

- `영화 정보 생성 페이지`이며 영화 정보를 작성 할 수 있는 Form이 표시됩니다.

- 해당 페이지에 접근하는 URL은 `/movies/new/` 입니다.

- 제출을 누르면  `영화 정보 생성 페이지`로 생성 요청(request)과 함께 전송됩니다.
- 생성 요청은 POST방식을 채택하였습니다.



 2.1영화 정보 생성(데이터베이스 저장)

- 해당 페이지에 접근하는 URL은 /movies/create/ 입니다.
- 페이지는 따로 구현되어있지 않으며 이전 페이지로부터 전송 받은 데이터를 데이터베이스에 저장하고 영화 정보를 조회하는 영화 정보 조회 페이지로 연결하는 역할을 합니다.



### 		3. 영화 정보 조회(R, Read)

![detail_01](/uploads/0178315f8fb0067421182ee941f1cc0c/detail_01.PNG)

![detail_02](/uploads/d411ad473931b96e6c365393abe9adca/detail_02.PNG)

- 영화 목록에서 Title을 선택한다면 위의 페이지와 연결됩니다.
-  해당 페이지에 접근하는 URL은 /movies/1/ , /movies/2/ 등 이며, 동 적으로 할당되는 부분이 존재합니다. 동적으로 할당되는 부분에는 데이터베 이스에 저장된 영화 정보의 Primary Key가 들어갑니다.
- 해당 Primary Key를 가진 영화의 모든 정보가 표시됩니다.
- 영화 정보의 최하단에는 목록 , 수정 , 삭제 링크가 있으며, 클릭 시 각각 영화 목록 , 해당 영화 정보 수정 Form , 해당 영화 정보 삭제 페이지로 이동합니다.



### 		4.영화 정보 수정(U, Update)

![edit](/uploads/2f223461338b76aed3479f83b4e85a9d/edit.PNG)

-  해당 페이지에 접근하는 URL은 /movies/1/edit/ , /movies/2/edit/ 등 이며, 동적으로 할당되는 부분이 존재합니다. 동적으로 할당되는 부분에는 데이터베이스에 저장된 영화 정보의 Primary Key가 들어갑니다
- 해당 Primary Key를 가진 영화 정보를 수정할 수 있는 Form이 표시 되며, 영화 정보 생성과 같은 Input값들을 가지고 있습니다.
- 이후 제출을 통해  /movies/1/update/로 연결되어  2.1영화 정보 생성(데이터베이스 저장)과 같은 과정으로 데이터 베이스를 수정하게 됩니다.



### 		5.영화 정보 삭제(D, Delete)

- 해당 페이지의 html은 따로 구현되어있지 않으며 `영화 정보 조회` 페이지의 하단 `삭제` 버튼을 통해 접근이 가능합니다.

- 해당 페이지의 URL은 /movies/1/delete/ , /movies/2/delete/ 등 이며, 동적으로 할당되는 부분이 존재합니다. 동적으로 할당되는 부분에는 데이터베이스에 저장된 영화 정보의 Primary Key가 들어갑니다.
- 해당 Primary Key를 가진 영화 정보를 데이터베이스에서 삭제합니다. 이후 `영화 정보 목록` 페이지로 Redirect 합니다.
