# Premium Django Weather App

A beautiful, fully-responsive Django web application that provides real-time weather data and dynamic city information. Designed with a modern "glassmorphism" aesthetic, it looks stunning on both desktop and mobile devices.

## Features

- 🌤️ **Real-time Weather Data**: Uses the OpenWeatherMap API to fetch accurate, metric temperature, humidity, wind speed, pressure, and weather descriptions.
- 📖 **Dynamic Wikipedia Integration**: Automatically retrieves and displays a summary of the searched city using the Wikipedia API.
- 💎 **Premium UI/UX**: Built with modern CSS featuring a glassmorphism design, vibrant gradients, and smooth animations.
- 📱 **Responsive Layout**: Adjusts perfectly on mobile, tablet, and desktop screens.
- 🛡️ **Robust Error Handling**: Gracefully handles invalid city names or failed API connections and displays a user-friendly error UI.
- 💰 **Monetization Ready**: Pre-built placeholders seamlessly integrated into the design for easy drop-in of Google AdSense scripts.

## Screenshots

*(You can add screenshots here later)*

## Technologies Used

- **Backend**: Python, Django, Requests
- **Frontend**: HTML5, Vanilla CSS (Glassmorphism design), Google Fonts (Outfit), FontAwesome (Icons)
- **APIs**:
  - [OpenWeatherMap API](https://openweathermap.org/api) (Weather data)
  - [Wikipedia REST API](https://en.wikipedia.org/api/rest_v1/) (City summaries)

## Getting Started

### Prerequisites

- Python 3.8+
- Django 5.x

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mallesh-1124/weatherapp.git
   cd weatherapp
   ```

2. **Install dependencies:**
   Make sure to install the required Python packages (e.g., `requests`, `django`).
   ```bash
   pip install django requests
   ```

3. **Run the server:**
   ```bash
   python manage.py runserver
   ```

4. **Open in Browser:**
   Go to `http://127.0.0.1:8000/` and search for any city!

## Monetization Setup

If you want to earn with Google AdSense, the app is ready for it. Open `weather/templates/weather.html` and look for the `adsense-container` divs. Replace the placeholder content with your actual Google AdSense `<script>` and `<ins>` tags.

## License

This project is open-source and available under the MIT License.
