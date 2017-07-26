# Demo_GradientDescent


Implemented a basic code for Gradient Descent as part of Siraj Rawal's course [Intro - The Math of Intelligence](https://www.youtube.com/watch?v=xRJCOz3AfYY)


Code referenced from : https://github.com/llSourcell/Intro_to_the_Math_of_intelligence


## Gradient descent visualization

https://raw.githubusercontent.com/mattnedrich/GradientDescentExample/master/gradient_descent_example.gif

## Dependencies

- numpy

  Use pip to install any dependencies.

## Dataset used

- `data.csv` file of the form :

   x,y

   Example:
   ```
   distance cycled(miles), calories burned(KCal)

   32.502345269453031,	    31.70700584656992
   55.142188413943821,	    78.211518270799232
   ........          ,     .......   
   ```  

## Usage

- Used hardcoded `data.csv` for data.

- To run:

  ```
  $ python3 demo.py

  Starting gradient descent -> initial_b = 0, initial_m = 0, initial_error = 5565.10783448
  Running...
  After 1000 iterations -> final_b = 0.116832206834, final_m = 1.4771976436, final_error = 112.5981953
   ```
