import numpy as np
from scipy.special import softmax
import tensorflow as tf
import tensorflow.keras as keras

def sigmoid(x):
    return 1 - 1 / (1 + np.exp(-x))


def uncrookedize(y_true, y_pred, is_tf=True):
    s = tf.math.reduce_sum(y_pred, axis=1)
    last_proba = 1 - tf.math.sigmoid(s)
    sigmoid_s_good_shape = tf.stack([tf.math.sigmoid(s)]*y_pred.shape[1], axis=1)
    first_proba = sigmoid_s_good_shape * tf.nn.softmax(y_pred)
    yy_pred = tf.concat([first_proba, last_proba[...,tf.newaxis]], axis=1)
    yy_true = tf.concat([y_true, (1- tf.math.reduce_sum(y_true, axis=1))[...,tf.newaxis]], axis=1)
    return yy_true, yy_pred


#def uncrookedize(y_true, y_pred, is_tf=True):
#    if is_tf:
#        s = tf.math.reduce_sum(y_pred, axis=1)
#        last_proba = 1 - tf.math.sigmoid(s)
#        sigmoid_s_good_shape = tf.stack([tf.math.sigmoid(s)]*y_pred.shape[1], axis=1)
#        first_proba = sigmoid_s_good_shape * tf.nn.softmax(y_pred)
#        yy_pred = tf.concat([first_proba, last_proba[...,tf.newaxis]], axis=1)
#        yy_true = tf.concat([y_true, (1- tf.math.reduce_sum(y_true, axis=1))[...,tf.newaxis]], axis=1)
#    else:
#        s = np.sum(y_pred, axis=1)
#        last_proba = 1 - sigmoid(s)
#        sigmoid_s_good_shape = np.stack([sigmoid(s)]*y_pred.shape[1], axis=1)
#        first_proba = sigmoid_s_good_shape * softmax(y_pred, axis=1)
#        yy_pred = np.concatenate([first_proba, last_proba[..., np.newaxis]], axis=1)
#        yy_true = np.concatenate([y_true, (1- np.sum(y_true, axis=1))[..., np.newaxis]], axis=1)
#    return yy_true, yy_pred

#def crooked_xentropy(y_true, y_pred):
#    """
#    Our customized loss function
#    Example: (4-class classification)
#        y_pred = [[ -500.0, -37.92, 99.99]]
#        y_true = [[0, 0, 0]]  # meaning that the true class is the fourth one.
#    """
#    s = tf.math.reduce_sum(y_pred, axis=1)
#    last_proba = 1 - tf.math.sigmoid(s)
#    sigmoid_s_good_shape = tf.stack([tf.math.sigmoid(s)]*y_pred.shape[1], axis=1)
#    first_proba = sigmoid_s_good_shape * tf.nn.softmax(y_pred)
#    yy_pred = tf.concat([first_proba, last_proba[...,tf.newaxis]], axis=1)
#    yy_true = tf.concat([y_true, (1- tf.math.reduce_sum(y_true, axis=1))[...,tf.newaxis]], axis=1)
#    #print(f"yy_pred =\n{yy_pred}")
#    #print(f"yy_true =\n{yy_true}")
#    #return tf.nn.softmax_cross_entropy_with_logits(
#    #    labels=yy_true,
#    #    logits=yy_pred,
#    #)
#    return keras.losses.categorical_crossentropy(
#        yy_true,
#        yy_pred,
#        from_logits=False,
#    )


def crooked_xentropy(y_true, y_pred):
    yy_true, yy_pred = uncrookedize(y_true, y_pred)
    return keras.losses.categorical_crossentropy(
        yy_true,
        yy_pred,
        from_logits=False,
    )


class CrookedAccuracy(keras.metrics.Metric):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.acc = keras.metrics.Accuracy()
    def update_state(self, y_true, y_pred, sample_weight=None):
        #yy_true, yy_pred = uncrookedize(y_true, y_pred)
        yy_true, yy_pred = uncrookedize(y_true, y_pred, is_tf=False)
        self.acc(tf.argmax(yy_true, axis=1), tf.argmax(yy_pred, axis=1))
    def result(self):
        self.acc.result()
    def get_config(self):
        base_config = super().get_config()
        return {**base_config}

