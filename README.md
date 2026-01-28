# 의약품 정보 시스템 (Pharmaceutical Information System)

Django와 MySQL을 사용한 의약품 정보 관리 웹 애플리케이션입니다.

## 주요 기능

### 1. 의약정보 검색
- **성분별 검색**: 약품의 성분으로 검색
- **회사별 검색**: 제조회사로 검색
- **효능별 검색**: 약품의 효능으로 검색
- **상세정보 제공**: 용법, 용량, 주의사항, 부작용 등

### 2. 게시판
- 게시글 작성, 수정, 삭제
- 페이지네이션 (10개씩)
- 로그인 사용자만 작성 가능

### 3. 사용자 인증
- Django 기본 인증 시스템
- 로그인/로그아웃

### 4. About Us
- 회사 소개 페이지

## 기술 스택

- **Backend**: Django 6.0
- **Database**: MySQL (또는 SQLite for development)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Language**: Python 3.12+

## 설치 방법

### 1. 저장소 클론

```bash
git clone https://github.com/ywhcho/med3_eun3.git
cd med3_eun3
```

### 2. 가상환경 생성 및 활성화

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정

`.env.example` 파일을 `.env`로 복사하고 필요한 값을 설정합니다:

```bash
cp .env.example .env
```

`.env` 파일 내용 (개발 환경의 경우 기본값 사용 가능):

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# MySQL 사용 시
DB_ENGINE=django.db.backends.mysql
DB_NAME=medinfo_db
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=3306
```

**참고**: 환경 변수가 설정되지 않으면 자동으로 SQLite를 사용합니다.

### 5. 데이터베이스 마이그레이션

```bash
python manage.py migrate
```

### 6. 관리자 계정 생성

```bash
python manage.py createsuperuser
```

### 7. 샘플 데이터 추가 (선택사항)

```bash
python manage.py shell < populate_data.py
```

### 8. 개발 서버 실행

```bash
python manage.py runserver
```

브라우저에서 `http://127.0.0.1:8000/` 접속

## 관리자 페이지

관리자 페이지는 `http://127.0.0.1:8000/admin/`에서 접근할 수 있습니다.

여기서 다음을 관리할 수 있습니다:
- 성분 (Ingredient)
- 제조회사 (Company)
- 효능 (Efficacy)
- 의약품 (Medicine)
- 게시글 (Post)
- 사용자 (User)

## 프로젝트 구조

```
med3_eun3/
├── board/              # 게시판 앱
│   ├── models.py       # Post 모델
│   ├── views.py        # 게시판 뷰
│   └── templates/      # 게시판 템플릿
├── medicines/          # 의약품 앱
│   ├── models.py       # Medicine, Ingredient, Company, Efficacy 모델
│   ├── views.py        # 의약품 검색 및 상세 뷰
│   └── templates/      # 의약품 템플릿
├── medproject/         # 프로젝트 설정
│   ├── settings.py     # Django 설정
│   └── urls.py         # URL 라우팅
├── templates/          # 공통 템플릿
│   ├── base.html       # 베이스 템플릿 (네비게이션 바 포함)
│   ├── home.html       # 홈페이지
│   └── about.html      # About Us
├── static/             # 정적 파일
│   └── css/
│       └── style.css   # 커스텀 CSS
├── populate_data.py    # 샘플 데이터 스크립트
├── requirements.txt    # Python 패키지 목록
└── manage.py           # Django 관리 스크립트
```

## 데이터베이스 모델

### Medicine (의약품)
- 제품명, 제조회사, 성분, 효능
- 용법용량, 주의사항, 부작용, 보관방법
- 허가번호, 허가일자

### Ingredient (성분)
- 성분명, 설명

### Company (제조회사)
- 회사명, 주소, 전화번호, 웹사이트

### Efficacy (효능)
- 효능명, 설명

### Post (게시글)
- 제목, 내용, 작성자, 조회수
- 작성일, 수정일

## MySQL 설정 (프로덕션)

MySQL을 사용하려면:

1. MySQL 서버 설치 및 실행
2. 데이터베이스 생성:

```sql
CREATE DATABASE medinfo_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'meduser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON medinfo_db.* TO 'meduser'@'localhost';
FLUSH PRIVILEGES;
```

3. `.env` 파일에 MySQL 정보 설정
4. `mysqlclient` 설치:

```bash
pip install mysqlclient
```

## 보안 주의사항

프로덕션 환경에서는:
1. `DEBUG=False`로 설정
2. `SECRET_KEY`를 안전하게 생성하고 보관
3. `ALLOWED_HOSTS`에 실제 도메인 추가
4. HTTPS 사용
5. 데이터베이스 자격 증명 보안 관리

## 라이선스

이 프로젝트는 교육 목적으로 만들어졌습니다.

## 문의

문의사항이 있으시면 이슈를 등록해주세요. 

## Bootstrap 설치 (선택사항)

기본적으로 CDN에서 Bootstrap을 로드합니다. 오프라인 환경이나 보안상의 이유로 로컬에 설치하려면:

```bash
# static/bootstrap 디렉토리에 Bootstrap 다운로드
cd static
wget https://github.com/twbs/bootstrap/releases/download/v5.3.0/bootstrap-5.3.0-dist.zip
unzip bootstrap-5.3.0-dist.zip
mv bootstrap-5.3.0-dist bootstrap
```

그런 다음 `templates/base.html`에서 CDN 링크를 로컬 파일 경로로 변경하세요.

