# ベースにする環境：Python 3.12 が最初から入った、軽量版の Linux
FROM python:3.12-slim

# コンテナの中の作業フォルダを決める（以降のコマンドはここで実行される）
WORKDIR /app

# sqlite3 コマンド（schema.sql を流し込むのに使う）を入れる
# python:3.12-slim には Python しか入っていないので、これが無いと
# 「sqlite3: not found」になる
RUN apt-get update && apt-get install -y --no-install-recommends sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# ライブラリのリストだけ先にコピーして、インストールする
# （コードより先にこれだけコピーするのは、コードを直すたびに
# 　pandas 等を入れ直さずに済むようにする定石）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリ本体とデータ、設定ファイルをコピーする
COPY src/ src/
COPY data/ data/

# このコンテナは 8000 番ポートで通信する、という宣言
EXPOSE 8000

# コンテナが起動したときに実行するコマンド
# ローカルでやってきた「sqlite3 ... < schema.sql」「import_csv.py」「uvicorn」を
# 順番に実行する（CIの test.yml でやっているのと同じ考え方）
CMD sh -c "sqlite3 data/paddy.db < src/schema.sql && python3 src/import_csv.py && uvicorn src.api:app --host 0.0.0.0 --port 8000"
