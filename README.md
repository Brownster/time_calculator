# Time Calculator

![image](https://github.com/user-attachments/assets/81e9ebdf-14c2-4bcf-b5e1-634d266473bd)

## Introduction

Time Calculator is a web application built with Flask and Pandas that helps users analyze their working hours. Upload a ServiceNow timesheet CSV file to automatically calculate and visualize total work time per day and per week.

## Features

- **User-Friendly Interface**: Clean, responsive design with helpful tooltips and guidance
- **File Upload**: Easily upload CSV files through the web interface
- **Data Processing**: Calculates total time worked per day and per week
- **Results Display**: Presents processed data in neatly formatted tables
- **Error Handling**: Clear error messages for invalid or improperly formatted files
- **Summary Statistics**: At-a-glance view of total hours, days worked, and weeks logged
- **Docker Support**: Run as a containerized application

## CSV Requirements

The application expects CSV files with:
- `u_actual_start` column in DD-MM-YYYY HH:MM:SS format
- `time_worked` column containing seconds worked

Example format:
```
u_actual_start,time_worked,other_columns,...
01-03-2023 09:00:00,3600,data,...
01-03-2023 14:30:00,5400,data,...
```

## Installation

### Prerequisites

- Python 3.6 or higher
- Pip package manager

### Standard Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Brownster/time_calculator.git
   cd time_calculator
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open a web browser and navigate to `http://127.0.0.1:5000/` to view the app.

### Docker Installation

1. Build the Docker image:
   ```bash
   docker build -t time-calculator .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 time-calculator
   ```

3. Access the application at `http://localhost:5000`

## Usage

1. Open the web application in your browser
2. Export your timesheet data from ServiceNow as a CSV file
3. Click "Upload & Calculate" and select your CSV file
4. View your time summary, including:
   - Total hours worked
   - Summary statistics
   - Daily breakdown of hours
   - Weekly totals

## Contributing

1. Fork the repository on GitHub
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them to your local repository
4. Push your changes to your forked repository on GitHub
5. Create a pull request to merge your changes into the main repository

## License

This project is licensed under the MIT License. See the LICENSE file for details.
