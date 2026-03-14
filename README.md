⚗️ Chemical Equipment Parameter Visualizer

Hybrid Web + Desktop Application for Chemical Data Analysis

The Chemical Equipment Parameter Visualizer is a hybrid application developed as part of a FOSSEE project. It combines a single Django backend API with both web and desktop interfaces to provide powerful visualization and analysis of chemical equipment data.
 
The platform enables users to upload CSV datasets containing equipment parameters such as equipment name, type, flowrate, pressure, and temperature. The backend processes this data and delivers analytical insights, which are visualized through tables and charts across both the web and desktop applications.

This project demonstrates:

Efficient CSV data processing

Backend–frontend API integration

Multi-platform visualization (Web + Desktop)

Practical data analytics implementation

✨ Features
📤 CSV File Upload

Upload CSV files containing chemical equipment parameters.

Supports structured industrial datasets for analysis.

📊 Data Analysis

The backend computes key insights including:

Total equipment count

Average flowrate, pressure, and temperature

Equipment-type distribution statistics

📈 Data Visualization

Web Application: Interactive charts using Chart.js

Desktop Application: Analytical visualizations via Matplotlib

🧾 Tabular Data Display

Structured tables displaying equipment details.

Easy comparison and inspection of parameter values.

🧩 Technology Stack
Layer	Technology
Backend	Django + Django REST Framework
Data Processing	Pandas
Database	SQLite (default Django DB)
Web Frontend	React.js + Chart.js
Desktop Frontend	PyQt5 + Matplotlib
Version Control	Git & GitHub
🚀 Project Architecture

This hybrid application consists of:

Django Backend API

Handles CSV upload

Processes data using Pandas

Returns computed statistics

Web Frontend (React.js)

Interactive data visualization

User-friendly dashboard

Desktop Application (PyQt5)

Local visualization interface

Matplotlib-based charts

🔮 Future Enhancements

Potential improvements include:

User authentication and role-based access

Storage of uploaded datasets

PDF report generation

Cloud deployment integration

Advanced analytics and trend detection

📄 Sample CSV Format
Equipment Name,Type,Flowrate,Pressure,Temperature
Pump A,Pump,120,5.6,80
Valve B,Valve,90,3.2,60
Reactor C,Reactor,200,8.1,120


⚙️ Setup Instructions
Backend Setup (Django)
cd backend
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Web Frontend Setup (React)
cd frontend
npm install
npm start

Desktop Application Setup (PyQt5)
cd desktopapp
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py

🔗 Backend API Overview

The Django backend exposes REST APIs that:

Accept CSV uploads

Parse and analyze data using Pandas

Return summary statistics

Serve processed data to both web and desktop applications
