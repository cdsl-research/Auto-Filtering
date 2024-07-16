# Auto-Filtering
このソフトウェアは　NFSサーバとクライアントの依存関係を取得し，重みをつけた後，
通知されたアラートを分類し，アラートの通知量を削減するソフトウェアです．
監視ソフトウェアはPrometheusを想定しています．

### 環境
- Ubuntu 22.04.4 LTS

- Python 3.10.12

必要なライブラリ
Flask
slackweb
subprocess
yaml
prometheus_api_client
datetime



### 対象ソフトウェア

Prometheus

NFSサーバ

NFSクライアント


### 構成要素

- ```monitoring_item_check.py```
  - get_prometheus_rules(): Prometheusの監視の監視のアラートのルールの内容を読み取り，取得する．
  - extract_expr_from_rules(): Prometheusに対してルールの問い合わせ
  - get_prometheus_query_result(): Prometheusに対する結果を表示
  - weight(): NFSサーバとディレクトリの共有関係共有関係を取得する

- ```monitoring_weight.py```
  - monitoring_weight(): NFSサーバとクライアントを特定
  - weight_calculation(): NFSサーバとディレクトリのディレクトリの共有関係から重さの計算
 
- ```Auto_filterring.py```
  - notification(): アラートの通知内容を作成する関数
  - format_alert_message(): アラートメッセージをフォーマットする関数
  - alert(): アラートを通知する関数


### 使い方
Step1
```
cd  Auto-Filtering
```

Step2
```
python3 Auto_filtering.py 
```



### 出力結果

実際にこんなアラートが出ます．

<img width="309" alt="スクリーンショット 2024-07-16 12 13 47" src="https://github.com/user-attachments/assets/c32c9bae-0faa-4506-af3c-0795c73c4187">


