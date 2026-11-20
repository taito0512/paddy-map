1. Context：canaryを最初5%にしたが、コンテナの台数が1台しかないため0台になった
2. Decision：canaryを5%→100%にした
3. Alternatives：別のデプロイ戦略（ROLLING）に変えることも検討したが、ECS Express Modeの制約でCANARY以外は選べなかった
4. Consequences：カナリアデプロイ本来の目的（新バージョンを少しだけ試して安全確認する）が実質できなくなり、新バージョンにバグがあればいきなり全体に影響する