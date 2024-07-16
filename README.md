# Auto-Filtering
このソフトウェアは　NFSサーバとクライアントの依存関係を取得し，重みをつけた後，
通知されたアラートを分類し，アラートの通知量を削減するソフトウェアです．
監視ソフトウェアはPrometheusを想定しています．

### 環境
Ubuntu 22.04.4 LTS

Python 3.10.12

必要なライブラリ
Flask
slackweb
subprocess
yaml
prometheus_api_client
datetime


### 構成要素

- ```monitoring_item_check.py```
  - get_prometheus_rules(): Prometheusの監視の監視のアラートのルールの内容を読み取り，取得する．
  - extract_expr_from_rules(): Prometheusに対してルールの問い合わせ
  - get_prometheus_query_result(): Prometheusに対する結果を表示
  - weight(): 重さを算出






### 使い方
Step1
```
cd  Auto-Filtering
```

Step2
```
python3 Auto_filtering.py 
```



