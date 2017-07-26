from numpy import *

# y = mx + b
# m is slope, b is y-intercept
def compute_error_for_line_given_points(b, m, points):
  total_error = 0
  for i in range(0, len(points)):
    x = points[i,0]
    y = points[i,1]
    total_error += (y - (m * x + b)) ** 2
  return total_error / float(len(points))

def step_gradient(b_current, m_current, points, learning_rate):
  b_gradient = 0
  m_gradient = 0

  total_pts = float(len(points))
  for i in range(0, len(points)):
    x = points[i,0]
    y = points[i,1]

    b_gradient = b_gradient - (2/total_pts) * (y - (m_current * x) + b_current)
    m_gradient = m_gradient - (2/total_pts) * x * (y - ((m_current * x) + b_current))

  new_b = b_current - learning_rate * b_gradient
  new_m = m_current - learning_rate * m_gradient
  return [new_b, new_m]

def gradient_descent_runner():
  # Initialize variable for Gradient Descent
  points = genfromtxt("data.csv", delimiter=",")

  learning_rate = 0.0001

  starting_b = 0  # initial y-intercept
  starting_m = 0  # initial slope

  num_iters = 1000

  print "Starting gradient descent -> initial_b = {0}, initial_m = {1}, initial_error = {2}".format(starting_b, starting_m,
                                                                            compute_error_for_line_given_points(
                                                                            starting_b, starting_m, points))
  print "Running..."

  for i in range(num_iters):
    [starting_b, starting_m] = step_gradient(starting_b, starting_m, array(points), learning_rate)

  print "After {0} iterations -> final_b = {1}, final_m = {2}, final_error = {3}".format(num_iters, starting_b, starting_m,
                                                                    compute_error_for_line_given_points(starting_b, starting_m, points))


if __name__ == '__main__':
  gradient_descent_runner()



