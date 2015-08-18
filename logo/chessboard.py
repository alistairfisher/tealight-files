from tealight.logo import move,turn

def corner(x):
  move(10)
  turn(90*x)
  move(1)

corner(1)