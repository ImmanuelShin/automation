# Lab - Class 19

## Project: Automation

### Immanuel Shin

## Setup

### Clone the Repository
```bash
git clone https://github.com/your-username/automation.git
cd automation
```

### Python Environment Setup

#### Install Python

If Python is not already installed, download and install it from the [official Python website](https://www.python.org/downloads/).

#### Create and Activate a Virtual Environment

```bash
python3 -m venv .venv

source .venv/bin/activate (Linux/Mac)

source .venv/Scripts/activate (Windows)
```

#### Install Requirements
```bash
pip install -r requirements.txt
```

### Run

From the root of the project directory, run ```python main.py```

## Usage

The Automation project provides a menu-driven interface for various file and folder manipulation tasks.

### Menu Options:

1. **Create Folder:**
   - Create a new folder. You will be prompted to enter the folder name.

2. **Handle Deleted User:**
   - Handle a deleted user by moving their documents to a temporary folder. Enter the username of the deleted user.

3. **Sort Documents:**
   - Sort documents based on file types (logs, mail, others) within a user's directory. Enter the username of the user.

4. **Parse Log Files:**
   - Parse log files within a user's directory, logging errors and warnings separately. Enter the username of the user.

5. **Count Specific File Types in a Directory:**
   - Count file types (including folders) within a user's directory. Enter the username of the user.

6. **Exit:**
   - Exit the automation script.

Follow the on-screen prompts to choose a task (1-6) and enter the required information when prompted.

Feel free to explore the functionalities offered by each menu option to efficiently manage files and folders!