Time Calculator
Introduction

Time Calculator is a simple web application built with Flask and Pandas. It allows users to upload a CSV file, processes the data to calculate the total time worked per day and per week, and displays the results in a neatly formatted table on the webpage.
Features

    File Upload: Easily upload CSV files through the web interface.
    Data Processing: Calculates total time worked per day and per week.
    Results Display: Displays the processed data in tabular format on the web interface.

Installation
Prerequisites

    Python 3.6 or higher
    Pip package manager

Steps

    Clone the repository:

    sh

git clone https://github.com/Brownster/time_calculator.git
cd flask-csv-processor

Install the required packages:

sh

pip install -r requirements.txt

Run the Flask app:

sh

    python app.py

    Open a web browser and navigate to http://127.0.0.1:5000/ to view the app.

Usage

    Click on the "Upload" button to select a CSV file from your computer. The file should contain at least two columns: u_actual_start for the start date and time_worked for the time worked.

    The application will process the data and display the total time worked per day and per week in tabular format on the webpage.

Contributing

    Fork the repository on GitHub.
    Clone your forked repository to your local machine.
    Create a new branch for your feature or bug fix.
    Make your changes and commit them to your local repository.
    Push your changes to your forked repository on GitHub.
    Create a pull request to merge your changes into the main repository.

License

This project is licensed under the MIT License. See the LICENSE file for details.
