# Dockerfile (이 내용을 복사해서 붙여넣으세요)

# 1. 베이스 이미지 변경: Python 3.10 사용!
FROM python:3.10

# 2. 작업 디렉토리 설정
WORKDIR /workspace # 또는 /app 등 원하는 경로

# 3. requirements.txt 복사
#    Dockerfile과 같은 위치에 requirements.txt 파일이 있어야 합니다.
COPY requirements.txt ./

# 4. pip 업그레이드 및 requirements.txt 로 패키지 설치
#    requirements.txt 안에 pysqlite3-binary가 포함되어 있어야 합니다.
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 5. (선택사항) 나머지 코드 복사 - 볼륨 마운트 사용 시 불필요
# COPY . .

# 6. 기본 실행 명령어
CMD ["/bin/bash"]