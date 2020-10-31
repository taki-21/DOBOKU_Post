# DOBOKU_Post
## URL
### https://doboku-post.site  
※ 「右上のログインボタン」 → 「かんたんログイン」 で新規登録なしでログインできます。

## イメージ図
![スクリーンショット 2020-10-28 0 27 14](https://user-images.githubusercontent.com/62042131/97323622-5558e080-18b4-11eb-8123-a430721c6985.png)


## 概要
主に土木、建築に関する写真を投稿し、共有できるアプリです。  
今まで知らなかった土木構造物、建築物及びその技術を知ることができます。

## 制作背景
　私は大学で４年間土木工学を学びました。その中で、「土木」という分野は日常を支える大きな役割を果たしているのにも関わらず、建設現場の３K（きつい、汚い、危険）というイメージがいまだ残っており、なかなか一般の方に興味を持ってもらえないと感じていました。実際に土木学科は年々減少し、さらに土木学科を専攻した人も最終的に土木以外の仕事につく人が多い印象を受けます。現在、土木・建築業界の人不足から建設現場の環境を改善することが急務となっていますが、それと同時に少しでも土木・建築に興味を持ってもらうことが必要だと感じ、このアプリケーションを制作しました。今まで知らなかった構造物や技術を気軽に知ることで、少しでも多くの方に土木・建築の魅力を感じてもらい、建設業界に対して興味を持っていただけたらと思っております。今後は写真のみではなく土木・建築に関する書籍や記事に関しても投稿できるよう機能を拡張したいと思っております。
 
## 使用技術
### フロントエンド
* Vue.js: 2.6.11
* Vue CLI: 4.4.6
* Vuetify: 2.2.11 （一部 UIkit: 3.5.6）
* HTML/CSS

### バックエンド
* Python: 3.8.3
* Django: 3.0
* Django REST Framework: 3.10
* poetry: 1.0.10
* uWSGI: 2.0.19.1

### Webサーバー
* Nginx: 1.17.8

### データベース
* PostgreSQL: 12.4

## 主な機能
### SPA
* VueとDjango REST Frameworkを使用することでフロントエンドとバックエンドを分離
* Vue CLIでbuildした静的ファイルをS3へデプロイ、CloudFrontで配信

### 投稿一覧
* 並び替え機能
  * 投稿日・いいねの数で並び替え
* 絞り込み機能
  * 橋やダムなどカテゴリによって投稿を絞り込む
  * 自分が投稿した投稿で絞り込む
  * 自分がいいねした投稿で絞り込む
  * 自分が投稿した投稿のみマップ表示
* マップ表示機能
  * 位置情報が登録されている投稿はマップ画面で位置を確認できる。
  * 吹き出しから詳細ページへ遷移が可能。
* 検索機能
  * タイトル、カテゴリ、投稿日、都道府県によって投稿を絞り込む（複数の条件を指定可能）
* 無限スクロール
  * vue-infinite-loadingを用いて実装
  * localStorageによりスクロール位置を保持

### 投稿詳細
* コメント機能
  * コメント送信
    * 非同期通信によりリアルタイムで送信結果が表示される
  * コメントの削除
    * 非同期通信によりリアルタイムで削除される。
* いいね機能
  * 非同期通信によりリアルタイムでカウントを反映
* 写真拡大機能
  * lightboxにより写真をクリックすると全画面で表示できる。
* 場所確認機能
  * 投稿に場所情報がある場合モーダルを用い地図表示できる。
  
### 新規投稿・投稿編集
* プレビュー表示
* 名前（タイトル）から住所及び緯度経度を検索「GoogleMap Geocording API」

### ユーザー周り
* ログイン機能
  * JWTによる認証
* 新規登録機能
* アカウント削除機能
* プロフィール編集機能
* フォロー・フォロワー機能

### テスト
* バックエンド
  * viewのテスト: 41methods
  * serializerのテスト: 6methods
* フロントエンド
  * 未実装

### その他
* マイページにて自分が投稿した投稿のカテゴリの割合を円グラフで表示
* レスポンシブ対応

## インフラ構成
### 構成図
![スクリーンショット 2020-10-10 19 33 22](https://user-images.githubusercontent.com/62042131/95652911-76d57080-0b2f-11eb-817f-71e84cba06da.png)
### AWS
* ECS/ECR/ALB/EC2/VPC/RDS(PostgreSQL)/S3/CroudFront/Route53/ACM
### Docker
* Docker: 19.03.12
* docker-compose: 1.27.2
  * ローカル環境を構築
### CircleCI
* 自動テスト
  * masterブランチ以外に pushすることでテスト開始
* 自動デプロイ
  * masterブランチへpushすることでECR/ECS/S3へデプロイ
  * Orbsを使用
  
## About me
  現在、22歳で某独立行政法人に勤務しております。バックエンドエンジニアを目指しポートフォリオの作成・改善、アウトプットを行っております。  
* [Twitter](https://twitter.com/saka___21)  
* [Qiita](https://qiita.com/saka___21)    
* [学習記録](https://saka-21.hatenablog.com/archive)


