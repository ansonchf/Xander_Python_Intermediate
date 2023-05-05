# Xander_Python_Intermediate

## Weather API APP

A simple Python program that takes a city name as input and retrieves the current weather information using OpenWeatherMap API.

Usage:
1. Run the "Python_API_Request" file in your terminal:
2. Enter a city name when prompted (e.g. "New York, London").
3. The program will retrieve and display the current temperature, humidity, and weather description for the specified city.

Note: If the program fails to retrieve the weather data, an error message will be displayed.

## Regular Expression Pattern Matcher

'This code uses the Python regular expressions module re to match patterns in text strings.
It includes eight different patterns, each with an example string to be matched.
The patterns include matching dates, email addresses, URLs, phone numbers, passwords, and credit card numbers.'

To use the code, simply run the "Regular_expressions" file and observe the output.
If a match is found for a given pattern and text string, the matched portion of the string will be printed.
If no match is found, a message stating that no match was found will be printed instead.

## Student Grades Reader

This program reads a CSV file containing student grades, calculates the average grade for each student, and determines if they pass or fail based on a threshold of 70%.

Usage:

To use this program, simply run the read_grades_file() function in file "Writing Exceptions" with the filename of the CSV file containing the student grades.

The program will print the name of each student, their average grade, and whether they passed or failed.

Exceptions:

This program defines a custom StudentFailException exception which is raised if a student fails. If this exception is raised, the student's pass/fail status will be set to "Fail".

If the CSV file specified in the function call is not found, a FileNotFoundError will be raised and an error message will be printed.
