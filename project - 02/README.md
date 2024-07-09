# Edge Detection with Canny Edge Detection

## Information

This Python script uses the OpenCV library to perform edge detection on an image. The script first converts the image to grayscale, applies Gaussian blur to reduce noise, and then uses the Canny edge detection method to find the edges in the image.

## Requirements

To run this script, you need the following:

- Python 3
- OpenCV (`cv2`) library
- NumPy (`numpy`) library
- An image file for edge detection (`test_image_2.jpg`)

To install the required libraries, use:

```
pip install opencv-python numpy
```

## Execution

Save the code in a Python file (e.g., `edge_detection.py`).
Place the image file (e.g., `test_image_2.jpg`) in the same directory or update the path in the script accordingly.
Run the following command in the terminal or command prompt:
```
python3 edge_detection.py
```
## Output

When the script is executed, three different windows will open with the following outputs:

- **Original Image**: The original grayscale image
- **Blurred Image**: The image after applying Gaussian blur
- **Edges**: The result image showing edges detected using the Canny edge detector

### Example Outputs

#### Original Image
![Original Image](img/borg.jpg)

#### Blurred Image
![Blurred Image](img/blur.jpg)

#### Edges
![Edges](img/bmask.jpg)
