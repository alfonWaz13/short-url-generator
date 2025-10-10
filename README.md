# ✂️ Short URL Generator 🚀

Welcome to **Short URL Generator**, an open-source project designed to help you master modern web development tools and workflows! 🎉

## 🧑‍💻 About This Project

This repository is a **learning playground** for:
- 🐍 **Django** — Web framework for rapid development
- 📦 **Django ORM** — Powerful database management
- 🤖 **GitHub Actions** — CI/CD automation
- ☁️ **AWS Deployment** — Cloud hosting and scaling

> **Note:**  
> The Python code and business logic (use cases, URL shortening) are intentionally **basic and collateral**. While the code works, refining it isn't the primary goal — the main focus is on practicing infrastructure and workflow skills!

## ✨ Features

- 🔗 Shorten long URLs with a simple web interface
- 🗂️ Store and retrieve URLs using Django ORM
- 🛠️ Automated tests and deployments via GitHub Actions
- 🌍 Deployable on AWS for real-world experience

## 🚦 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/alfonWaz13/short-url-generator.git
   ```
2. **Install dependencies**
   ```bash
   uv sync
   source .venv/bin/activate
   ```
3. **Run project**
    - **Run locally with django runserver**:
   
    This will start a containerized environment using Docker Compose with the database and will apply the migrations.
   ```bash
   make run-local
   ```
   - **Run locally with gunicorn**:
   
   This command is designed to run in a production-like environment using Gunicorn as the application server. It assumes that you have a PostgreSQL database running and accessible with the specified environment variables, but it can be run also locally. In order to make it work, you need to run the database first using:
   ```bash
    make run-local-db
    ```
    After that, you can run the Gunicorn application server using:
    ```bash
    make run-production
    ```

## 🛠️ Tech Stack

- Django & Django ORM
- GitHub Actions (CI/CD)
- AWS (Deployment)
- Python (Basic use cases)

## 🌱 Purpose

This project is all about **growth, experimentation, and hands-on learning** with modern development tools. The URL shortening logic is simple by design — focus your energy on the frameworks, workflows, and cloud deployment!

## 🤝 Contributing

Contributions are welcome! Feel free to fork, open issues, or submit pull requests if you'd like to help improve the infrastructure or share deployment tips.
