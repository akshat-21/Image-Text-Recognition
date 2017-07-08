# Image Text Recognition

* Used Tesseract Open Source OCR Engine for recognition of text from images.
  * **`grayscale.py`** is to convert the image to grayscale and **`blacknwhite.py`** is to convert image to image with white background. Used these for preprocessing of images to optimize results of Tesseract OCR.

* Used Microsoft's Computer Vision API
  * **`ocr.py`** detects text in an image and extract the recognised words into a machine-readable character stream and **`handwriting.py`** to detect and extract handwritten text from image.
