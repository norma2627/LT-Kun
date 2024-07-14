# LTくん
- サークル用のbot
- LTのテーマを管理

## コマンド
`/get`: LTのテーマを取得<br>
`/post {theme-title}`: LTのテーマを保存<br>
`/check`: 保存されているLTのテーマを確認<br>

## デプロイ先
- [Koyeb](https://app.koyeb.com)

## 環境構築
### デバッグ用Botとサーバー作成
ローカルからデバッグをするためのDiscord Botの作成などを記載しています。
[デバッグ環境のセットアップ](./docs/setup-dev.md)

### Development
コンテナをビルドする。  
```sh
docker build -t -lt-kun .
```

コンテナを実行する。  
```sh
docker run lt-kun
```

Discordから`/get`などのコマンドを実行する。  
