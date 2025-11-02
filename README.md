# 🔐 Password Generator

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A versatile and interactive **Password Generator** built in Python that supports multiple types of passwords with customizable options and entropy-based strength evaluation.

Generate:
- **Random Passwords** (fully customizable with digits, letters, and symbols)  
- **Memorable Passwords** (using NLTK Brown corpus or custom word lists)  
- **PIN Codes** (numeric-only passwords)  

---

## 📌 Table of Contents

1. [Features](#🧩-features-✨)
2. [How it Works](#how-it-works-🔍)
3. [Installation and Setup](#installation-and_setup-🛠️)
4. [Example Gameplay](#example_gameplay-🕹️)
5. [File Structure](#file_structure-🗂️)
6. [Teck Stack](#tech_stack-💻)
7. [Future Improvements](#cfuture_improvements-🔮)
8. [Author](#author-👩‍💻)
9. [License](#license-📜)

---

## Features ✨

- **Multiple Password Types:** Random, Memorable, PIN  
- **Random Passwords Customization:**  
  - Include/exclude numbers, symbols, lowercase, uppercase, or both  
  - Entropy calculation for strength feedback  
- **Memorable Passwords:**  
  - NLTK Brown corpus or custom CSV word list  
  - Stopwords removal for meaningful words  
  - Custom separator between words  
  - Symbol substitutions (e.g., `i -> !`, `o -> 0`)  
- **PIN Code Generator:** Simple numeric passwords  
- **Password Strength Feedback:** Weak / Moderate / Strong / Excellent  

## 🧠 Password Types
| Type | Description |
|------|--------------|
| **Random Password** | Fully random with digits, letters, and/or symbols. |
| **Memorable Password** | Based on meaningful words from NLTK corpus (or user CSV). |
| **PIN Code** | Numeric-only password for simple access codes. |
---
## 🚀 How It Works

Briefly explain how your program or app works, e.g.:

- Users can generate memorable or random passwords using different settings.
- Each password can include special characters, separators, and length customization.
- Frequency-based word selection from the NLTK Brown corpus improves natural memorability.
---
## 🧩 Installation and Setup

Follow these steps to install and run the project locally:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/YourUsername/RepositoryName.git

# 2️⃣ Navigate to the project folder
cd RepositoryName

# 3️⃣ Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate   # for macOS/Linux
venv\Scripts\activate      # for Windows

# 4️⃣ Install dependencies
pip install -r requirements.txt

# 5️⃣ Run the Streamlit app (if applicable)
streamlit run app.py
```
## 🕹️ Example Gameplay
You can show an example interaction, like:
```
🔐 Password Generator
---------------------
Enter password type: Memorable
Enter length: 4
Enter separator: -
Your generated password:
Tree-Dream-Candle-River
```
Or include a screenshot / gif (if you have one):
```
![App Screenshot](images/demo.png)
```
## 🗂️ File Structure
```
project-folder/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
└── utils/                # Helper modules (if any)
```
## 💻 Tech Stack
**•	Python 3.10+**
**•	Streamlit —** for web interface
**•	NLTK —** for text corpus and word frequency
**•	Secrets —** for secure random generation

## 🔮 Future Improvements
	•	Add multilingual word lists
	•	Include user customization for symbol sets
	•	Enhance UI styling in Streamlit

## 👩‍💻 Author

Amineh Alimohammadi
💼 🔗 [GitHub Profile](https://github.com/AminehAlm)

## 📜 License

This project is licensed under the MIT License — feel free to use and modify it freely.