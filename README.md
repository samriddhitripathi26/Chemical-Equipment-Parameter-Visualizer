🧪 Chemical Equipment Parameter Visualizer-Hybrid Web + Desktop Application
📌 Project Overview
The Chemical Equipment Parameter Visualizer is a hybrid application developed as part of a project under FOSSEE.
It consists of a single Django backend API consumed by:
a Web Application built with React.js
a Desktop Application built with PyQt5

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

✨ Implemented Features
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
🔐 User authentication and role-based access
🕘 Storage and retrieval of previously uploaded datasets
📄 PDF report generation
☁️ Cloud deployment
📊 Advanced analytics and trend detection

📄 Sample CSV Format
Equipment Name,Type,Flowrate,Pressure,Temperature
Pump A,Pump,120,5.6,80
Valve B,Valve,90,3.2,60
Reactor C,Reactor,200,8.1,120

⚙️ Backend Setup (Django)
cd backend
python -m venv venv
source venv/bin/activate        
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

🌐 Web Frontend Setup (React)
cd frontend
npm install
npm start

🖥 Desktop Application Setup (PyQt5)
cd desktopapp
python -m venv venv
source venv/bin/activate        
pip install -r requirements.txt
python main.py

🔗 Backend API Overview
The Django backend exposes REST APIs to:
Accept CSV file uploads
Parse and analyze data using Pandas
Return computed summary statistics
Serve data to both Web and Desktop frontends
