 # paddy-map

研究で作った水田スクリーニング（K-Means による水田／非水田の判定結果）を、ブラウザで見られる Web アプリ。
地図上で田んぼをLeafletで色分けし、地域と確信度で絞り込める。
Python（FastAPI）でAPIを作り、Leaflet で地図を描き、AWS で動かす。
