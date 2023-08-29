# 🍔 fastapi-practice
[점프투 FastApi](https://wikidocs.net/book/8531) 와 [공식문서](https://fastapi.tiangolo.com/ko/async/#in-a-hurry) 를 참고하여 공부하고 있습니다.

# 공부 내용 기록
## 0827
- fast api의 초기 설정과 app, router에 대한 전반적인 이해
- migration 관리 alembic에 대한 전반적인 이해
```
## 마이그레이션 방법
1. 스키마 변경 이후 `alembic revision --autogenerate`를 작성.
2. `alembic upgrade head`으로 데이터베이스에 적용한다.
3. `alembic history` 으로 마이그레이션을 확인한다.

## 기타
- `alembic current` 를 사용하면 현재 마이그레이션 상태를 확인할 수 있다.
- `alembic downgrade -1`를 사용하면 이전 상태로 되돌릴 수 있다.
```
- database 연결 및 `SQLALCHEMY`의 모델 및 base에 관련하여 공부
- pydantic을 통한 스키마(dto) 이해.
- 기타 파이썬의 Union과 fastapi의 Depends 조금 이해

## 0829
- DTO(schema)를 통한 response에 대한 이해. (response model 활용)
- response model을 사용하기 위해서는 return 할 때 객체가 필요하다.
