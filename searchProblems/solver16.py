#Given an input board configuration, the state space for this problem can be defined as the set of all possible board combinations that can be obtained by applying the specified actions (i.e., sliding the tiles to the left or right or up or down).
#For this problem, the successor function gives all the possible child states which can be generated by applying the L,R,U,D moves. We've considered the edge weights to be 1 for this problem.
#We've done a modified version of the Manhattan distance as the heuristic. We had tried with the misplaced tiles heuristic, but Manhattan distance gives us the best results in terms of heuristics. This is the admissible heuristic because it gives the lowest estimate to reach the goal.
#We've implemented A* search algorithm with Manhattan distance as heuristic.
#We had faced some issues while finding the admissible heuristic for this problem. We solved it by trial and error. 
#contact details: atremukh@indiana.edu, touahmed@indiana.edu
import sys
import heapq
from copy import deepcopy
input_board=list()
goal_state=[['1','2','3','4'],['5', '6', '7', '8'], ['9','10','11','12'], ['13','14','15','16']]

def draw_board(board):
    print "Draw Board"
    for i in board:
        print '| '+i[0].ljust(2)+' | '+ i[1].ljust(2)+' | '+ i[2].ljust(2)+' | '+ i[3].ljust(2) +' |'
        print '--------------------'

def rotate_row_left(list):
    return list[1:] + list[:1]

def rotate_row_right(list):
    return list[-1:] + list[:-1]

def calculate_heuristics(state):

    misplaced = 0;
    for i in range(4):
        for j in range(4):
            if(state[i][j] != goal_state[i][j]):
                misplaced = misplaced+1
    #print "Inside calculate heuristics.........." + str(misplaced)
    return misplaced


##############################	

def get_goal_coordinates(state):
    goal_i = 0
    goal_j = 0
    for i in range(4):
        for j in range(4):
            if( goal_state[i][j] ==state):
                goal_i = i
                goal_j = j
    return [goal_i,goal_j]

def calc_modulo(val):
    if(val/3 == 0):
        return val%3
    else:
        return val/3




def manhattan_dist(state):
    goal_state_i = 0
    goal_state_j = 0
    manhattan_distance = 0
    for i in range(4):
        for j in range(4):
          #  print state[i][j]
            goal_state_i,goal_state_j = get_goal_coordinates(state[i][j])

            manhattan_distance += calc_modulo(abs(i - goal_state_i)) + calc_modulo(abs(j - goal_state_j))

            #print "Manhattan distance = " + str(manhattan_distance)
    return manhattan_distance


###########################
def create_a_child(parent, action, i):
    child_node=dict()
    #print parent['state']

    child_state=parent['state']
    #draw_board(child_state)
    if action=='L':
        child_state[i-1]=rotate_row_left(child_state[i-1])
    elif action=='R':
        child_state[i-1]=rotate_row_right(child_state[i-1])
    elif action=='U':
        temp=child_state[0][i-1]

        child_state[0][i-1]=child_state[1][i-1]
        child_state[1][i-1]=child_state[2][i-1]
        child_state[2][i-1]=child_state[3][i-1]
        child_state[3][i-1]=temp
    else:
        temp=child_state[3][i-1]
        child_state[3][i-1]=child_state[2][i-1]
        child_state[2][i-1]=child_state[1][i-1]
        child_state[1][i-1]=child_state[0][i-1]
        child_state[0][i-1]=temp
    #draw_board(child_state)
    child_node['state']=child_state
    child_node['parent']=parent
    g_n = parent['path_cost'] + 1
    child_node['path_cost'] = g_n
    h_n = manhattan_dist(child_state)
    child_node['cost']= g_n +h_n

    child_node['heuristics']=h_n#calculate_heuristics(child_state)
    child_node['action']=action+str(i)
    child_node['moves'] = parent['moves'] + ' ' + child_node['action']
    return child_node

def generate_childs(parent):
    child_list=list()
  #  draw_board(goal_state)
    parent=deepcopy(parent)
   # print parent['state']
    for i in range(1,5):
        child_list.append(create_a_child(deepcopy(parent),'L',i))
        child_list.append(create_a_child(deepcopy(parent),'R',i))
        child_list.append(create_a_child(deepcopy(parent),'U',i))
        child_list.append(create_a_child(deepcopy(parent),'D',i))

    #for item in child_list:

        #print 'Action'+item['action']
        #print '.............................'
        #draw_board(item['state'])
        #print item['heuristics']
    #draw_board(goal_state)
    return child_list

def read_file(filename):
    f=open(filename,'r')
    for line in f:
        row =line.strip().split(' ')
        input_board.append(row)

    f.close()
    #print input_board

def check_goal(child_state, goal_state):

    for i in range(4):
        for j in range(4):
            if(child_state[i][j] != goal_state[i][j]):
                return False
    return True




def a_star(input_board):
    init_node=dict()

    g_n = 0
    init_state=deepcopy(input_board[:])
    init_node['state']=init_state
    h_n = manhattan_dist(init_state)#calculate_heuristics(init_state)
    init_node['parent']=None
    init_node['path_cost'] = g_n
    init_node['cost']=g_n + h_n
    init_node['heuristics']=h_n
    init_node['action']=None
    init_node['moves']=''
    
  

    fringe = []

    heapq.heappush(fringe, (init_node['cost'], init_node))

    while (len(fringe) != 0):
        node = heapq.heappop(fringe)
        if(check_goal(init_node['state'],goal_state)):
            return
        children = generate_childs(node[1])
        #print children
        for each_child in children:
            #print each_child['cost']
            #print "heuristics = " + str(each_child['heuristics'])

            if(check_goal(each_child['state'],goal_state)):
                print each_child['moves']
                #print each_child['cost']
                return
            else:
                heapq.heappush(fringe,(each_child['cost'],each_child))











def main(argv):
     if (len(argv) < 1):
        print "Input board filename required"
        return
     else:
        filename=argv[0]
     read_file('board')
     #generate_goal_state()
     #draw_board(input_board)
     print "......................START........................"
     #generate_childs(input_board)
     a_star(deepcopy(input_board))
     #h_n_1 = manhattan_dist(input_board)

if __name__ == "__main__":
    main(sys.argv[1:])