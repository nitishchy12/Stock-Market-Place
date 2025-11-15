📈 Stock Market Trading Application

A real-time stock trading simulation platform built with Django, featuring live stock prices, portfolio management, and trading capabilities.

🎯 Features

72+ Real Stocks - Live prices from major markets (AAPL, MSFT, GOOGL, TSLA, etc.)

Real-Time Data - Auto-updating prices every 30 seconds

Portfolio Management - Track your investments and performance

Watchlist - Monitor stocks you're interested in

Trading Simulation - Buy and sell stocks with real market prices

Transaction History - Complete record of all your trades

Email Notifications - Get notified about successful trades

Admin Dashboard - Comprehensive management interface

Responsive Design - Works on desktop and mobile

🚀 Quick Setup & Run
Prerequisites

Python 3.11+ installed

pip (Python package manager)

Easy Setup

Install dependencies:

pip install -r requirements.txt


Run database migrations:
python manage.py migrate


Create admin user:
python manage.py createsuperuser


Populate with stock data:
python manage.py populate_stocks


Start the application:
python manage.py runserver

Your application will be live at http://localhost:8000

🌐 Access Your Application
Main Application → http://localhost:8000
Admin Panel → http://localhost:8000/admin
API Health Check → http://localhost:8000/api/health/

✔ Use the superuser credentials created earlier.

💼 Using the Application
Register/Login
Browse stocks
Add stocks to watchlist
Perform simulated trades
Track your portfolio
Check transaction history

🏗️ Architecture
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Django App    │    │   Stock APIs    │
│   (HTML/CSS/JS) │◄──►│   (Python)      │◄──►│   (yfinance)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │   Database      │
                       │   (SQLite/PG)   │
                       └─────────────────┘

📊 Available Stocks
Tech: AAPL, MSFT, GOOGL, AMZN, META, TSLA, NVDA, NFLX
Finance: JPM, BAC, WFC, GS, MS, V, MA, AXP
Healthcare: JNJ, PFE, UNH, MRK, ABT, ABBV
Consumer Goods: KO, PEP, WMT, COST, MCD, NKE
ETFs: SPY, QQQ, IWM, VTI

Total 72+ real market stocks

🔧 Development
Local Development (without Docker)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py populate_stocks
python manage.py runserver

Additional Commands
python manage.py populate_stocks --symbols AAPL MSFT GOOGL
python manage.py runserver --verbosity=2
python manage.py runserver 0.0.0.0:8080

🔗 API Endpoints

/api/stock/<symbol>/price/

/api/watchlist/update-prices/

/api/health/

/api/ready/

/api/alive/

🛠️ Tech Stack

Backend: Django 4.2

Language: Python 3.11+

Frontend: HTML, CSS, JavaScript, Bootstrap

Database: SQLite

Stock Data: yfinance

Caching: In-memory

📝 License

This project is open source and available under the MIT License.

🤝 Contributing

Fork

Create feature branch

Commit changes

Submit PR

🆘 Support

If you face issues:

pip install -r requirements.txt

python manage.py migrate

python manage.py populate_stocks

Check terminal logs

⚙️ DevOps Integration (Docker + Ansible + Nagios + Terraform)

This project includes a full DevOps setup inside the infra/ directory.

🐳 Docker + Ansible Cluster
Location: infra/ansible
Spin up Master & Nodes
docker compose up -d

Containers created:
ansible-master
ansible-node1
ansible-node2

Run Playbook
docker exec -it ansible-master bash
cd /home/ansible/ansible-work
ansible-playbook hello-world.yml

📊 Nagios Monitoring (Docker)
Location: infra/nagios
Start Monitoring System
docker compose up -d
Access Nagios Web UI
👉 http://localhost:8080

Login:
Username: nagiosadmin
Password: nagios
Monitors:
CPU
Memory
Disk
HTTP status
Ping

🌍 Terraform (Infrastructure as Code)
Location: infra/terraform
Initialize & Apply
terraform init
terraform apply -auto-approve

Creates file:
project_output.txt

Happy Trading! 📈💰