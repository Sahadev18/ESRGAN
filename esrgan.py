import os
import time
from PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import sys
os.environ["TFHUB_DOWNLOAD_PROGRESS"] = "True"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python esrgan.py <file_path>')
        sys.exit(1)
    
    IMAGE_PATH = sys.argv[1]
    # Add your logic to process the uploaded file here
    print('Processing file:', IMAGE_PATH)

# Declaring Constants
SAVED_MODEL_PATH = './model' 

def preprocess_image(image_path):
  """ Loads image from path and preprocesses to make it model ready
      Args:
        image_path: Path to the image file
  """
  hr_image = tf.image.decode_image(tf.io.read_file(image_path))
  # If PNG, remove the alpha channel. The model only supports
  # images with 3 color channels.
  if hr_image.shape[-1] == 4:
    hr_image = hr_image[...,:-1]
  hr_size = (tf.convert_to_tensor(hr_image.shape[:-1]) // 4) * 4
  hr_image = tf.image.crop_to_bounding_box(hr_image, 0, 0, hr_size[0], hr_size[1])
  hr_image = tf.cast(hr_image, tf.float32)
  return tf.expand_dims(hr_image, 0)

def save_image(image, filename):
  """
    Saves unscaled Tensor Images.
    Args:
      image: 3D image tensor. [height, width, channels]
      filename: Name of the file to save.
  """
  if not isinstance(image, Image.Image):
    image = tf.clip_by_value(image, 0, 255)
    image = Image.fromarray(tf.cast(image, tf.uint8).numpy())
  image.save("%s.jpg" % filename)
  print("Saved as %s.jpg" % filename)

# #%matplotlib inline
def plot_image(image, title=""):
  """
    Plots images from image tensors.
    Args:
      image: 3D image tensor. [height, width, channels].
      title: Title to display in the plot.
  """
  image = np.asarray(image)
  image = tf.clip_by_value(image, 0, 255)
  image = Image.fromarray(tf.cast(image, tf.uint8).numpy())
  plt.imshow(image)
  plt.axis("off")
  plt.title(title)

hr_image = preprocess_image(IMAGE_PATH)

# Plotting Original Resolution image
plot_image(tf.squeeze(hr_image), title="original")
save_image(tf.squeeze(hr_image), filename="./LR/original")

model = hub.load(SAVED_MODEL_PATH)

start = time.time()
fake_image = model(hr_image)
fake_image = tf.squeeze(fake_image)
print("Time Taken: %f" % (time.time() - start))

# Plotting Super Resolution Image
plot_image(tf.squeeze(fake_image), title="SR")
save_image(tf.squeeze(fake_image), filename="./static/SR")