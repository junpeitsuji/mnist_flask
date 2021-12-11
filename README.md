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

mnistのサンプルコードは https://www.tensorflow.org/tutorials/quickstart/beginner?hl=ja を参照（実行結果は ipython_notebook/sample.ipynb にあります。）


# 実行方法
```
$ python app.py
（モデルが学習し終わるまでしばらく待つ）
```

その後 http://localhost:5000/ にアクセスする


# 実行結果
以下のようなページが表示されます。
（解像度が小さいので、ブラウザを拡大するといいです。）

黒い32x32の領域をマウスでドラッグすると、文字が書けます。
「判別」ボタンを押すと、モデルに基づいて判別されます。

<img width="799" alt="sample" src="https://user-images.githubusercontent.com/1301953/145673148-d98f6840-fff5-4055-bd60-5619b5204e98.png">

なお、学習に用いたmnistのモデル（60000データ中128データ分を画像化したもの）は static/images/mnist.jpg 内に入っています。
