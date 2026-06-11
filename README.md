# Rule-Based AI Chatbot

## Project Overview

This is a simple Rule-Based AI Chatbot developed using Python. The chatbot responds to predefined user queries using a dictionary of rules and responses. It demonstrates the fundamentals of conversational AI and rule-based natural language interaction without requiring machine learning models.

This project was developed as part of the DecodeLabs AI Internship Program.

---

## Objectives

* Understand the basics of chatbot development.
* Implement a rule-based conversational system.
* Practice Python programming concepts such as dictionaries, functions, loops, and conditional statements.
* Simulate human-computer interaction through predefined responses.

---

## Features

* Interactive command-line chatbot interface.
* Predefined responses for greetings and common conversations.
* Answers basic questions about Artificial Intelligence and DecodeLabs.
* Provides help and guidance commands.
* Handles unknown inputs gracefully.
* Supports multiple exit commands.

---

## Technologies Used

* Python 3.x
* Dictionaries
* Functions
* Loops
* Conditional Statements

---

## How It Works

The chatbot uses a dictionary named `RESPONSES` that contains predefined user inputs as keys and corresponding replies as values.

### Example

```python
RESPONSES = {
    "hello": "Hello! I'm DecoBot. How can I help you today?",
    "what is ai": "Artificial Intelligence is the simulation of human intelligence by machines."
}
```

When a user enters a message:

1. The input is converted to lowercase.
2. Extra spaces are removed.
3. The chatbot searches for a matching key in the response dictionary.
4. If found, the corresponding response is displayed.
5. Otherwise, a default fallback message is returned.

---

## ▶️ Installation & Usage

### Clone the Repository

```bash
git clone https://github.com/atif929/DecodeLabs-Week1_Project_chatbot.git
```

## 💬 Sample Conversation

```text
==================================================
 Rule-Based AI Chatbot
==================================================

You: hello
Bot: Hello! I'm DecoBot. How can I help you today?

You: what is ai
Bot: Artificial Intelligence is the simulation of human intelligence by machines.

You: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs.

You: exit
Bot: Goodbye!
```

---

## 🔑 Supported Commands

### Greetings

* hello
* hi
* hey

### General Questions

* how are you
* what is your name
* who are you

### AI Related Questions

* what is ai
* what is machine learning
* what is a chatbot
* what is rule based ai

### DecodeLabs Information

* what is decodelabs
* contact

### Utility Commands

* help
* what can you do

### Exit Commands

* exit
* quit
* stop
* close
* q

---

## 📈 Future Improvements

* Add Natural Language Processing (NLP).
* Integrate machine learning-based intent recognition.
* Support voice input and speech output.
* Develop a graphical user interface (GUI).
* Connect with external APIs for dynamic responses.
* Store conversation history.

---

## 📚 Learning Outcomes

Through this project, the following concepts were practiced:

* Python programming fundamentals
* Rule-based Artificial Intelligence
* Dictionary data structures
* User input handling
* Function design
* Command-line application development

---

## 👨‍💻 Author

**Atif Rameez**
Software Engineering Student
Sukkur IBA University

GitHub: https://github.com/929

---

## 📄 License

This project is created for educational and internship purposes under the DecodeLabs AI Internship Program.
