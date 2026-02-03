Chemical Equipment Parameter Visualizer
Hybrid Web + Desktop Application
📌 Project Overview

The Chemical Equipment Parameter Visualizer is a hybrid application developed as part of a project under FOSSEE.
It consists of a single Django backend API consumed by:

A Web Application built with React.js

A Desktop Application built with PyQt5

The application allows users to upload a CSV file containing chemical equipment parameters such as equipment name, type, flowrate, pressure, and temperature. The backend processes the uploaded data and provides analytical results, which are visualized through tables and charts in both the web and desktop interfaces.

The project demonstrates effective CSV data handling, backend–frontend API integration, and data visualization across multiple platforms.

🧩 Tech Stack
Layer	Technology
Backend	Django + Django REST Framework
Data Processing	Pandas
Database	SQLite (default Django DB)
Web Frontend	React.js + Chart.js
Desktop Frontend	PyQt5 + Matplotlib
Version Control	Git & GitHub
✅ Implemented Features
📤 CSV File Upload

Upload CSV files containing chemical equipment data

📊 Data Analysis

Total equipment count

Average flowrate, pressure, and temperature

Equipment type-wise distribution

📈 Data Visualization

Interactive charts using Chart.js (Web)

Analytical charts using Matplotlib (Desktop)

🧾 Tabular Data Display

Structured table showing equipment details

🔮 Future Enhancements

User authentication and role-based access

Storage and retrieval of previously uploaded datasets

PDF report generation

Cloud deployment

Advanced analytics and trend detection
