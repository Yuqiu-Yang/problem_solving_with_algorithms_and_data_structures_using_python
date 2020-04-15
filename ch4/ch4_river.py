

def river(ML,CL,MR,CR, B_pos, visit_list):
    if (MR == 3) and (CR == 3):
        visit_list[ML][CL][B_pos] = True
        if B_pos == 0:
            B_pos_string = "Left"
        else:
            B_pos_string = "Right"
        print(f"\tOn the left side we have {ML} missionaries, and {CL} cannibals\n \
                On the right side we have {MR} missionaries, and {CR} cannibals\n \
                The boat is on the {B_pos_string}")
        return True
    elif (((ML != 0) and (CL > ML))) or \
        (((MR != 0) and (CR > MR))):
        #print(f"Fail {ML}{CL}{MR}{CR}{B_pos}")
        visit_list[ML][CL][B_pos] = True
        return False
    else:
        if visit_list[ML][CL][B_pos] == False:
            visit_list[ML][CL][B_pos] = True
            if B_pos == 0:
                s1 = False
                s2 = False
                s3 = False
                s4 = False
                s5 = False
                if (ML >= 1):
                    s1 = river(ML - 1, CL, MR + 1 ,CR, 1, visit_list)
                found = s1 or s2 or s3 or s4 or s5
                if (CL >= 1) and not found:
                    s2 = river(ML, CL - 1, MR ,CR + 1, 1, visit_list)
                found = s1 or s2 or s3 or s4 or s5
                if (ML >= 1) and (CL >= 1) and not found:
                    s3 = river(ML - 1, CL - 1, MR + 1 ,CR + 1, 1, visit_list)
                found = s1 or s2 or s3 or s4 or s5
                if (ML >= 2) and not found:
                    s4 = river(ML - 2, CL, MR + 2 ,CR, 1, visit_list)
                found = s1 or s2 or s3 or s4 or s5
                if (CL >= 2) and not found:
                    s5 = river(ML, CL - 2, MR ,CR + 2, 1, visit_list)

                found = s1 or s2 or s3 or s4 or s5

                if found:
                    if B_pos == 0:
                        B_pos_string = "Left"
                    else:
                        B_pos_string = "Right"
                    print(f"\tOn the left side we have {ML} missionaries, and {CL} cannibals\n \
                            On the right side we have {MR} missionaries, and {CR} cannibals\n \
                            The boat is on the {B_pos_string}")
                return found
            else:
                s1 = False
                s2 = False
                s3 = False
                s4 = False
                s5 = False
                if MR >= 1:
                    s1 = river(ML + 1, CL, MR - 1 ,CR, 0, visit_list)
                found = s1 or s2 or s3 or s4 or s5
                if (CR >= 1) and not found:
                    s2 = river(ML, CL + 1, MR ,CR - 1, 0, visit_list)
                found = s1 or s2 or s3 or s4 or s5
                if (MR >= 1) and (CR >= 1) and not found:
                    s3 = river(ML + 1, CL + 1, MR - 1 ,CR - 1, 0, visit_list)
                found = s1 or s2 or s3 or s4 or s5
                if (MR >= 2) and not found:
                    s4 = river(ML + 2, CL, MR - 2 ,CR, 0, visit_list)
                found = s1 or s2 or s3 or s4 or s5
                if (CR >= 2) and not found:
                    s5 = river(ML, CL + 2, MR ,CR - 2, 0, visit_list)
                found = s1 or s2 or s3 or s4 or s5
                if found:
                    if B_pos == 0:
                        B_pos_string = "Left"
                    else:
                        B_pos_string = "Right"
                    print(f"\tOn the left side we have {ML} missionaries, and {CL} cannibals\n \
                            On the right side we have {MR} missionaries, and {CR} cannibals\n \
                            The boat is on the {B_pos_string}")
                return found

        else:
            return False

ML = 3
CL = 3
MR = 0
CR = 0

visit_list = []
for i in range(ML + 1):
    temp = [False] * (CL + 1)
    visit_list.append(temp)
    for j in range(CL + 1):
        temp = [False] * 2
        visit_list[i][j] = temp

river(ML, CL, MR, CR,0, visit_list)
