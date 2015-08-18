from tealight.logo import move,turn

def corner(x):
  move(100)
  turn(90*x)
  move(10)

corner(1)