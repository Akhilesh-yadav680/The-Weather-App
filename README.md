# 🌤️ The Weather App

A simple weather forecasting web application built with **Python** and **Django**.  
This app fetches real-time weather data using the **OpenWeatherMap API** and displays it in a user-friendly web interface.

---

## 🚀 Features

- Search weather by city name
- Displays temperature, weather condition, humidity, and more
- Clean and responsive interface using Django templates
- Uses OpenWeatherMap API for accurate and up-to-date data

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (via Django templates)
- **API**: [OpenWeatherMap](https://openweathermap.org/)
- **Database**: SQLite (default Django DB)

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Akhilesh-yadav680/The-Weather-App.git
cd The-Weather-App
2. Create a Virtual Environment 
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt

4. Add Your API Key
In views.py, replace 'Your API Key' with your actual OpenWeatherMap API key.

Alternatively, use a .env file and load it using python-dotenv.

5. Run the App
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

📁 Project Structure
The-Weather-App/
│
├── main/
│   ├── templates/
│   ├── views.py
│   └── ...
│
├── weather/
│   ├── views.py
│   └── ...
│
├── weather_app/
│   ├── settings.py
│   └── ...
│
├── manage.py
└── requirements.txt
📄 License
This project is open-source and available under the MIT License.

🙋‍♂️ Author
Akhilesh Yadav
GitHub Profile
---

Let me know if you want to add:
- Screenshots or a demo GIF
- Environment variable support (`.env`)
