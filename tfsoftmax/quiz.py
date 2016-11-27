# Solution is available in the other "solution.py" tab
import tensorflow as tf


def run():
    output = None
    logit_data = [2.0, 1.0, 0.1]
    logits = tf.placeholder(tf.float32)

    # ToDo: Calculate the softmax of the logits
    # softmax =
    softmax = tf.nn.softmax(logits)

    with tf.Session() as sess:
        # ToDo: Feed in the logits data
        #output = sess.run(softmax,    )
        output = sess.run(softmax, feed_dict={logits: logit_data})

    return output
