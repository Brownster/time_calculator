from flask import Flask, request, render_template
import pandas as pd
import io

app = Flask(__name__)

def seconds_to_hours_minutes(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours} hours {minutes} minutes"

@app.route('/', methods=['GET', 'POST'])
def index():
    daily_totals = None
    weekly_totals = None
    
    if request.method == 'POST':
        csv_file = request.files['file']
        if not csv_file.filename.endswith('.csv'):
            return "Please upload a CSV file", 400

        # Read the CSV content with specific encoding and handling bad lines
        try:
            df = pd.read_csv(csv_file, encoding='ISO-8859-1', error_bad_lines=False)
        except Exception as e:
            return str(e), 400

        # Process the CSV data
        df['u_actual_start'] = pd.to_datetime(df['u_actual_start'], errors='coerce', format='%d-%m-%Y %H:%M:%S')
        
        # Weekly Totals
        df['Week'] = df['u_actual_start'].dt.strftime('%U')
        weekly = df.groupby('Week')['time_worked'].sum().reset_index()
        weekly['time_worked'] = weekly['time_worked'].apply(seconds_to_hours_minutes)
        weekly = weekly.sort_values(by='Week', ascending=False)  # Sort by week, descending
        weekly_totals = weekly.to_dict(orient='records')
        
        # Daily Totals
        df['ActualStartDate'] = df['u_actual_start'].dt.date
        daily = df.groupby('ActualStartDate')['time_worked'].sum().reset_index()
        daily['time_worked'] = daily['time_worked'].apply(seconds_to_hours_minutes)
        daily = daily.sort_values(by='ActualStartDate', ascending=False)  # Sort by date, descending
        daily_totals = daily.to_dict(orient='records')

    return render_template('upload.html', weekly_totals=weekly_totals, daily_totals=daily_totals)

if __name__ == '__main__':
    app.run(debug=True)
