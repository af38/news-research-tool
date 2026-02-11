# Contributing to News Research Tool 🚀

Thank you for your interest in contributing!
We welcome contributions of all kinds — bug fixes, new features, documentation improvements, and suggestions.

Please read this guide before getting started.

---

## 📌 Table of Contents

* Code of Conduct
* How to Contribute
* Development Setup
* Branch Naming Convention
* Commit Message Guidelines
* Pull Request Process
* Reporting Bugs
* Suggesting Features
* Coding Standards
* Need Help?

---

## 🤝 Code of Conduct

Be respectful and constructive in all interactions.

* Be kind and inclusive
* Give helpful feedback
* Respect different experience levels

---

## 🚀 How to Contribute

You can contribute by:

* Fixing bugs
* Adding new features
* Improving documentation
* Writing tests
* Refactoring code
* Reviewing pull requests

If you're new, check issues labeled:

👉 `good first issue`
👉 `help wanted`

---

## 💻 Development Setup

### 1️⃣ Fork the repository

Click **Fork** at the top right of the repo page.

---

### 2️⃣ Clone your fork

```bash
git clone https://github.com/af38/news-research-tool.git
cd news-research-tool
```

---

### 3️⃣ Add upstream remote

```bash
git remote add upstream https://github.com/af38/news-research-tool.git
```

---

### Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Set Up Environment Variables
Create a .env file in the project root:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

## 🎮 Run the project
```bash
streamlit run main.py
```

---

## 🌱 Branch Naming Convention

Create a new branch for every change.

Format:

```
feature/short-description
fix/short-description
docs/short-description
refactor/short-description
test/short-description
```

Examples:

```
feature/add-login-page
fix/navbar-bug
docs/update-readme
```

---

## ✏️ Commit Message Guidelines

Use clear and descriptive commit messages.

Format:

```
type: short description
```

Types:

* feat → new feature
* fix → bug fix
* docs → documentation changes
* style → formatting changes
* refactor → code restructuring
* test → adding tests
* chore → maintenance tasks

Examples:

```
feat: add user authentication
fix: resolve login validation bug
docs: update installation guide
```

---

## 🔀 Pull Request Process

1. Ensure your branch is up to date

```bash
git pull upstream main
```

2. Push your branch

```bash
git push origin your-branch-name
```

3. Open a Pull Request

4. In your PR description include:

* What you changed
* Why you changed it
* Screenshots (if UI change)
* Related issue number (if any)

Example:

```
Closes #12
```

---

## 🐞 Reporting Bugs

Before creating a bug report:

* Check existing issues first

When reporting, include:

* Clear description
* Steps to reproduce
* Expected behavior
* Actual behavior
* Screenshots (if applicable)
* Environment (OS, browser, version)

---

## 💡 Suggesting Features

Feature requests should include:

* Problem description
* Proposed solution
* Use case
* Possible alternatives

---

## 🧑‍💻 Coding Standards

Please follow:

* Clean and readable code
* Meaningful variable names
* Consistent formatting
* Comment complex logic
* Write tests when possible

If applicable:

* Follow project lint rules
* Follow framework best practices

---

## ✅ Before Submitting

Make sure:

✔ Code builds successfully
✔ Tests pass
✔ No lint errors
✔ PR description is complete

---

## 🙋 Need Help?

If you need help:

* Open a discussion
* Comment on an issue

---

## ⭐ Thank You

Your contributions make this project better for everyone.

Happy coding 🎉
