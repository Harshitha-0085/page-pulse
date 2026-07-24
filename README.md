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

## Design Decisions

### 1. Flask for the Backend

I chose Flask because it is lightweight, easy to develop REST APIs with, and well-suited for small web applications like Page Pulse.

### 2. BeautifulSoup for HTML Parsing

I used BeautifulSoup because it provides a simple and reliable way to parse HTML and extract information such as the page title, meta description, headings, and image attributes.

### 3. Graceful Error Handling

I designed the application to return meaningful JSON error messages instead of crashing when users provide invalid URLs, when a website times out, or when the content is not HTML. This improves reliability and user experience.

---

## AI Usage

I used AI tools to understand concepts, troubleshoot deployment issues, and review my implementation. After using AI suggestions, I implemented, tested, debugged, and deployed the application myself. I also verified the outputs, added unit tests, improved error handling, and ensured the final application met the assignment requirements.

---

## 👩‍💻 Author

Harshitha M

---

Built for Digital Heroes Training Task