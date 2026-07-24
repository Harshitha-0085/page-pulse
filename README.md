# 🚀 Page Pulse

Page Pulse is a full-stack web application that analyzes any webpage and provides useful SEO and accessibility insights.

Built as part of the **Digital Heroes Software Development Training Task**.

---

## ✨ Features

- 🌐 Analyze any valid webpage URL
- 📄 Detect page title
- 📝 Extract meta description
- 🔢 Count H1 tags
- 🖼️ Detect images missing alt text
- 📚 Approximate word count
- ⚡ Measure response time
- 🌍 Display HTTP status code
- ❌ Handle invalid URLs and connection errors

---

## 🛠 Tech Stack

### Frontend
- React
- Vite

### Backend
- Flask
- BeautifulSoup
- Requests

### Testing
- Pytest

---

## 📁 Project Structure

```
page-pulse/
│
├── frontend/
├── backend/
│   ├── app.py
│   ├── analyzer.py
│   ├── tests/
│   └── requirements.txt
│
└── README.md
```

---

## 🚀 Run Locally

### Backend

```bash
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🧪 Run Tests

```bash
cd backend
pytest
```

---

## 📡 API Endpoint

### POST `/analyze`

Example request:

```json
{
  "url": "https://example.com"
}
```

---

## 👩‍💻 Author

Harshitha M

---

Built for Digital Heroes Training Task