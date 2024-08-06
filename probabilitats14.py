

two_dice = [[ (i,j) for i in range(1, 7)]for j in range(1,7)]


def show_results(two_dice):
    print ( "      1       2       3       4       5       6   ")
    for r in range(len(two_dice)):
        print (r+1, two_dice[r])
        

show_results(two_dice)