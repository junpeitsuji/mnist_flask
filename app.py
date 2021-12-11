import numpy as np
from PIL import Image

from flask import Flask, render_template, request
app = Flask(__name__)

import tensorflow as tf


def init_model():
    # mnistのデータを取得
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0  # [0,255]->[0,1] に規格化

    # 機械学習モデルを設定
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ])

    # 誤差関数
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    # 学習に関する設定
    model.compile(optimizer='adam',
                loss=loss_fn,
                metrics=['accuracy'])

    # 学習を実行
    model.fit(x_train, y_train, epochs=5)

    # テストデータの評価
    model.evaluate(x_test,  y_test, verbose=2)

    return model



# 文字画像表示
def ConvertToImg(img):
    return Image.fromarray(np.uint8(img))

# データを画像形式に変換して保存
def save_image(data):
    # MNIST一文字の幅（32px）
    chr_w = data.shape[1]
    # MNIST一文字の高さ（32px）
    chr_h = data.shape[2]

    # 文字を１枚の画像に描画する
    canvas = Image.new('RGB', (chr_w, chr_h), (255, 255, 255))

    # 文字を読み込んで描画
    chrImg = ConvertToImg(data.reshape(chr_w, chr_h))
    canvas.paste(chrImg, (0, 0))

    #canvas.show()
    # 画像をJPEGとして保存
    canvas.save('static/images/test_data/mnist_test.jpg', 'JPEG', quality=100, optimize=True)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 送られてきたデータを取得
        arr = np.array(eval(request.form['key']))
        print(arr.shape)

        # 送られてきたデータを画像にして保存
        save_image(arr)  

        # 学習したモデルで予測
        predictions = model(arr).numpy()
        #print(predictions)
        result = tf.nn.softmax(predictions).numpy()
        print("softmax:", result)
        argmax = np.argmax(result)
        print("argmax:", argmax)

        # 結果をJSONで返す
        return {'result': str(argmax), 'softmax': str(result[0])}

    return render_template('index.html')


if __name__ == "__main__":
    # モデルを作成・学習
    model = init_model()

    app.run(host='0.0.0.0', debug=True)
