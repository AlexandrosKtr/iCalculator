# iCalculator
#### Video Demo: https://youtu.be/7A4tRtKsLQw

## Overview

This is a simple graphical calculator application, built using Pythons's **tkinter** library, mimicking the IOS calculator and its features. The calculator supports basic arithmetic operations such as addition, subtraction, multiplication and division, along some additional features like percentage calculation and toggling between positive and negative numbers.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Percentage calculation
- Toggle between positive and negative numbers
- Clear and clear all functionality
- Graphical interface that mimics the IOS calculator

## Requirements

- Python 3.x
- **tkinter** library

## Installation

1. Ensure you have Python 3.x installed on your system. You can download it from the [official Python website](https://www.python.org/).

2. Clone this repository or download the **iCalculator.py** file on your local machine.

## Usage

1. Navigate to the directory containing the **iCalculator.py** file in your terminal or command prompt.

2. Run the calculator application using the following command:

    python iCalculator.py

3. The calculator window will appear. Use the buttons to perform your desired calculations.

## Code Structure

- **main()**: Initializes and starts the calculator application.
- **Calculator** class: Defines the main calculator logic and GUI components.
    - **__init__()**: Initializes the calculator, creating the root window, **entry** widget and buttons.

### Functions

- **create_root()**: Creates the main application window.
- **create_entry(root)**: Creates the **entry** widget for calculator display, using the provided root.
- **create_buttons(calculator)**: Creates and configures all the buttons for the provided calculator object.
- Button-specific functions that define the behavior of indivisual buttons, on the calculator object:

    - **button_num(calculator, num)**: Clears the **entry** widget and inserts the number **num** into it if **num** is the first number after an operation or after beginning the  application. If not the number **num** is added at the end of the **entry** widget. If an operator is already chosen, saves the number inputed before the operator to a temporary variable **temp**.
    - **button_comma(calculator)**: Inserts a comma at the end of the **entry** widget if one is not already present on the display.
    - **button_clear(calculator)**: Clears the **entry** widget and allows the all clear button to be pressed.
    - **button_clear_all(calculator)**: Clears everything on the calculator, including: 
        - **entry**
        - **temp** variable
        - **operator** variable
        - Resets **new** variable to True.
    - **button_equal(calculator)**: Completes the operation between the numbers in the **entry** widget and the **temp** variable, using the **operator** variable, and the result is displayed in **entry**. If the **temp** variable is empty, the number on the **entry** widget is copied in **temp** and then the operation is completed using the chosen operator.
    - **button_operator(calculator, op)**: Updates the **operator** variable to the **op** variable provided. If **operator** is not empty, completes the operation and then updates **operator** to **op**.
    - **button_percentage(calculator)**: Divides the number on the **entry** widget by 100.
    - **button negative(calculator)**: Inserts a "-" at the start of the **entry** widget, or removes it if one already exists.
- **button_toggle(calculator, operator="")**: Changes the colours of the chosen operator's button.

## Customization

- You can modify the appearance of the calculator by changing the button styles, colors, and fonts within the **create_buttons** function.
- Additional functionality can be added by defining new button-specific functions and adding corresponding buttons in the **create_buttons** function.

## Testing

A **test_iCalculator.py** file is included to test the core functionality of the **iCalculator.py** application. This test suite ensures that all calculator operations perform correctly.

### Running Tests 

1. Ensure you have **pytest** installed. If notn install it using the following command:

    pip install pytest

2. Run the tests using the following command:

    pytest test_iCalculator.py

3. The test results will be displayed in the terminal, indicating whether the functions in **iCalculator.py** are working as expected.

### Test Structure

- The tests are organized to cover various functionalities of the calculator, including:
    - Basic arithmetic operations
    - Special functions like percentage and negative toggling