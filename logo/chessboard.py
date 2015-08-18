from tealight.logo import move,turn

def square(side):
  for i in range (0,3):
     move(side)
     turn(90)

def column():
  for i in range(0,8):
    square(30)
    move(30)
  turn(180)
  move(240)

def chessboard():
  for i in range(0,8):
    column()
    turn(270)
    move(30)
    turn(270)

chessboard()