import random
# -*- coding: utf-8 -*-
# tạo bảng
board = []
boards= []  #bảng này để in ra vì join chỉ nối dạng string
for x in range(4):
  board.append(["*"] * 4)
  boards.append(["*"] * 4)
#tạo list random:
ran=[2,4]
# nhập ngẫu nhiên số:
for i in range(4):
    for j in range(4):
        board[i][j] = random.randrange(0,4,2)
        boards[i][j] = str(board[i][j])
print board
def table(b):
    for row in b:
        print " ".join(row)
table(boards)

while 5>0:
    
    act= raw_input("What do you want to do?")
#thao tác gạt sang phải:    
    if act == "d":
        for i in board:
            while i[3] ==0 and (i[2] !=0 or i[1] !=0 or i[0] !=0):   # loại bỏ số không ở giữa
                i[3]=i[2]
                i[2]=i[1]
                i[1]=i[0]
                i[0]=0
            while i[2] ==0 and (i[1] !=0 or i[0] !=0):
                i[2]=i[1]
                i[1]=i[0]
                i[0]=0
            while i[1] ==0 and i[0] !=0:
                i[1]=i[0]
                i[0]=0
#cộng dồn vào            
            if i[3] == i[2]:
                i[3]*=2
                i[2] =0
            if i[2] == i[1]:
                i[2] *=2
                i[1] =0
            if i[1] == i[0]:
                i[1] *=2
                i[0] =0
                
            while i[3] ==0 and (i[2] !=0 or i[1] !=0 or i[0] !=0):   # loại bỏ số không ở giữa một lần nữa
                i[3]=i[2]
                i[2]=i[1]
                i[1]=i[0]
                i[0]=0
            while i[2] ==0 and (i[1] !=0 or i[0] !=0):
                i[2]=i[1]
                i[1]=i[0]
                i[0]=0
            while i[1] ==0 and i[0] !=0:
                i[1]=i[0]
                i[0]=0
        for i in board:
          if min(i) ==0:
              while 0< 5 :          
                  k= random.choice(board)
                  j= random.randrange(0,4)
                  if k[j] != 0:
                      k[j]= k[j]
                  elif k[j] ==0:
                      k[j] = random.choice(ran)
                      break
                      break
            
#đổi dạng int sang string:
        for i in range(4):
            for j in range(4):
                boards[i][j] = str(board[i][j])
        print table(boards)
#thao tác gạt sang trái
    elif act =="a":
        for i in board:
            while i[0] ==0 and (i[2] !=0 or i[1] !=0 or i[3] !=0):   # loại bỏ số không ở giữa
                i[0]=i[1]
                i[1]=i[2]
                i[2]=i[3]
                i[3]=0
            while i[1] ==0 and (i[2] !=0 or i[3] !=0):
                i[1]=i[2]
                i[2]=i[3]
                i[3]=0
            while i[2] ==0 and i[3] !=0:
                i[2]=i[3]
                i[3]=0
#cộng dồn vào            
            if i[0] == i[1]:
                i[0]*=2
                i[1] =0
            if i[1] == i[2]:
                i[1] *=2
                i[2] =0
            if i[2] == i[3]:
                i[2] *=2
                i[3] =0
                
            while i[0] ==0 and (i[2] !=0 or i[1] !=0 or i[3] !=0):   # loại bỏ số không ở giữa
                i[0]=i[1]
                i[1]=i[2]
                i[2]=i[3]
                i[3]=0
            while i[1] ==0 and (i[2] !=0 or i[3] !=0):
                i[1]=i[2]
                i[2]=i[3]
                i[3]=0
            while i[2] ==0 and i[3] !=0:
                i[2]=i[3]
                i[3]=0
        for i in board:
          if min(i) ==0:
              while 0< 5 :          
                  k= random.choice(board)
                  j= random.randrange(0,4)
                  if k[j] != 0:
                      k[j]= k[j]
                  elif k[j] ==0:
                      k[j] = random.choice(ran)
                      break
                      break
#đổi dạng int sang string:
        for i in range(4):
            for j in range(4):
                boards[i][j] = str(board[i][j])
        print table(boards)
#-----------sang trái sang phải thành công--------------------#
    elif act =="s":
      for j in range(4):
        while board[3][j]==0 and ( board[2][j] !=0 or board[1][j] !=0 or board[0][j] !=0):
          board[3][j] = board[2][j]
          board[2][j] = board[1][j]
          board[1][j] = board[0][j]
          board[0][j] = 0
        while board[2][j]==0 and ( board[1][j] !=0 or board[0][j] !=0):
          board[2][j] = board[1][j]
          board[1][j] = board[0][j]
          board[0][j] = 0
        while board[1][j]==0 and board[0][j] !=0:
          board[1][j] = board[0][j]
          board[0][j] = 0
        if board[3][j] == board[2][j]:
          board[3][j] *=2
          board[2][j] =0
        if board[2][j] == board[1][j]:
          board[2][j] *=2
          board[1][j] =0
        if board[1][j] == board[0][j]:
          board[1][j] *=2
          board[0][j] =0
        while board[3][j]==0 and ( board[2][j] !=0 or board[1][j] !=0 or board[0][j] !=0):
          board[3][j] = board[2][j]
          board[2][j] = board[1][j]
          board[1][j] = board[0][j]
          board[0][j] = 0
        while board[2][j]==0 and ( board[1][j] !=0 or board[0][j] !=0):
          board[2][j] = board[1][j]
          board[1][j] = board[0][j]
          board[0][j] = 0
        while board[1][j]==0 and board[0][j] !=0:
          board[1][j] = board[0][j]
          board[0][j] = 0
      for i in board:
          if min(i) ==0:
              while 0< 5 :          
                  k= random.choice(board)
                  j= random.randrange(0,4)
                  if k[j] != 0:
                      k[j]= k[j]
                  elif k[j] ==0:
                      k[j] = random.choice(ran)
                      break
                      break
      for i in range(4):
            for j in range(4):
                boards[i][j] = str(board[i][j])
      print table(boards)
#kéo lên:        
    elif act == "w":
      for j in range(4):
        while board[0][j]==0 and ( board[2][j] !=0 or board[1][j] !=0 or board[3][j] !=0):
          board[0][j] = board[1][j]
          board[1][j] = board[2][j]
          board[2][j] = board[3][j]
          board[3][j] = 0
        while board[1][j]==0 and ( board[2][j] !=0 or board[3][j] !=0):
          board[1][j] = board[2][j]
          board[2][j] = board[3][j]
          board[3][j] = 0
        while board[2][j]==0 and board[3][j] !=0:
          board[2][j] = board[3][j]
          board[3][j] = 0
        if board[0][j] == board[1][j]:
          board[0][j] *=2
          board[1][j] =0
        if board[1][j] == board[2][j]:
          board[1][j] *=2
          board[2][j] =0
        if board[2][j] == board[3][j]:
          board[2][j] *=2
          board[3][j] =0
        while board[0][j]==0 and ( board[2][j] !=0 or board[1][j] !=0 or board[3][j] !=0):
          board[0][j] = board[1][j]
          board[1][j] = board[2][j]
          board[2][j] = board[3][j]
          board[3][j] = 0
        while board[1][j]==0 and ( board[2][j] !=0 or board[3][j] !=0):
          board[1][j] = board[2][j]
          board[2][j] = board[3][j]
          board[3][j] = 0
        while board[2][j]==0 and board[3][j] !=0:
          board[2][j] = board[3][j]
          board[3][j] = 0  
      for i in board:
          if min(i) ==0:
              while 0< 5 :          
                  k= random.choice(board)
                  j= random.randrange(0,4)
                  if k[j] != 0:
                      k[j]= k[j]
                  elif k[j] ==0:
                      k[j] = random.choice(ran)
                      break
                      break
          
      for i in range(4):
            for j in range(4):
                boards[i][j] = str(board[i][j])
      print table(boards)
#hoàn tất các bước di chuyển:    
    
