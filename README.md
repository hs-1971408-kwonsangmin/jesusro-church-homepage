# 예수로교회 홈페이지 시안 — 사용 안내

## 1. 파일 구성

```
site/
 ├ index.html          ← 홈페이지 본체 (이 파일만 열면 됩니다)
 ├ assets/             ← 사진 폴더
 │   ├ church-spring.jpg     봄 · 교회 전경
 │   ├ church-summer.jpg     여름 · 교회 전경
 │   ├ church-autumn.jpg     가을 · 교회 전경
 │   ├ church-winter.jpg     겨울 · 교회 전경
 │   ├ church-family.jpg     전교인 단체사진
 │   ├ pastor-portrait.jpg   담임목사 인물사진
 │   ├ pastor-welcome.jpg    인사말 페이지 상단 배너
 │   ├ youth-retreat.jpg     청년·청소년부 수련회
 │   ├ kids-worship.jpg      주일학교(유치부) 예배
 │   ├ bulletin-winter.jpg   주보 이미지(겨울)
 │   └ bulletin-autumn.jpg   주보 이미지(가을)
 └ README.md           ← 이 문서
```

## 2. 사진 교체 방법 (가장 중요)

**파일 이름만 똑같이 맞춰서 덮어쓰면 끝입니다.** HTML을 수정할 필요가 없습니다.

예를 들어 봄 사진을 바꾸고 싶으면:
1. 새 사진의 이름을 `church-spring.jpg` 로 바꾼다
2. `assets` 폴더에 넣어 기존 파일을 덮어쓴다
3. 브라우저에서 새로고침 (Ctrl+F5)

**권장 규격**
- 전경·배너용 가로 사진: 가로 1600px 내외, 용량 300KB 이하
- 인물 사진: 세로형, 가로 600px 내외
- 형식: JPG (PNG도 되지만 용량이 커집니다)

**어느 사진이 어디에 쓰이는지**

| 파일명 | 사용되는 곳 |
|---|---|
| church-spring.jpg | 히어로(봄), 사역카드, 갤러리, 새가족 CTA, 소식 페이지 상단 |
| church-summer.jpg | 히어로(여름), 이번주 설교 썸네일, 설교·오시는길 페이지 상단 |
| church-autumn.jpg | 히어로(가을), 사역카드, 주보·갤러리 페이지 상단 |
| church-winter.jpg | 히어로(겨울), 사역카드, 부서 페이지 상단 |
| church-family.jpg | 갤러리(전교인 사진) |
| pastor-portrait.jpg | 홈 인사말 섹션, 인사말 페이지 |
| pastor-welcome.jpg | 인사말 페이지 상단 배너 |
| youth-retreat.jpg | 청소년부 페이지, 부서 카드, 갤러리 |
| kids-worship.jpg | 유치부 카드, 청소년부 앨범, 갤러리 |

## 3. 글 내용 수정 방법

`index.html` 파일을 메모장이나 VS Code로 열어서 아래 부분을 찾아 고치면 됩니다.

- **설교 목록** → `const sermons=[` 로 시작하는 부분
- **공지사항** → `const notices=[`
- **부서 안내** → `const departments=[`
- **갤러리** → `const gallery=[`
- **주보** → `const bulletinData={`
- **청소년부 앨범·게시판·연간일정** → `const youthAlbums=[`, `youthNotices`, `youthYear`
- **행사 캘린더** → `const calendarEvents={`

## 4. 인터넷 주소로 올리는 방법 (무료)

### 가장 쉬운 방법 — Netlify Drop
1. 브라우저에서 `app.netlify.com/drop` 접속
2. **site 폴더 전체**를 화면에 드래그 앤 드롭
3. 몇 초 뒤 `랜덤이름.netlify.app` 주소가 생성됨 → 그 링크를 공유

회원가입 없이도 임시 배포가 되며, 가입하면 주소 이름을 바꿀 수 있습니다.

### GitHub Pages
1. GitHub 저장소 생성 후 site 폴더 내용 업로드
2. Settings → Pages → Branch를 main / root로 지정
3. `아이디.github.io/저장소명` 으로 접속

### 교회 도메인(jesusro.com) 연결
현재 운영 중인 홈페이지가 그 주소를 쓰고 있으므로, 시안 단계에서는
`demo.jesusro.com` 같은 하위 주소를 쓰는 것을 권장합니다.
Netlify/GitHub Pages 설정에서 도메인을 추가하고, 도메인 관리 업체에서
DNS(CNAME) 레코드를 연결하면 됩니다.

## 5. 페이지 직접 링크

주소 뒤에 `#`를 붙이면 특정 페이지로 바로 갈 수 있습니다.

- `주소/#greeting` — 담임목사 인사말
- `주소/#sermon` — 설교 아카이브
- `주소/#bulletin` — 온라인 주보
- `주소/#board` — 교회 소식
- `주소/#dept` — 부서 안내
- `주소/#youth` — 청소년부
- `주소/#gallery` — 사진첩
- `주소/#family` — 새가족 등록
- `주소/#visit` — 오시는 길

카카오톡이나 문자로 "청소년부 페이지 보세요" 하며 `주소/#youth`를 보내면
바로 그 화면이 열립니다.

## 6. 참고

- 이 시안은 **데이터베이스 없이** 작동합니다. 새가족 등록 폼은 화면 확인용이며
  실제로 저장되지 않습니다. 실제 접수 기능은 제작 업체가 서버와 연결해야 합니다.
- 설교 영상은 현재 안내 메시지만 뜹니다. 실제로는 교회 유튜브 채널을 연결하면 됩니다.
- 시설 평면도는 방문 안내용 개념도입니다. 실제 도면에 맞춰 수정이 필요합니다.
