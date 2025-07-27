
# 🏬 Warehouse Inventory Tracker

A simple Django-based web application to manage products, stock transactions, and view real-time inventory.

🔗 **Live Demo:** [warehouse-inventory-tracker.onrender.com](https://warehouse-inventory-tracker.onrender.com)

---

## 🚀 Features

- ✅ Add & manage products
- ✅ Record stock-in and stock-out transactions
- ✅ Track current inventory levels
- ✅ Simple UI for admin users
- ✅ Django Admin Panel for advanced control
- ✅ Hosted on Render

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (default, can be switched to PostgreSQL)
- **Frontend:** HTML, CSS, Bootstrap (basic styling)
- **Hosting:** Render

---

## 📦 Installation (Local Development)

```bash
# Clone the repository
git clone https://github.com/Anish-89/warehouse-inventory-tracker.git
cd warehouse-inventory-tracker

# Create virtual environment
python -m venv env
env\Scripts\activate   # For Windows
# OR
source env/bin/activate   # For macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the server
python manage.py runserver
```

---

## 👤 Create Admin User

```bash
python manage.py createsuperuser
```

Use this account to log in at:  
`http://127.0.0.1:8000/admin` or your deployed admin URL.
<<<<<<< HEAD
Admin Username: Admin
Password : anishjha22
=======

>>>>>>> 79c6a44 (Add project README with live demo link)
---

## 🧪 Sample Use Case

1. Go to **Add Transaction** to record stock-in or stock-out.
2. Use **Manage Products** (via admin panel) to add/edit product info.
3. View **Current Inventory** on the main dashboard.

---

## 🌐 Deployment on Render

### Files Required:
- `requirements.txt`
- `Procfile` → `web: gunicorn config.wsgi`
- `render.yaml` (optional for auto-deploy)

### Common Deploy Steps:
- Push repo to GitHub
- Create new Web Service on Render
- Set Build Command: `pip install -r requirements.txt`
- Set Start Command: `gunicorn config.wsgi`
- Add environment variable: `PYTHON_VERSION=3.x`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Anishkumar Jha**  
[GitHub Profile](https://github.com/Anish-89)
