# Xander_Python_Intermediate

## Weather API APP

A simple Python program that takes a city name as input and retrieves the current weather information using OpenWeatherMap API.

### Usage
1. Run the "Python_API_Request" file in your terminal:
2. Enter a city name when prompted (e.g. "New York, London").
3. The program will retrieve and display the current temperature, humidity, and weather description for the specified city.

Note: If the program fails to retrieve the weather data, an error message will be displayed.

## Regular Expression Pattern Matcher

This code uses the Python regular expressions module re to match patterns in text strings.
It includes eight different patterns, each with an example string to be matched.
The patterns include matching dates, email addresses, URLs, phone numbers, passwords, and credit card numbers.

To use the code, simply run the "Regular_expressions" file and observe the output.
If a match is found for a given pattern and text string, the matched portion of the string will be printed.
If no match is found, a message stating that no match was found will be printed instead.

## Student Grades Reader

This program reads a CSV file containing student grades, calculates the average grade for each student, and determines if they pass or fail based on a threshold of 70%.

### Usage

To use this program, simply run the read_grades_file() function in file "Writing Exceptions" with the filename of the CSV file containing the student grades. The program will print the name of each student, their average grade, and whether they passed or failed.

### Exceptions

This program defines a custom StudentFailException exception which is raised if a student fails. If this exception is raised, the student's pass/fail status will be set to "Fail". If the CSV file specified in the function call is not found, a FileNotFoundError will be raised and an error message will be printed.

## Addition Function Unit Test 
### Function description
The addition function takes in two integers as input and returns their sum. This code contains a simple addition function to calculate the sum of two given integers, and a set of unit tests written using the unittest module to ensure that the function is working correctly.

### Unit tests
The TestAddition class contains three test cases to verify the addition function:

- test_positive: tests whether the function returns the correct sum for two positive integers.
- test_negative: tests whether the function returns the correct sum for two negative integers.
- test_zero: tests whether the function returns the correct sum for two zeros.

All tests use the assertEqual method to compare the expected output with the actual output of the addition function.

## Factorial Function Unit Test 
### Function description
This code contains a function factorial() that calculates the factorial of a given integer. The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, the factorial of 5 is 5 x 4 x 3 x 2 x 1 = 120.

The factorial() function raises a ValueError if a negative integer is provided as input. The function returns 1 if the input integer is 0.

### Unit tests
The TestFactorial class tests the factorial() function with various inputs. The test suite has three test cases:

- test_factorial_of_zero tests if the function returns 1 when input is 0.
- test_factorial_of_positive_integer tests if the function returns the correct value for a positive integer input.
- test_factorial_of_negative_integer tests if the function raises a ValueError when a negative integer input is provided.

To run the test cases, execute the file. The test results will be displayed in the console.