# 📈 Stock Market Trading Application

A real-time stock trading simulation platform built with Django, featuring live stock prices, portfolio management, and trading capabilities.

## 🎯 Features

-  **72+ Real Stocks** - Live prices from major markets (AAPL, MSFT, GOOGL, TSLA, etc.)
-  **Real-Time Data** - Auto-updating prices every 30 seconds
-  **Portfolio Management** - Track your investments and performance
-  **Watchlist** - Monitor stocks you're interested in
-  **Trading Simulation** - Buy and sell stocks with real market prices
-  **Transaction History** - Complete record of all your trades
-  **Email Notifications** - Get notified about successful trades
-  **Admin Dashboard** - Comprehensive management interface
-  **Responsive Design** - Works on desktop and mobile

## 🚀 Quick Setup & Run

### Prerequisites
- Python 3.11+ installed
- pip (Python package manager)

### Easy Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Create admin user:**
   ```bash
   python manage.py createsuperuser
   ```

4. **Populate with stock data:**
   ```bash
   python manage.py populate_stocks
   ```

5. **Start the application:**
   ```bash
   python manage.py runserver
   ```

That's it! Your application will be running at http://localhost:8000

## 🌐 Access Your Application

After running the server, visit:

- **Main Application**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin
- **API Health Check**: http://localhost:8000/api/health/

### Admin Credentials
Use the superuser credentials you created during setup

## 💼 Using the Application

1. **Register/Login** - Create your trading account
2. **Browse Stocks** - View 72+ available stocks with live prices
3. **Build Watchlist** - Add stocks you want to monitor
4. **Start Trading** - Buy and sell stocks with real market prices
5. **Track Performance** - Monitor your portfolio's growth
6. **View History** - Review all your transactions

## 🏗️ Architecture

```
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
```

## 📊 Available Stocks

### Tech Giants
AAPL, MSFT, GOOGL, AMZN, META, TSLA, NVDA, NFLX

### Financial
JPM, BAC, WFC, GS, MS, V, MA, AXP

### Healthcare
JNJ, PFE, UNH, MRK, ABT, ABBV

### Consumer Goods
KO, PEP, WMT, COST, MCD, NKE

### ETFs
SPY, QQQ, IWM, VTI

And many more! (72+ total stocks)

## 🔧 Development

### Local Development (without Docker)

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Populate stock data
python manage.py populate_stocks

# Start development server
python manage.py runserver
```

### Additional Commands

```bash
# Update stock prices
python manage.py populate_stocks --symbols AAPL MSFT GOOGL

# Create more stocks
python manage.py populate_stocks

# View application logs
python manage.py runserver --verbosity=2

# Run with different port
python manage.py runserver 0.0.0.0:8080
```

## 🔗 API Endpoints

- `/api/stock/<symbol>/price/` - Get real-time stock price
- `/api/watchlist/update-prices/` - Update all watchlist prices
- `/api/health/` - Application health check
- `/api/ready/` - Readiness probe
- `/api/alive/` - Liveness probe

## 🛠️ Tech Stack

- **Backend**: Django 4.2, Python 3.11+
- **Database**: SQLite (simple and fast)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Stock Data**: yfinance, Tiingo API (real-time prices)
- **Caching**: In-memory caching
- **Web Server**: Django development server

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## 🆘 Support

If you encounter any issues:

1. Check if all dependencies are installed: `pip install -r requirements.txt`
2. Ensure database is migrated: `python manage.py migrate`
3. Verify stock data exists: `python manage.py populate_stocks`
4. Check for any error messages in the terminal

---

**Happy Trading! 📈💰**
