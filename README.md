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
Windows PowerShellで下記を実行。

```
$ git clone git@github.com:junpeitsuji/mnist_flask.git
$ cd mnist_flask
$ python -m venv venv
$ .\venv\Scripts\activate

(venv) $ pip install matplotlib jupyterlab
(venv) $ pip install --upgrade tensorflow
(venv) $ pip install flask
```

ただし `.\venv\Scripts\activate` を実行するには、PowerShellを開く前に実行ポリシーを `RemoteSigned` に変更する必要があるかもしれない。
https://docs.vmware.com/jp/vRealize-Automation/7.6/com.vmware.vra.iaas.blade.doc/GUID-C86DCF49-F23B-4B9C-9FD5-95524FB74F01.html

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

<img width="1223" alt="スクリーンショット 2021-12-11 22 45 25" src="https://user-images.githubusercontent.com/1301953/145678919-5dbf9de0-c032-4bb6-aa9e-75e34b1365d2.png">

なお、学習に用いたmnistのモデル（60000データ中128データ分を画像化したもの）は static/images/mnist.jpg 内に入っています。
