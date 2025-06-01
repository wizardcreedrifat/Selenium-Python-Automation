# Goggle title fetcher using selenium

This Python script launches a Chrome browser, navigates to [Google.com](https://www.google.com), prints the page title, and then closes the browser.

## Requirements

1. Install the Pycham Community Edition.
2. Create a python project from File --> New Project.
3. In the project create a file main.py by opening the terminal and put the command --> **touch main.py**.
4. Python3 install (python 3.x) , Google Chrome (Latest Version).

### Python Packages Used

1. Again in the terminal put in the command line ( **pip install selenium webdriver-manager** ) this is the Python libraries essential for automation testing with Selenium.
2. Then will be asked for upgrading so the command will be **pip install --upgrade pip**.

### How it Works 

1. Uses webdriver-manager to automatically download and configure the correct version of ChromeDriver.
2. Launches the Chrome browser via Selenium.
3. Opens the Google Homepage.
4. Waits 3 seconds for the page to load.
5. Prints the title of the page.
6. Closes the browser.
