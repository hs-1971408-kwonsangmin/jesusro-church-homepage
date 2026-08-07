# 예수로교회 홈페이지

배포 주소: https://jesusro-demo.netlify.app

`main` 브랜치에 push하면 Netlify가 자동으로 배포합니다.

## 1. 파일 구성

```
├ index.html          ← 화면을 그리는 코드 (글 내용은 들어있지 않습니다)
├ content/            ← 홈페이지에 나오는 모든 글·사진 정보
│   ├ site.json           교회 이름·주소·전화·담임목사·예배 시간
│   ├ menu.json           상단 메뉴
│   ├ departments.json    부서 8개 (조직도·담당자 이름·연간일정)
│   ├ bulletins.json      온라인 주보
│   ├ sermons.json        설교 아카이브
│   ├ notices.json        공지사항
│   ├ gallery.json        사진첩
│   ├ calendar.json       첫 화면 행사 달력
│   └ facility.json       시설 안내 평면도
├ admin/              ← 관리자 화면 (글 수정 도구)
│   ├ index.html
│   └ config.yml
└ assets/             ← 사진 파일
```

**중요** — 예전에는 `index.html` 안에 글이 같이 들어 있었지만, 지금은 글과 사진 정보가
전부 `content/` 폴더로 분리되어 있습니다. 글을 고칠 때 `index.html`은 건드리지 않습니다.

## 2. 글 고치는 방법 (관리자 화면)

주소 뒤에 `/admin/` 을 붙이면 관리자 화면이 열립니다.

```
https://jesusro-demo.netlify.app/admin/
```

여기서 메뉴 추가·삭제, 부서 조직도의 목사님·부장집사님 이름, 주보 파일 업로드,
설교·공지·사진첩을 모두 고칠 수 있습니다. 저장하면 자동으로 홈페이지에 반영됩니다.

주보나 사진은 **파일을 화면에 끌어다 놓으면(드래그 앤 드롭)** 업로드됩니다.

### 로그인 설정 (아직 안 되어 있습니다)

현재 `admin/config.yml`의 로그인 설정은 임시값입니다. 이대로는 GitHub 계정이 있는
사람만 로그인할 수 있습니다. 교역자·집사님들이 쓰시려면 아래 설정이 필요합니다.

1. https://decapbridge.com 가입
2. **Create site** → 저장소 `hs-1971408-kwonsangmin/jesusro-church-homepage` 연결
3. 화면에 생성되는 `backend:` 설정을 복사해서 `admin/config.yml` 맨 위의 `backend:` 블록을 교체
4. 편집하실 분들을 이메일로 초대

## 3. 내 컴퓨터에서 미리 보기

`index.html`을 더블클릭해서 여는 방식은 이제 **동작하지 않습니다.**
브라우저 보안정책(CORS) 때문에 `content/` 폴더의 파일을 읽지 못합니다.

터미널에서 이 폴더로 이동한 뒤:

```bash
python3 -m http.server 8000
```

그리고 브라우저에서 `http://localhost:8000` 으로 접속하세요.

관리자 화면까지 로그인 없이 시험해 보려면 터미널을 하나 더 열어서:

```bash
npx decap-server
```

## 4. 사진 교체

`assets` 폴더의 파일을 같은 이름으로 덮어쓰면 됩니다. 관리자 화면에서 업로드해도 됩니다.

**권장 규격**
- 전경·배너용 가로 사진: 가로 1600px 내외, 용량 300KB 이하
- 주보: 글씨가 읽혀야 하므로 **가로 1500px 이상**을 권장합니다
- 인물 사진: 세로형, 가로 600px 내외

현재 `assets` 안의 일부 사진(`church-autumn` 563px, `church-winter` 515px,
`kids-worship` 225px, 주보 2장 264px)은 해상도가 낮아 크게 표시하면 흐릿합니다.
가능하면 원본 사진으로 교체하시는 것을 권합니다.

## 5. 페이지 직접 링크

주소 뒤에 `#`를 붙이면 특정 페이지로 바로 갈 수 있습니다.

| 주소 | 페이지 |
|---|---|
| `#greeting` | 담임목사 인사말 |
| `#sermon` | 설교 아카이브 |
| `#bulletin` | 온라인 주보 |
| `#board` | 교회 소식 |
| `#dept` | 부서 안내 |
| `#gallery` | 사진첩 |
| `#family` | 새가족 등록 |
| `#visit` | 오시는 길 |
| `#dept-youth` | 청소년부 (부서별로 `#dept-무엇` 형식) |

부서 페이지는 `dept-infant`(영아부), `dept-kids`(유치부), `dept-child`(아동부),
`dept-youth`(청소년부), `dept-young`(청년부), `dept-smallgroup`(목장·소그룹),
`dept-women`(여전도회), `dept-men`(남선교회) 입니다.

## 6. 아직 연결되지 않은 것

- 새가족 등록 폼은 화면 확인용이며 실제로 저장되지 않습니다. 접수 기능은 서버 연결이 필요합니다.
- 설교 영상은 안내 메시지만 뜹니다. 교회 유튜브 채널을 연결하면 됩니다.
- 온라인 헌금, SNS 링크는 안내 메시지만 뜹니다.
- 시설 평면도는 방문 안내용 개념도입니다. 실제 도면에 맞춰 수정이 필요합니다.
