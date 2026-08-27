# RULES
# You have to move all disks as the original order (biggest to smallest) to the end pole, using start pole, middle pole and end pole. 
# You can move only one disk at a time 
# You cannot place a lager disk on top of a smaller one

# NOTES
# recursion
# the biggest disk is the bottom one eg. num_of_disks
# the position of a disk is number_of_disks - ?


def tower(num_of_disks, start_pole, end_pole, middle_pole):
    if num_of_disks == 1: # base case 
        print("Move %i from pole %s to pole %s" %(num_of_disks, start_pole, end_pole))

    else:
        tower(num_of_disks -1 , start_pole, middle_pole, end_pole)
        print("Move %i from pole %s to pole %s" %(num_of_disks, start_pole, end_pole))
        tower(num_of_disks -1, middle_pole, end_pole, start_pole)

tower(3,"A", "B", "C")