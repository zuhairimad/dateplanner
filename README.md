# Date Planner App

A friendly web application that helps you plan the perfect date using AI-powered recommendations. The app takes into account your city, date, desired vibe, and budget to create a curated list of activities and suggestions.

## Features

- Input city, date, vibe, and budget preferences
- AI-powered date planning using crewAI
- Modern, responsive UI with Tailwind CSS
- Real-time web search for up-to-date recommendations

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd date-planner
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
```bash
python app.py
```
3. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Enter the city where you want to plan your date
2. Select the date
3. Choose the vibe you're going for (romantic, casual, adventurous, cultural, or relaxed)
4. Select your budget range
5. Click "Plan My Date!" and wait for your personalized date plan

## Technologies Used

- Flask
- crewAI
- Tailwind CSS
- OpenAI API
- DuckDuckGo Search API # dateplanner
