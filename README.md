# task-organizer-bot

## Introduction

Task Organizer Bot is a Python-based application designed to help users manage tasks efficiently using state transitions. It ensures proper task state management, error handling, and secure configuration. The bot is designed with modularity and scalability in mind, making it a great starting point for building robust task management solutions.

## Architectural Model:

![architectural_model](https://github.com/user-attachments/assets/5fbead67-9f50-4fc0-a2b3-f5e251fd7ee4)

## Features

- **State Management**: Supports task states (`Created`, `In Progress`, `Completed`, `Archived`) with a proper state transition model.
- **Task Reporting**: Generates task reports in CSV format for easy tracking and analysis.
- **Robust Exception Handling**: Handles both expected and unexpected errors gracefully, logging all events.
- **Secure Configuration**: Uses `.env` files for sensitive credentials or configurations (e.g., API keys).
- **Extensible Design**: Well-structured, modular design for easy customization and scalability.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/task-organizer-bot.git
    cd task-organizer-bot
    ```

2. **Install Dependencies**:
    Ensure you have Python 3.x installed, then install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
    Create a `.env` file in the project directory to securely store configurations:
    ```plaintext
    # Example .env file
    API_KEY=your_api_key_here
    ```

##  Usage

1. **Run the Bot**:
    Execute the bot using the command:
    ```bash
    python task_bot.py
    ```

2. **Add Tasks**:
    Tasks can be added programmatically by modifying the `__main__` block or integrating the bot into an API/UI.

3. **Generate Reports**:
    The bot will generate a `tasks_report.csv` file containing all tasks with their details and current states.

4. **Logging**:
    Logs are stored in the `task_bot.log` file for monitoring the bot's activity.
