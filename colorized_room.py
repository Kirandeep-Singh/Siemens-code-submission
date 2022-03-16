'''
Pattern list is hardcoded as of now. We can configure our program to read it from a text file or take it as user input as well.
Logic:
1. First I created an 2D list out of the input pattern.
2. Then we traverse over list in a nested manner.
3. Lets call the layout as set of rows and columns and we start iterating over rows.
4. If there is no space in row, it means its a complete wall. we skip the further iteration.
5. If there is space in row, we need to iterate over all elements of this row.
     i. If element is # we can skip
    ii. If patter in # #, it means it's a door, lets skip this as well.
   iii. If current element is space, element before is # then
        a. if element above it i.e in last row is # then most likely we are in a new room. so we mark it as count
        b. if element above is a " " then we are below door, i.e in a new room,hence set element = count.
        c. otherwise, we are in same room, hence we mark this element as value = previous element.
    iv. If current element is a " " and element before it is not #
        a. if element above and below is # it means its another door, lets skip this.
        b. if element above is not # and before element is not " ", then we take value above. (Here assumption that no narrow passage is there comes into picture)
        c. else the value will be set as same as previous one.
'''

patterns = ['''##########
#   #    #
#   #    #
## #### ##
#        #
#        #
#  #######
#  #  #  #
#        #
##########
''','''##########
#   #    #
#   #    #
## #### ##
#        #
#        #
##########
''', '''##########
#   #    #
#   #    #
## #### ##
#   #    #
#        #
##########''']

# patterns = ['''##########
# #   #    #
# #   #    #
# ## #### ##
# #        #
# #        #
# #  #######
# #  #  #  #
# #        #
# ##########
# ''']

class Colors:
    color0 = '\033[40m'
    color1 = '\033[41m'
    color2 = '\033[42m'
    color3 = '\033[43m'
    color4 = '\033[44m'
    color5 = '\033[45m'
    color6 = '\033[46m'
    color7 = '\033[47m'
    nocolor = '\033[0m'
    map = {0: color0, 2: color1, 3: color2, 4: color3, 7: color4, 5: color5, 6: color6, 1: color7, "#": nocolor}

def room_colorizer(layout):
    height = len(layout)
    width = len(layout[0])

    count = 0
    for i, val in enumerate(layout):
        if " " in val:
            for j, val1 in enumerate(val):
                if val1 == "#":
                    continue
                if val[j - 1] == "#" and val1 == " " and val[j + 1] == "#":
                    # Found a Door, continue dont mark
                    continue
                elif val[j - 1] == "#" and val1 == " ":
                    if layout[i - 1][j] == "#":  # Check element above current element
                        # Found pattern Most Likely a room
                        layout[i][j] = count
                    elif layout[i - 1][j] == " ":  # Check element above current element
                        # Most Likely below a door, hence new room
                        layout[i][j] = count
                    else:
                        layout[i][j] = layout[i - 1][
                            j]  # We are in same room, hence setting value similar to prev element.
                elif val[j - 1] != "#" and val1 == " ":
                    if layout[i - 1][j] == "#" and layout[i + 1][j] == "#":
                        # Found vertical Door Dont mark
                        continue
                    if layout[i - 1][j] != "#" and val[j - 1] == " ":
                        layout[i][j] = layout[i - 1][j]
                    else:
                        layout[i][j] = val[j - 1]
                    if j < width - 1:
                        if val[j + 1] == "#":
                            count += 1

    tmp = []
    for line in layout:
        for elem in line:
            if elem not in (" ", "#") and elem not in tmp:
                tmp.append(elem)
        # print (tmp)
        print(
            "".join([x if x in ("#", " ") else "{} {}".format(Colors.map[tmp.index(x)], Colors.nocolor) for x in line]))

### Let's create a 2D list layout using the given pattern
for pattern in patterns:
    print("Starting New Pattern")
    layoutmap = []
    for line in pattern.split("\n"):
        if line:
            x = [i for i in line]
            layoutmap.append(x)
    room_colorizer(layoutmap)
    print ("\n")






