import tensorflow as tf
class InceptionV3():
    def __init__(self, input_shape, num_classes):
        self.input_shape = input_shape
        self.num_classes = num_classes

    def build_model(self):
        tf.keras.backend.clear_session()
        inputs = tf.keras.Input(shape=self.input_shape)

        InceptionV3 = tf.keras.applications.InceptionV3(input_shape = self.input_shape,
                                                        include_top=False, 
                                                        input_tensor=inputs,weights='imagenet'
                                                        )

        x = InceptionV3.get_layer('conv2d_69').output
        x = tf.keras.layers.GlobalAveragePooling2D()(x)
        outputs = tf.keras.layers.Dense(self.num_classes, activation='softmax')(x)
        model = tf.keras.Model(inputs, outputs)
        return model