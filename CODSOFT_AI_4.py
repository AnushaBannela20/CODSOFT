import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# 1. Load Pre-trained CNN (ResNet50 for feature extraction)
base_model = ResNet50(weights="imagenet")
cnn_model = Model(inputs=base_model.input, outputs=base_model.layers[-2].output)

# Function to extract image features
def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = tf.keras.applications.resnet50.preprocess_input(x)
    features = cnn_model.predict(x, verbose=0)
    return features

# 2. Dummy vocabulary + captions (In practice, train with dataset like MSCOCO)
tokenizer = {"<start>":1, "a":2, "dog":3, "on":4, "the":5, "grass":6, "<end>":7}

# 3. Simple Decoder (RNN-like simulation)
def generate_caption(features):
    # Normally: LSTM/Transformer trained on dataset
    # Here: a fixed caption for demo
    return "a dog on the grass"

# 4. Run the pipeline
img_path = "dog.jpg"   # Replace with your image path
features = extract_features(img_path)
caption = generate_caption(features)

print("Generated Caption:", caption)

