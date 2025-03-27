# Docker Tutorial
このリポジトリは、**Dockerの基本操作を学ぶためのリポジトリ**です。  
PyTorch を使って MNIST を分類するモデルを、Docker上で学習・推論します。

## 使い方
```bash
# Dockerイメージのビルド
docker build --tag mnist-cnn .

# コンテナで学習
# ここでローカルの{SHARED_DIR}が/app/outputsと共有される
docker run --rm -v {SHARED_DIR}:/app/outputs mnist-cnn python train.py --save-path outputs/mnist_cnn.pth
# コンテナで学習済みモデルを使って推論
docker run --rm -v {SHARED_DIR}:/app/outputs mnist-cnn python test.py --model-path outputs/mnist_cnn.pth

# イメージ一覧の確認
docker images

# イメージの削除
docker rmi mnist-cnn
```

## 参考資料
- [【Docker入門】初心者向け！Dockerの基本を学んでコンテナ型の仮想環境を作ろう！](https://youtu.be/B5tSZr_QqXw?si=qTkjdDOOTLwJOK0c)
- [MLやってる人向けに最低限理解してほしいDocker勉強会](https://www.docswell.com/s/8590143908/KNRQVD-2023-10-25-145217#p1)
