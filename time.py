from flask import Flask, request, render_template
import pandas as pd
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    daily_totals = None
    weekly_totals = None
    
    if request.method == 'POST':
        csv_file = request.files['file']
        if not csv_file.filename.endswith('.csv'):
            return "Please upload a CSV file", 400

        # Read CSV content into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # Process the CSV data as per your original PowerShell script
        df['ActualStartDate'] = pd.to_datetime(df['u_actual_start'], format='%d-%m-%Y').dt.date
        daily_totals = df.groupby('ActualStartDate')['time_worked'].sum().reset_index()

        df['Week'] = pd.to_datetime(df['u_actual_start'], format='%d-%m-%Y').dt.strftime('%U')
        weekly_totals = df.groupby('Week')['time_worked'].sum().reset_index()

    return render_template('upload.html', daily_totals=daily_totals.to_dict(orient='records') if daily_totals is not None else None, weekly_totals=weekly_totals.to_dict(orient='records') if weekly_totals is not None else None)


if __name__ == '__main__':
    app.run(debug=True)
