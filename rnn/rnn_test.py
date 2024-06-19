import numpy as np
import os
import shutil

import tensorflow_datasets as tfds
import tensorflow as tf
import keras

tfds.disable_progress_bar()


url = 'https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz'

dataset = tf.keras.utils.get_file('aclImdb_v1.tar.gz', url,
                                  untar=True, cache_dir='.',
                                  cache_subdir='')

dataset_dir = os.path.join(os.path.dirname(dataset), 'aclImdb')
print("Dataset Dir: {}".format(dataset_dir))

train_dir = os.path.join(dataset_dir, 'train')
print("Train Dir: {}".format(train_dir))

# remove unused folders to make it easier to load the data
remove_dir = os.path.join(train_dir, 'unsup')
shutil.rmtree(remove_dir)