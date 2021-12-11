import tensorflow as tf


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

# 学習済みモデルの保存
model.save('data/learned_mnist_model.h5')
