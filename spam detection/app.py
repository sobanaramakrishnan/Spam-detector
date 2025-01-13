from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib

# Load pre-trained model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Initialize FastAPI app
app = FastAPI()

# Template setup
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Render the spam detector HTML page.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict_spam(message: str = Form(...)):
    """
    Predict if the given message is spam or not.
    """
    try:
        # Transform input text
        text_vector = vectorizer.transform([message])

        # Predict spam probability
        spam_probability = model.predict_proba(text_vector)[0][1] * 100

        # Determine spam classification
        is_spam = "Spam" if spam_probability > 50 else "Not Spam"

        return {
            "classification": is_spam,
            "spam_probability": f"{spam_probability:.2f}%"
        }
    except Exception as e:
        return {"error": str(e)}
