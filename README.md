# Auto-Filtering
このソフトウェアは　NFSサーバとクライアントの依存関係を取得し，重みをつけた後，
通知されたアラートを分類し，アラートの通知量を削減するソフトウェアです．

### 環境
Ubuntu 22.04.4 LTS
Python Python 3.10.12

以下のソフトウェアがあることが前提です．
- Kubernetes
- NFSサーバ
- NFSクライアント
- Prometheus
- AlertManager
- Node-Exporter

### 使い方
Step1
```
cd  Auto-Filtering
```

Step2
```
python3 Auto_filtering.py 
```



