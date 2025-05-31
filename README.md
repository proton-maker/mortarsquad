# Mortar Mil Interpolator for Squad

<p align="center">
  <img src="https://github.com/proton-maker/mortarsquad/blob/main/header.jpg?raw=true" alt="Mortar Calculator Banner" width="600">
</p>

This Python script calculates the mil value for a given target distance using spline interpolation. It is specifically designed to be used with the game **Squad** to provide more accurate mil adjustments for mortar aiming based on the game's ballistic mechanics.

## Features

* **Spline Interpolation:** Uses `scipy.interpolate.UnivariateSpline` for accurate mil value calculation, tailored to Squad's mortar ballistics.
* **Distance Input:** Prompts the user to enter the target distance in meters, the standard unit used in Squad.
* **Input Validation:** Checks if the user input is a valid number to prevent errors.
* **Clear Output:** Displays the calculated mil value for the given distance.
* **Interactive Loop:** Allows the user to perform multiple calculations without restarting the script, useful for adjusting to different targets in Squad.

## Usage

1.  **Installation**

    * Ensure you have Python 3.x installed.
    * Install the required libraries using pip:

        ```bash
        pip install numpy scipy
        ```

2.  **Running the script**

    * Save the script as a `.py` file (e.g., `squad_mortar_calculator.py`).
    * Open a terminal and navigate to the directory where you saved the file.
    * Execute the script:

        ```bash
        python squad_mortar_calculator.py
        ```

3.  **Input**

    * The script will prompt you to enter the target distance in meters. **This distance should be obtained from Squad's in-game rangefinder or map measurements.**
    * Enter a numerical value and press Enter.
    * To exit the script, type `exit` and press Enter.

## Code Explanation

* **`interpolate_mil(d_target)`:**

    * Defines two NumPy arrays: `distances` (in meters) and `mil_values` (corresponding mil adjustments). **These data points are calibrated for Squad's mortar system.**
    * Creates a `UnivariateSpline` object from the `scipy.interpolate` library to perform spline interpolation. This method is used to estimate mil values for distances not explicitly listed in the arrays, providing a smoother and more accurate result than linear interpolation, which is crucial for precision in Squad.
    * Returns the interpolated mil value for the given `d_target`.
* **`is_number(input_string)`:**

    * A helper function to validate user input, ensuring only numerical distances are processed.
    * Tries to convert the `input_string` to a float.
    * Returns `True` if the conversion is successful, `False` otherwise.
* **`main()`:**

    * The main function of the script.
    * Prints a title indicating its purpose for Squad.
    * Enters a `while` loop to continuously prompt the user for input, allowing for multiple calculations in a Squad session.
    * Handles user input, including the `exit` command to terminate the script.
    * Validates the user's distance input using `is_number()` to ensure correct usage.
    * Calls `interpolate_mil()` to calculate the mil value based on the game's specific data.
    * Prints the result, providing the player with the necessary adjustment for their mortar.

## Important Notes

* **Accuracy:** The accuracy of the calculations is *highly dependent* on the accuracy and completeness of the data within the `distances` and `mil_values` arrays. **Ensure these values are up-to-date and specific to the current version of Squad.**
* **Game-Specific Data:** This script is designed for the specific dataset provided within the code, which is tailored to Squad. **Do not use this script with other games without recalibrating the `distances` and `mil_values` arrays.**
* **Distance Units:** The script assumes the input distance is in meters, which is the standard unit used in Squad. **Always use meters for accurate results.**
* **In-Game Factors:** Keep in mind that in-game factors like wind and elevation may also affect mortar accuracy in Squad, and this script does not account for those.
