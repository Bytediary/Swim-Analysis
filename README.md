# Swim Performance Analysis

This project helps you see how different conditions (like weather or meet types) affect your swim times.

## What the Project Does
This project takes a spreadsheet of swim times and looks for patterns. It calculates whether you got faster or slower in a race, and checks if things like **Championship vs. Invitational meets** or the **outdoor temperature** changed how well you swam.

## Why the Project Is Useful
It is hard to compare different swim events just by looking at seconds. Dropping 2 seconds in a short 50 Free is huge, but dropping 2 seconds in a long 500 Free is very small. 

This project is useful because it turns your time drops into a simple percentage. This lets you compare all of your races fairly and proves exactly what helps you swim faster.

## How to Get Started
Follow these simple steps to run the project on your computer:

1. **Install Python Libraries:** Open your terminal and install the tool needed to read spreadsheets:
   ```bash
   pip install pandas scipy statsmodels
   ```
2. **Get Your Spreadsheet:** Download your spreadsheet from Google Sheets as a `.csv` file. 
3. **Name the File:** Name your file exactly `swim_data.csv` and put it in the same folder as your Python script.
4. **Run the Code:** Run your Python script to see your swim summaries.

## Where to Get Help
If you get stuck or have questions about how to set up your spreadsheet, you can click the **Issues** tab at the top of this GitHub page and type your question there.

## Who Maintains the Project
This project is built and maintained by me! Anyone is welcome to suggest new ideas or help improve the code.
