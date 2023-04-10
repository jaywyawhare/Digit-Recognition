# Digit Recognition App

This is a Streamlit application that allows users to draw digits on a canvas and predicts the drawn digits using a pre-trained neural network model. The application is based on the popular MNIST dataset, which consists of images of hand-drawn digits (0-9) and their corresponding labels.

## Features
- User-friendly interface for drawing digits on a canvas.
- Prediction of drawn digits using a pre-trained neural network model.
- Real-time display of the drawn digit and the predicted digit on the app.
- Ability to reset the canvas and draw a new digit.

## Prerequisites
Before running the application, make sure you have the following dependencies installed:

- Python (3.6+)
- Streamlit
- OpenCV (cv2)
- TensorFlow
  
You can install the required dependencies using the following command:
```bash
pip install -r requirements.txt
```

## How to Run

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/mnist-digit-recognition-app.git
    ```
    
2. Navigate to the project directory:
    ```bash
    cd mnist-digit-recognition-app
    ```

3. Place your pre-trained model file (mnist.h5) in the model directory.

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

5. Open a web browser and enter the URL http://localhost:8501/ to access the app.

6. Draw a digit on the canvas and click the "Predict" button to see the predicted digit.

## Model Training
The pre-trained model (mnist.h5) used in this app was trained on the MNIST dataset using a deep neural network. The training code and details of the model architecture can be found in the [Notebook](./notebook/notebook.ipynb) file in this repository.

## Contributing
If you would like to contribute to this project, you can open an issue or submit a pull request. All contributions are welcome!

## License
This project is open-source and available under the MIT License.

## Acknowledgements
This application was developed using the following libraries and frameworks:

- Streamlit: https://streamlit.io/
- OpenCV: https://opencv.org/
- TensorFlow: https://www.tensorflow.org/
- MNIST dataset: http://yann.lecun.com/exdb/mnist/

Special thanks to the authors and contributors of these libraries and datasets for their valuable work.