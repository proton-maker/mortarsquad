# Mortar Mil Interpolator

This Python script calculates the mil value for a given target distance using spline interpolation. It's designed to provide more accurate mil adjustments based on a predefined dataset of distances and corresponding mil values, likely derived from game data or ballistic tables.

## Features

* **Spline Interpolation:** Uses `scipy.interpolate.UnivariateSpline` for accurate mil value calculation.
* **Distance Input:** Prompts the user to enter the target distance in meters.
* **Input Validation:** Checks if the user input is a valid number.
* **Clear Output:** Displays the calculated mil value for the given distance.
* **Interactive Loop:** Allows the user to perform multiple calculations until they choose to exit.

## Usage

1.  **Installation**

    * Ensure you have Python 3.x installed.
    * Install the required libraries using pip:

        ```bash
        pip install numpy scipy
        ```

2.  **Running the script**

    * Save the script as a `.py` file (e.g., `mortar_calculator.py`).
    * Open a terminal and navigate to the directory where you saved the file.
    * Execute the script:

        ```bash
        python mortar_calculator.py
        ```

3.  **Input**

    * The script will prompt you to enter the target distance in meters.
    * Enter a numerical value and press Enter.
    * To exit the script, type `exit` and press Enter.

## Code Explanation

* **`interpolate_mil(d_target)`:**
    * Defines two NumPy arrays: `distances` (in meters) and `mil_values` (corresponding mil adjustments).
    * Creates a `UnivariateSpline` object from the `scipy.interpolate` library to perform spline interpolation.  A spline interpolation is used to estimate mil values for distances not explicitly listed in the arrays, providing a smoother and more accurate result than linear interpolation.
    * Returns the interpolated mil value for the given `d_target`.
* **`is_number(input_string)`:**
    * A helper function to validate user input.
    * Tries to convert the `input_string` to a float.
    * Returns `True` if the conversion is successful, `False` otherwise.
* **`main()`:**
    * The main function of the script.
    * Prints a title.
    * Enters a `while` loop to continuously prompt the user for input.
    * Handles user input, including the `exit` command.
    * Validates the user's distance input using `is_number()`.
    * Calls `interpolate_mil()` to calculate the mil value.
    * Prints the result.

## Important Notes

* The accuracy of the calculations depends entirely on the accuracy and completeness of the data in the `distances` and `mil_values` arrays.
* This script is designed for the specific dataset provided within the code.  Changing the data arrays will change the results.
* The script assumes the input distance is in meters.
