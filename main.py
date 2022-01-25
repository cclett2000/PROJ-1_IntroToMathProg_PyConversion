# Charles Lett Jr.
# January 25, 2022
# Desc: Python conversion of my java program that calculates quadratic formulas
#       and returns the root type

###########################################
# FUNCTIONS
def q_calc(list, a, b, c):
    # calculations
    root = b * b - 4 * a * c  # determinate

    # disabled, python doesn't handle numbers that can't be computed
    #pos_formula = (- b + sqrt(root)) / (2 * a)  # root 1
    #neg_formula = (- b - sqrt(root)) / (2 * a)  # root 2

    # debug
    if enable_debug:
        print('Numbers: ' + str(a) + ', ' + str(b) + ', ' + str(c))
        print('Root:', str(root), '\n')

    # data storage
    temp = ['Numbers=' + '['+str(a)+', '+str(b)+', '+str(c)+']', 'Root=' + str(root)]

    # root type check
    if (root < 0): temp.append('Type=No Real Roots')
    elif (root == 0): temp.append('Type=One Real Root')
    elif (root > 0): temp.append('Type=Two Real Roots')

    list.append(temp)  # store in main list

def q_display(list):
    for i in list:
        print(i)

############################################
# MAIN
enable_debug = True
number_storage = [[1, -3, 4],   # EX 1
                  [-4, 12, -9], # EX 2
                  [2, -11, 5]]  # EX 3
data = []   # stores final data

# run num through functions
for elem in number_storage:
    q_calc(data, elem[0], elem[1], elem[2])

q_display(data) # display to user