

# 🤖 Agentic AI System with FastAPI

This project is a **multi-agent AI backend** built using **FastAPI**, where each agent has a **clear responsibility** such as weather checking, PDF question answering, meeting scheduling, and general Q&A.

The system demonstrates **agent orchestration**, where one agent can invoke another agent to complete a task.

---

## 🚀 Features

### ✅ Agent 1 – Weather Agent

* Extracts city automatically from user query
* Works for **any city**
* Uses OpenWeather API
* Example:

  ```
  What is the weather in Chennai?
  ```

---

### ✅ Agent 2 – PDF Agent

* Answers questions from uploaded PDF content
* If the answer is **not found in the PDF**, it redirects to **web search**

---

### ✅ Agent 3 – Meeting Agent (Orchestrator)

* Calls **Weather Agent**
* Checks if weather is **good or bad**
* Schedules or postpones meeting based on weather conditions

---

### ✅ Agent 4 – Q&A Agent

* Handles general user questions
* Acts as a fallback conversational agent

---

## 🧠 Agent Workflow

```
User Query
   │
   ├── Weather Request ──▶ Weather Agent
   │
   ├── PDF Question ──▶ PDF Agent ──▶ Web Search (if needed)
   │
   ├── Meeting Request ──▶ Weather Agent ──▶ Meeting Decision
   │
   └── General Question ──▶ QA Agent
```

---

## 🗂 Project Structure

```
agentic_ai/
│
├── app/
│   ├── main.py
│   │
│   ├── agents/
│   │   ├── weather_agent.py
│   │   ├── meeting_agent.py
│   │   ├── pdf_agent.py
│   │   └── qa_agent.py
│   │
│   └── tools/
│       ├── weather_tool.py
│       └── web_search.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
OPENWEATHER_API_KEY=your_openweather_api_key
```

> Get your API key from: [https://openweathermap.org/api](https://openweathermap.org/api)

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/agentic-ai.git
cd agentic-ai
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 API Endpoints

### 🌦 Weather Agent

```http
POST /weather?question=what is the weather in chennai
```

---

### 📅 Meeting Agent

```http
POST /meeting?question=verify weather tomorrow in chennai and schedule a meeting
```

#### Sample Response

```json
{
  "city": "Chennai",
  "temperature": 32,
  "condition": "clear sky",
  "meeting": "Meeting scheduled ✅"
}
```

---

### ❓ Q&A Agent

```http
POST /qa?question=What is FastAPI?
```

---

## 🧠 Technologies Used

* **Python 3.11**
* **FastAPI**
* **Uvicorn**
* **OpenWeather API**
* **Agent-based architecture**  *
