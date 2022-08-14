# doboku-post

## URL

### https://doboku-post.site

※ 「右上のログインボタン」 → 「かんたんログイン」 で新規登録なしでログインできます。

## イメージ図

![スクリーンショット 2020-10-28 0 27 14](https://user-images.githubusercontent.com/62042131/97323622-5558e080-18b4-11eb-8123-a430721c6985.png)

## 概要

主に土木、建築に関する写真を投稿し、共有できるアプリです。
今まで知らなかった土木構造物、建築物及びその技術を知ることができます。

## 制作背景

私は大学で４年間土木工学を学びました。その中で、「土木」という分野は日常を支える大きな役割を果たしているのにも関わらず、建設現場の３ K（きつい、汚い、危険）というイメージがいまだ残っており、なかなか一般の方に興味を持ってもらえないと感じていました。実際に土木学科は年々減少し、さらに土木学科を専攻した人も最終的に土木以外の仕事につく人が多い印象を受けます。現在、土木・建築業界の人不足から建設現場の環境を改善することが急務となっていますが、それと同時に少しでも土木・建築に興味を持ってもらうことが必要だと感じ、このアプリケーションを制作しました。今まで知らなかった構造物や技術を気軽に知ることで、少しでも多くの方に土木・建築の魅力を感じてもらい、建設業界に対して興味を持っていただけたらと思っております。今後は写真のみではなく土木・建築に関する書籍や記事に関しても投稿できるよう機能を拡張したいと思っております。

## 使用技術

### フロントエンド

- Vue.js: 2.6.11
- Vue CLI: 4.4.6
- Vuetify: 2.2.11 （一部 UIkit: 3.5.6）
- HTML/CSS

### バックエンド

- Python: 3.8.3
- Django: 3.0
- Django REST Framework: 3.10
- poetry: 1.0.10

### Web サーバー

- Nginx: 1.17.8

### アプリケーションサーバー

- uWSGI: 2.0.19.1

### データベース

- PostgreSQL: 12.4

## 主な機能

### SPA

- Vue と Django REST Framework を使用することでフロントエンドとバックエンドを分離
- Vue CLI で build した静的ファイルを S3 へデプロイ、CloudFront で配信

### 投稿一覧

- 並び替え機能
  - 投稿日・いいねの数で並び替え
- 絞り込み機能
  - 橋やダムなどカテゴリによって投稿を絞り込む
  - 自分が投稿した投稿で絞り込む
  - 自分がいいねした投稿で絞り込む
  - 自分が投稿した投稿のみマップ表示
- マップ表示機能
  - 位置情報が登録されている投稿はマップ画面で位置を確認できる。
  - 吹き出しから詳細ページへ遷移が可能。
- 検索機能
  - タイトル、カテゴリ、投稿日、都道府県によって投稿を絞り込む（複数の条件を指定可能）
- 無限スクロール
  - vue-infinite-loading を用いて実装
  - localStorage によりスクロール位置を保持

### 投稿詳細

- コメント機能
  - コメント送信
    - 非同期通信によりリアルタイムで送信結果が表示される
  - コメントの削除
    - 非同期通信によりリアルタイムで削除される。
- いいね機能
  - 非同期通信によりリアルタイムでカウントを反映
- 写真拡大機能
  - lightbox により写真をクリックすると全画面で表示できる。
- 場所確認機能
  - 投稿に場所情報がある場合モーダルを用いて地図表示ができる。

### 新規投稿・投稿編集

- プレビュー表示
- 名前（タイトル）から住所及び緯度経度を検索「GoogleMap Geocording API」
- 各フォームにバリデーションを実装

### ユーザー周り

<img width="600" alt="スクリーンショット 2020-11-01 16 19 49" src="https://user-images.githubusercontent.com/62042131/97797155-12a15a80-1c5e-11eb-9bd3-5e4461ed5851.png">

- ログイン機能
  - JWT による認証
- 新規登録機能
- アカウント削除機能
- プロフィール編集機能
- フォロー・フォロワー機能

### テスト

- バックエンド
  - view のテスト: 41methods
  - serializer のテスト: 6methods
- フロントエンド
  - 未実装

### その他

- マイページにて自分が投稿した投稿のカテゴリの割合を円グラフで表示
- レスポンシブ対応

## インフラ構成

### 構成図

![スクリーンショット 2020-10-10 19 33 22](https://user-images.githubusercontent.com/62042131/95652911-76d57080-0b2f-11eb-817f-71e84cba06da.png)

### AWS

- ECS/ECR/ALB/EC2/VPC/RDS(PostgreSQL)/S3/CloudFront/Route53/ACM を使用
- S3 にバケットを 2 つ作り、一つは Vue.js のファイル、もう一つはアップロードされる投稿画像やアイコン画像を格納する。
- CloudFront により、S3 に配置したファイルを高速かつ安全に配信する。
- VPC 内でサブネットを二つ作成し一つは EC2 インスタンスにそれぞれ配置された Django と Nginx による API サーバーとして利用し、もう一つは RDS によって REST API のデータを管理するために利用する。
- Route53 によりドメインを管理する。
- ACM により SSL 証明書を発行し暗号化通信をすることで安全性を確保する。

### Docker

- Docker: 19.03.12
- docker-compose: 1.27.2
  - ローカル環境を構築

### CircleCI

- 自動テスト
  - master ブランチ以外に push することでテスト開始
- 自動デプロイ
  - master ブランチへ push することで Django, Nginx のファイルを ECR/ECS へデプロイ
  - develop ブランチへ push することで Vue.js の静的ファイルを S3 へデプロイ
  - Orbs を使用

## ER 図

<img width="600" alt="スクリーンショット 2020-11-01 16 19 49" src="https://user-images.githubusercontent.com/62042131/99896250-1dd22e00-2cd2-11eb-93d3-d89b64aece04.jpg">
