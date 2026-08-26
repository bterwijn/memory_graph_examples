import numpy as np
mg.extend_numpy()

moves = 0

def set_up(total,start):
    global moves

    moves = 0
    m = np.empty((3,total+1))
    for i in range(3):
        for j in range(total+1):
            m[i,j] = -1
    for i in range(total):
        m[start,i] = int(total-i-1)

    m_list = [m]
    return m,m_list

def move_disk(total,num,m,move_from,move_to,m_list):
    global moves
    temp =m[move_from,np.where(m[move_from]==-1)[0][0]-1]
    m[move_from,np.where(m[move_from]==-1)[0][0]-1]= -1
    m[move_to,np.where(m[move_to]==-1)[0][0]] = temp
    moves = moves + 1
    m_list.append(m)

def towers_algorithm(total,num,m,start,middle,final,m_list):

    if num == 0:
        return
    else:
        towers_algorithm(total,num-1,m,start,final,middle,m_list)
        move_disk(total,num,m,start,final,m_list)
        towers_algorithm(total,num-1,m,middle,start,final,m_list)
        
total = 3
start = 0
middle = 1
final = 2
m,m_list = set_up(total, 1)
print(f'{m=},\n{m_list=}')
towers_algorithm(total, total, m, start, middle, final, m_list)
