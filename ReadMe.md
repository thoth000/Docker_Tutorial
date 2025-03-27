# docker tutorial
このリポジトリは、**Dockerの基本操作を学ぶためのリポジトリ**です。  
PyTorch を使って MNIST を分類するモデルを、Docker上で学習・推論します。

## 使い方
```bash
# Dockerイメージのビルド
docker build --tag mnist-cnn .

# コンテナで学習(ローカルのSHARE_DIRECTORYが/app/outputsと共有される)
ocker run --rm -v {SHARE_DIRECTORY}:/app/outputs mnist-cnn python train.py --save-path outputs/mnist_cnn.pth
# コンテナで学習済みモデルを使って推論
docker run --rm mnist-cnn python infer.py

# イメージ一覧の確認
docker images

# イメージの削除
docker rmi mnist-cnn

# 実行中コンテナの確認
docker ps

# 全コンテナの確認
docker ps -a
