![image](https://github.com/user-attachments/assets/272de719-651e-4246-8264-c12b6d9eae5c)

![image](https://github.com/user-attachments/assets/a4a59809-9751-4da6-aa9b-7c5de77f1075)

# Horse or Human Classification

This project involves creating an AI model to classify images as either containing a horse, a human, or neither. The model is implemented using TensorFlow, and a web application for uploading and classifying images is built using Flask. The web interface is designed with HTML and CSS to provide a user-friendly experience.

## Project Overview

### AI Model
- **Objective**: Classify images into three categories: horse, human, or neither.
- **Technology**: TensorFlow for model training and prediction.
- **Model**: A neural network model saved as `model.keras`.

### Web Application
- **Framework**: Flask for handling server-side logic and routes.
- **Frontend**: HTML and CSS for the user interface.
- **Functionality**: 
  - Upload an image through a web form.
  - Display the classification result on a new page.
  - Redirect to an error page if there's an issue with the upload or classification.
  - 
## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/horse-or-human.git
   cd horse-or-human]

   Create a Virtual Environment

2. **Create a Virtual Environment**
  python -m venv venv

3. **Activate the Virtual Environment**
   windows:
   venv\Scripts\activate

   macOS/linux:
   source venv/bin/activate

4. **Install Dependencies**
    pip install -r requirements.txt

5. **Run the Flask Application**
   python app.py

   The application will be available at http://127.0.0.1:5000.
