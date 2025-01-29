# Spam Detector Web App

A simple **Spam Detection** web application using **FastAPI** and **Scikit-learn**. This app predicts whether a given text message is spam or not using a pre-trained machine learning model.

## Features

- 🚀 **FastAPI Backend**: Lightweight and high-performance API.
- 🧠 **Machine Learning Model**: Uses a trained spam detection model with **Scikit-learn**.
- 🎨 **Interactive UI**: Simple and user-friendly interface with **HTML, CSS, and JavaScript**.
- 🔍 **Real-Time Prediction**: Instantly detects spam messages.

## Technologies Used

- **FastAPI** for the backend
- **Scikit-learn** for machine learning
- **Joblib** for model serialization
- **Jinja2** for HTML templating
- **JavaScript** for frontend interactions

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/sobanaramakrishnan/spam-detector.git
   cd spam-detector
   ```

2. **Create a Virtual Environment** (Optional but recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the FastAPI Server**
   ```sh
   uvicorn main:app --reload
   ```

5. **Access the Web App**  
   Open your browser and go to:
   ```
   http://127.0.0.1:8000
   ```

## Usage

1. Enter a text message in the input box.
2. Click the **Check Spam** button.
3. View the spam classification and probability result.

## API Endpoint

- **POST `/predict`**
  - **Request:** `message` (string)
  - **Response:** Classification (`Spam` or `Not Spam`) and probability.

## Example API Request

```sh
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/x-www-form-urlencoded" -d "message=Congratulations! You've won a prize."
```

## Example API Response

```json
{
  "classification": "Spam",
  "spam_probability": "85.23%"
}
```

## License

This project is open-source and available under the **MIT License**.

---

**Happy Coding! 🚀**

