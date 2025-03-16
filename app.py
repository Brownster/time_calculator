from flask import Flask, request, render_template, flash
import pandas as pd
import io
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev_key_for_flashing_messages')

def seconds_to_hours_minutes(seconds):
    """Convert seconds to a formatted hours and minutes string."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours} hours {minutes} minutes"

@app.route('/', methods=['GET', 'POST'])
def index():
    daily_totals = None
    weekly_totals = None
    error_message = None
    
    if request.method == 'POST':
        # Check if file was provided
        if 'file' not in request.files:
            error_message = "No file selected. Please choose a CSV file to upload."
            return render_template('upload.html', error_message=error_message)
            
        csv_file = request.files['file']
        
        # Check if filename is empty
        if csv_file.filename == '':
            error_message = "No file selected. Please choose a CSV file to upload."
            return render_template('upload.html', error_message=error_message)
            
        # Check file extension
        if not csv_file.filename.endswith('.csv'):
            error_message = "Invalid file format. Please upload a CSV file."
            return render_template('upload.html', error_message=error_message)

        # Read the CSV content with specific encoding and handling bad lines
        try:
            df = pd.read_csv(csv_file, encoding='ISO-8859-1', on_bad_lines='skip')
        except Exception as e:
            error_message = f"Error reading CSV file: {str(e)}"
            return render_template('upload.html', error_message=error_message)

        # Check for required columns
        required_columns = ['u_actual_start', 'time_worked']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            error_message = f"Missing required columns: {', '.join(missing_columns)}. Please ensure your CSV has the correct format."
            return render_template('upload.html', error_message=error_message)

        try:
            # Process the CSV data
            df['u_actual_start'] = pd.to_datetime(df['u_actual_start'], errors='coerce', format='%d-%m-%Y %H:%M:%S')
            
            # Check if any dates were successfully parsed
            if df['u_actual_start'].isna().all():
                error_message = "No valid dates found. Please ensure dates are in DD-MM-YYYY HH:MM:SS format."
                return render_template('upload.html', error_message=error_message)
            
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
            
            # Add summary statistics
            total_days = len(daily)
            total_weeks = len(weekly)
            total_seconds = df['time_worked'].sum()
            total_hours = total_seconds // 3600
            total_minutes = (total_seconds % 3600) // 60
            
            summary = {
                'total_days': total_days,
                'total_weeks': total_weeks,
                'total_hours': total_hours,
                'total_minutes': total_minutes
            }
            
        except Exception as e:
            error_message = f"Error processing data: {str(e)}"
            return render_template('upload.html', error_message=error_message)

    return render_template(
        'upload.html', 
        weekly_totals=weekly_totals, 
        daily_totals=daily_totals,
        summary=summary if 'summary' in locals() else None,
        error_message=error_message
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5002)), debug=True)
