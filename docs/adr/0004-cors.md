1. Context：ブラウザのJavaScript(map.js)が別ドメイン(AWS)のデータを読み取ることを、ブラウザ自体がデフォルトでブロックしていた
2. Decision：CORSMiddlewareです。src/api.pyに追加して、「このドメインからのアクセスはOK」と明示的に許可する設定を書きました。
3. Alternatives：フロントをAWS側にまとめることも可能でしたが、GitHub Pagesは無料で、わざわざAWS側にフロント用の仕組み（S3+CloudFrontなど）を追加するとコストも手間も増える
4. Consequences：楽になった分、どこの誰のWebサイトからでもこのAPIを叩けるようになった（セキュリティは緩い）。ただし元のデータが公開情報で書き込み権限も無いGETのみなので、実害は小さい