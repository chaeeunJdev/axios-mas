# 관통프로젝트
<br>

# 1. 팀원 정보 및 업무 분담 내역
  ### - 정채은(팀장) : Django를 활용하여 server 구축, vue를 사용하여 영화 추천 알고리즘 구현
  ### - 최형운 : 전반적인 front 부분을 담당, vue를 활용하여 server에서 가져온 데이터를 가공, 출력
<br>

# 2. 목표 서비스 구현 및  실제 구현 정도
## 목표 서비스
* front
  * 전체적인 영화 목록을 보여주는 Index
  * 영화의 디테일(좋아요, 리뷰 기능)
  * Community(댓글 기능 포함)
  * 영화 추천 알고리즘(장르별 추천, youtube shorts처럼 예고편을 자동 재생)
  * 프로필(좋아요 누른 영화목록, 내가 쓴 게시글)

* back
  * 영화 데이터를 json 파일로 만들기
  * 영화 목록 가져오기
  * 영화 리뷰 댓글 기능 구현, 댓글 목록 저장
  * 게시글 저장 및 게시글 댓글 기능(수정, 삭제)
  * 로그인 기능

## 실제 구현 정도
* front
  * 전체적인 영화 목록을 보여주는 Index
  * 영화의 디테일(좋아요, 리뷰 기능)
  * Community(댓글 기능 포함)
  * 영화 추천 알고리즘(장르별 추천)
  * 프로필(좋아요 누른 영화목록)

* back
  * 영화 데이터를 json 파일로 만들기
  * 영화 목록 가져오기
  * 영화 리뷰 댓글 기능 구현, 댓글 목록 저장
  * 게시글 저장 및 게시글 댓글 기능(수정, 삭제)
  * 로그인 기능

## 총평 : front에서 2가지 기능을 제외 모두 구현

<br>

# 3. 데이터베이스 모델링(ERD)
<img src="./read/erd.png">
<br>


# 4. 영화 추천 알고리즘에 대한 기술적 설명
## MVTI
## 1. MVTI 첫 화면
<img src="./read/mvti1.png" width="50%">

## 2. 2개 중 하나씩 총 4개의 장르를 선택 한다.
<img src="./read/mvti2.png" width="50%">

## 3. 하단에 '나의 MVTI 확인하기'를 누르면 선택에 따른 결과가 나온다.
<img src="./read/mvti3.png" width="50%">

## 4. 새로고침도 가능하다.
<img src="./read/mvti4.png" width="50%">
<br>

## 기술적 설명
## 1. 버튼을 선택하면 해당 버튼에 저장되어 있는 장르를 전송한다.
## 2. 전송된 장르(영어)의 앞글자를 이용하여 MVTI가 완성된다.
## 3. 동시에 선택된 장르의 영화를 랜덤으로 하나씩 뽑는다.
## 4. 결과쪽 div에 하나씩 뽑힌 총 4개의 영화 포스터를 출력한다.

<br>

# 5. 서비스 대표 기능에 대한 설명
## 1. 영화 디테일
## 영화 디테일 첫 화면이다. 리뷰를 쓸수 있으며 포스터와 영화에 대한 정보들이 보여진다.
<img src="./read/detail1.png" width="50%">

## 예고편보기를 누르면 tmdb에서 받아온 해당 정보의 예고편을 볼수 있게 한다.
<img src="./read/detail2.png" width="50%">

## 해당 영화와 비슷한 영화를 보여준다. 보여지는 포스터를 누르면 해당 추천 영화의 디테일로 이동을 한다.
<img src="./read/detail3.png" width="50%">

## 2. 커뮤니티
## 1. 커뮤니티 첫화면
<img src="./read/community1.png" width="50%">

## 2. create 버튼을 누르면 토글된 작성칸이 나온다.
<img src="./read/community2.png" width="50%">

## 3. 작성된 내용은 사진과 같이 출력이 된다.
<img src="./read/community3.png" width="50%">

## 4. 작성된 커뮤니티 항목의 자세한 내용을 볼수 있다.
<img src="./read/community4.png" width="50%">

## 5. 작성자만 수정이 가능하다.
<img src="./read/community5.png" width="50%">

## 6. 정상적으로 수정이 된 모습이다.
<img src="./read/community6.png"    width="50%">

## 7. 댓글로 작성이 가능하다.
<img src="./read/community7.png"  width="50%">

## 8. 댓글 역시 수정이 가능하다.
<img src="./read/community8.png"  width="50%">

## 9. 정상적으로 수정이 된 모습이다.
<img src="./read/community9.png"  width="50%">

## 3. 검색

## 1. 상단에 검색바에 키워드를 입력한다
<img src="./read/search1.png"  width="50%">

## 2. 해당 키워드가 들어간 정보들을 출력한다.
<img src="./read/search2.png"  width="50%">

## 3. 장르 역시 검색이 가능하다.
<img src="./read/search3.png"  width="50%">

<br>


# 6. 기타(느낀 점, 후기)
## 최형운
### - 처음 시작할때 내가 이걸 할수 있을까라는 생각이 들었었습니다. 그러나 프로젝트가 진행되어가면서 조금씩이나마 성장하는 나의 모습을 보면서 뿌듯했습니다. 
### - 그리고 파트너와 소통을 하면서 기능을 추가하고 구글링을 통해 새로운 기능을 습득하는 재미가 있었습니다. 이전에 배웠었던 AXIOS같은 기능들을 어느정도 사용할수 있게 되었습니다. 
### - AXIOS 에러를 다양하게 접하면서 어디쪽 문제인지 살짝 알게 되었습니다. CSS에 대해 어느정도 생각한 모습을 구현 할수 있게 되었습니다. 
### - 특히 정렬 같은 경우에는 이해를 하지 못하고 하는 경우가 많았는데 이제는 이렇게 하면 되겠다 라고 생각을 하면서 할수 있게 되었습니다. 
### 그리고 bootstrap의 기능을 다양하게 사용해보면서 다음에 비슷한 상황을 겪을때 수월하게 진행할수 있게 된거 같습니다.

<br>

## 정채은
### - 그동안은 Django와 Vue를 따로 구현하여 각각을 개발했었다보니 Vue와 Django를 같이 활용하여 프로젝트를 진행하는 것이 어렵기도 하고, 이해가 덜 된 부분이 많아 실수도 많이 하였습니다. 특히나 Back 모델을 구현하고 Postman을 활용하여 제대로 구현이 되었는지 테스트를 한 후 Vue에 데이터를 넘겨 줬어야 하는데, 이 부분이 미숙했던 것 같아 아쉽기도하고 다음부터는 모델 구현 후 꼭 확인해보아야 겠다는 나름의 다짐을 하게되었습니다
### - model과 serializer에 대한 내용을 복습하지 않은 채로 진행하였다보니 원하는 필드를 화면에 출력함에 있어 serializer를 제대로 작성하지 못하여 발생하는 실수가 많았습니다. model에 필드를 작성하였더라도 화면에 출력하기 위해서 serializer 정의가 중요함을 느낄 수 있었습니다.
### - 기획과 기록의 중요성을 느낄 수 있었습니다. 프로젝트 시작 첫 날 나름 기획을 많이 하였다고 생각했지만, 프로젝트를 진행할 수록 중심이 흔들리기도하고 이것저것 다양한 기능들을 추가하다보니 복잡해지기도 하였습니다. 하지만 파트너와 함께 노션에 기획안과 추가 기능들을 계속하여 정리하고, 그 날 구현한 기능들, 겪었던 문제상황 및 해결방법을 기록하였던 것이 많은 도움이 되었습니다. 다음번에 하게 될 프로젝트는 더욱 꼼꼼하게 기록하고 기획해야겠다는 생각이 들었습니다.
### - 마지막으로 페어 프로그래밍을 체험하며 브랜치 생성 및 git merge에 관해 배울 수 있어서 좋았습니다. 서로 같은 파일을 수정한 채로 각 브랜치에 커밋하고 마스터에 merge하려고 하면 충돌이 일어나서 이런 문제로 몇번이나 브랜치를 삭제하고 다시 clone 받기를 반복한 후 git에서의 작업 영역 분리의 중요성을 느낄 수 있었습니다. 또한, 한가지의 주제를 파트너와 함께 공동의 목표를 정하고 세세한 부분까지 같이 토론하며 서로에게 맞춰가는 과정이 이번 프로젝트를 진행함에 있어 큰 힘이 되어주었고 파트너와의 소통의 중요성을 느낄 수 있었습니다.