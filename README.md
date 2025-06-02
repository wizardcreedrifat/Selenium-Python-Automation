# 🔍 Automate Google Title Fetch Using Selenium (Python)

This Python script automates the Chrome browser to open [Google.com](https://www.google.com), fetches and prints the page title, and then closes the browser — using **Selenium** and **webdriver-manager** for a smooth setup.

---

## ✅ Requirements

1. Install **PyCharm Community Edition**.
2. Create a Python project:  
   `File > New Project`
3. Inside the project, create a file:
   
   **touch main.py**
4. Install Python 3.x (if not already installed).
5. Ensure the latest version of Google Chrome is installed in machine which will be used.

## 📦 Python Packages Used 
Open the terminal and run the following command to install necessary packages:
       
 **pip install selenium webdriver-manager**

If prompted to upgrade pip, run:

**pip install --upgrade pip**

These libraries are essential for automating browser interactions and managing ChromeDriver versions automatically.

## ⚙️ How It Works 
1. Uses webdriver-manager to auto-download the correct version of ChromeDriver.
2. Launches the Chrome browser using Selenium.
3. Opens the Google homepage.
4. Waits 3 seconds to allow the page to fully load.
5. Prints the page title (google) in run prompt.
6. Closes the browser session cleanly.

## ▶️ Running the Script
To run the automation script:
**python main.py**

## ✅Result
Google

## 📁 Project Structure
Selenium-python/


├ main.py         
**Main script that runs the automation**.

├ README.md       
**This File**.

## 📝 Notes
1. Make sure your Chrome browser matches the ChromeDriver version. **webdriver-manager** handles this automatically.
2. This script is ideal for beginners learning Selenium for automation testing.

## 📄 License
```yaml
This project is free to use for educational and personal learning purposes. 
