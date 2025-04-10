# Budget Buddy Tracker

A Python-based expense tracking application that helps users log their expenses, manage monthly budgets, and stay on top of their financial goals.

---

## 🔧 Features

- Log daily expenses
- Categorize expenses (Food, Transport, Entertainment, etc.)
- Set monthly budgets for each category
- Get alerts when budget is exceeded or 10% is remaining
- Generate monthly spending reports
- Compare spending vs. budget per category
- Custom alerts and email notifications
- Group expense sharing (like Splitwise)
- Dockerized for easy deployment

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/budget-buddy-tracker.git
cd budget-buddy-tracker
```

### 2. Create a virtual environment and activate it

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate    # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python server.py
```

Visit `http://localhost:5000` in your browser.

---

## 🧪 Testing Steps

1. Log expenses in various categories.
2. Set different monthly budgets.
3. Try exceeding the budget to trigger alerts.
4. Reduce budget to test 10% left warning.
5. Check the monthly report view.
6. Test group sharing feature (if enabled).

---

## 🗃️ SQL / ORM

- The application uses **SQLite** with **SQLAlchemy ORM** for database operations.
- See `models.py` and `db_config.py` for implementation.

---

## 🐳 Docker Setup

### Build Docker image

```bash
docker build -t budget-buddy .
```

### Run Docker container

```bash
docker run -d -p 5000:5000 budget-buddy
```

---

## 👨‍💻 Developed By

**Vaishnavi Gumparthi**

> For internship submission at L7 Informatics
