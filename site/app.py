import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('../model/mnist.h5')

def preprocess_image(image):
    image = cv2.resize(image, (28, 28))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image / 255.0
    image = np.reshape(image, (1, 28, 28, 1))
    return image

def app():
    st.title("Digit Recognition")
    canvas = st.canvas()

    if st.button("Predict"):
        drawn_image = np.array(canvas.image_data)
        preprocessed_image = preprocess_image(drawn_image)
        prediction = model.predict(preprocessed_image)
        digit_index = np.argmax(prediction)
        st.write("Predicted Digit:", digit_index)

if __name__ == "__main__":
    app()
