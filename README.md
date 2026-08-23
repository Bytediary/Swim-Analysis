# Swim Performance Analysis

## My Learning Journey (How I Built This)
I am a 12-year-old developer and competitive swimmer. I wanted to see how real-world conditions affect racing times. 

I used AI to help me polish up my goals one by one to get organized with my ideas and help me write parts of this README, but **100% of the debugging, idea, logic design, and problem-solving was done by me.** Every time the code broke—like when I got the `SettingWithCopyWarning` or columns turned into text instead of numbers—I asked the AI to explain the error. Then, I fixed the bugs myself, researched the parameters of the functions I learned, and wrote down exactly what every single function does line-by-line in a physical notebook.

## What the Project Does

This project takes a spreadsheet of swim times and looks for patterns. **Instead of using fake example data, the code was built completely around actual, real-world swim logs so it handles real racing scenarios.** It calculates whether you got faster or slower in a race, and checks if factors like **Championship vs. Invitational meets** or the **outdoor temperature** changed how well you swam.

## Why the Project Is Useful
It is hard to compare different swim events just by looking at seconds. Dropping 2 seconds in a short 50 Free is huge, but dropping 2 seconds in a long 500 Free is very small. 

This project is useful because it turns your time drops into a simple percentage. This lets you compare all of your races fairly and proves exactly what helps you swim faster.

## Key Insights Discovered

When you run this script on your data, it looks at your races from different angles to find things that simple averages completely miss:

* **Averages vs. The Clutch Factor:** A standard statistical test only looks at your *average* time drop. This can look weird if you swam average times in your secondary events at a big meet. This tool fixes that by calculating a **Clutch Win Percentage** to show how *frequently* you actually beat your seed times. This proves if you are good at stepping up under pressure!
* **Weather vs. Pool Lengths:** By automatically breaking your data down by pool types (SCY, SCM, LCM), the script separates your pure swimming from your wall turns. It shows you exactly how much outdoor factors like wind speed and cold weather actually slows you down when you don't have a lot of turns to save you.

## How to Get Started
Follow these simple steps to run the project on your computer:

1. **Install Python Libraries:** Open your terminal and install the tool needed to read spreadsheets:
 ```bash
  pip install pandas scipy statsmodels matplotlib
```
2. **Get Your Spreadsheet:** Download your spreadsheet from Google Sheets as a `.csv` file. 
3. **Name the File:** Name your file exactly `Swim_Data.csv` and put it in the same folder as your Python script.
4. **Run the Code:** Run your Python script to see your swim summaries.

## Where to Get Help
If you get stuck or have questions about how to set up your spreadsheet, you can click the **Issues** tab at the top of this GitHub page and type your question there.

## Who Maintains the Project
This project is built and maintained by me! Anyone is welcome to suggest new ideas or help improve the code.
2. **Get Your Spreadsheet:** Download your spreadsheet from Google Sheets as a `.csv` file. 
3. **Name the File:** Name your file exactly `Swim_Data.csv` and put it in the same folder as your Python script.
4. **Run the Code:** Run your Python script to see your swim summaries.

## Where to Get Help
If you get stuck or have questions about how to set up your spreadsheet, you can click the **Issues** tab at the top of this GitHub page and type your question there.

## Who Maintains the Project
This project is built and maintained by me! Anyone is welcome to suggest new ideas or help improve the code.
