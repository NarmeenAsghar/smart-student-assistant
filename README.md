# 📘 Smart Student Assistant 🤖

Welcome to the **Smart Student Assistant**, an interactive chatbot built using **Chainlit**, **OpenRouter**, and **OpenAI-compatible models** like `gpt-4o`.

This assistant is designed to help students with:

* ✅ Quick study tips
* 📝 Summarizing long paragraphs
* 💬 Answering academic queries
* 📚 Encouraging better learning habits

---

## 🚀 Features

* 📘 **Study Tips** – Get motivational hacks using `tip` command.
* 📄 **Smart Summarizer** – Just type `summarize: your paragraph...`.
* 🤖 **AI Chat** – Ask questions from any subject and get detailed, supportive answers.
* 🧠 **Memory Friendly UX** – Starts with a welcome, then guides based on user input.

---

## ⚙️ Tech Stack

* **Python 3.10+**
* **[Chainlit](https://www.chainlit.io/)** for UI interface
* **[OpenRouter](https://openrouter.ai/)** for LLM access
* **OpenAI Python SDK**
* `.env` file for secure API handling

---

## ⚙️ Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/NarmeenAsghar/smart-student-assistant.git
   cd smart-student-assistant
   ```

2. **Create & Activate Virtual Environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` File**

   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key
   BASE_URL=https://openrouter.ai/v1
   MODEL=openrouter/gpt-4o
   ```

5. **Run the App**

   ```bash
   chainlit run main.py
   ```

6. **Chat with Your Assistant!**

   * Say `hi` to get help options.
   * Type `tip` for a study hack.
   * Type `summarize: <your text>` to get summaries.

---

## 🥪 Example Prompts

* `tip`
* `summarize: Artificial intelligence is the simulation of human intelligence...`
* `What is Newton's second law of motion?`
* `Hello`

---

## 💡 Future Enhancements

* Add subject-specific modes (e.g., Math, Physics, CS)
* Note-taking or PDF summarization
* Voice input support
* Local memory for follow-ups
