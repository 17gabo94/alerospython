# 🐍 Python Console Menu Project

This project is a Python console application that displays an interactive menu with several functionalities.  
Each menu option executes a different module, making the code modular, clear, and easy to maintain.

---

## 🚀 Menu Features

1. **Sum digits** → Calculates the sum of all digits in a given number.  
2. **Password Validator** → Validates passwords according to defined rules.  
3. **Remove duplicates from a list** → Removes duplicate elements from a list.  
4. **Data file extraction** → Extracts and processes data from a file.  
5. **Translation log calculator** → Calculates metrics related to translation logs.  
0. **Exit** → Terminates the program.

---

## 🧰 Project Structure
ALEROSPYTHON/
├── data_file_extraction/
│   ├── data_file_extraction.py
│   ├── data.txt
│   
│
├── password_validator/
│   ├── password_validator.py
│   
│
├── remove_duplicates/
│   ├── remove_duplicates.py
│   
│
├── sum_digits/
│   ├── sum_digits.py
│   
│
├── translation_log_calculator/
│   ├── translation_log_calculator.py
│   
│
├── main.py
├── .gitignore
└── README.md


Each folder contains a Python module with a main function named `execute()` that runs when the console menu calls it.

---

## 🧑‍💻 How to Run the Project in GitHub Codespaces

1. Select the `main` or `master` branch in the repository.  
2. Click on **“<> Code”** and choose **“Create Codespace on main”**.  
3. Install the **Python extension** if it’s not already installed.  
   - Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac).  
   - Search for: `Extensions: Install Extensions`.  
   - Install the **Python** extension by Microsoft.  
4. Open the file `main.py`.  
5. Press the ▶️ **"Run" (Play)** button or run the following command in the terminal:
   ```bash
   python main.py