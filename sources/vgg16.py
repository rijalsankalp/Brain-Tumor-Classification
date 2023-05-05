import tensorflow as tf
class VGG16():
    def __init__(self, input_shape, num_classes):
        self.input_shape = input_shape
        self.num_classes = num_classes

    def build_model(self):
        tf.keras.backend.clear_session()
        inputs = tf.keras.Input(shape=self.input_shape)
        vgg16 = tf.keras.applications.VGG16(input_shape = self.input_shape,
                        include_top=False, 
                        input_tensor=inputs,weights='imagenet')
        x = vgg16.get_layer('block5_conv3').output
        x = tf.keras.layers.GlobalAveragePooling2D()(x)
        outputs = tf.keras.layers.Dense(self.num_classes, activation='softmax')(x)
        model = tf.keras.Model(inputs, outputs)
        return model