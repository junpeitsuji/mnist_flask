import numpy as np
from PIL import Image
import tensorflow as tf
import json

from flask import Flask, render_template, request
app = Flask(__name__)


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
        arr = np.array(json.loads(request.form['key']))

        # 送られてきたデータを画像にして保存
        save_image(arr)  

        arr = arr / 255.0
        print(arr.shape)

        # 学習したモデルで予測
        predictions = model(arr).numpy()
        #print(predictions)
        result = tf.nn.softmax(predictions).numpy()
        print("softmax:", result)

        # softmaxの値が一番高いindexを判別結果とする(0-9)
        argmax = np.argmax(result)
        print("argmax:", argmax)

        # 結果をJSONで返す
        return {'result': str(argmax), 'softmax': str(result[0])}

    return render_template('index.html')


if __name__ == "__main__":
    # mnistの学習済みモデルを読み込み
    model = tf.keras.models.load_model('data/learned_mnist_model.h5')

    app.run(host='0.0.0.0', debug=True)
