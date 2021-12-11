# mnist_flask
tensorflowのMNISTサンプルをflaskと連携する

## 実行環境
```
Windows 10

$ python --version
3.8.10
$ pip --version
21.1.1 ...
```

## インストール方法
```
$ git@github.com:junpeitsuji/mnist_flask.git
$ cd mnist_flask
$ python -m venv venv
$ .\venv\Scripts\activate

$ pip install matplotlib jupyterlab
$ pip install --upgrade tensorflow
$ pip install flask
```

tensorflowのインストール方法は 
https://www.tensorflow.org/install/pip?hl=ja#virtual-environment-install を参照


# 実行方法
```
$ python app.py
（モデルが学習し終わるまでしばらく待つ）
```

その後 http://localhost:5000/ にアクセスする
