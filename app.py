from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/plan_date', methods=['POST'])
def plan_date():
    try:
        # Get user inputs from the form
        city = request.form.get('city')
        date = request.form.get('date')
        duration = request.form.get('duration')
        vibe = request.form.get('vibe')
        budget = request.form.get('budget')

        # Create the prompt for OpenAI
        prompt = f"""Plan a perfect {duration} date in {city} for {date} with a {vibe} vibe and a {budget} budget.

Please structure your response in the following format:

Main Activity
- [Describe the main activity]
- [Include any necessary details like location, timing, etc.]

Dining Option
- [Recommend a restaurant or cafe]
- [Include cuisine type, price range, and any special features]

Backup Plan
- [Suggest an indoor alternative in case of bad weather]
- [Include location and timing]

Cost Breakdown
- [List estimated costs for each component]
- [Include any tips for saving money]

Additional Tips
- [Include any relevant local tips]
- [Add any special considerations for the date]

Please keep the activities appropriate for the {duration} timeframe and ensure they align with the {budget} budget."""

        # Get response from OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert date planner with extensive knowledge of local attractions, restaurants, and activities. You excel at creating unique and memorable experiences based on people's preferences."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        # Extract the response text
        date_plan = response.choices[0].message.content

        # Return the result as JSON
        return jsonify({
            'success': True,
            'date_plan': date_plan
        })

    except Exception as e:
        print("Error in /plan_date:", e)
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 