def haveConflict(event1, event2):
    # if event2[0][:2] <= event2[1][:2] and int(event1[0][3:]) - int(event1[1][3:]) <= int(event2[0][3:]):
    #     return True
    sh1 = int(event1[0][:2]) * 60
    sm1 = int(event1[0][3:])
    eh1 = int(event1[1][:2]) * 60
    em1 = int(event1[1][3:])
    sh2 = int(event2[0][:2]) * 60
    sm2 = int(event2[0][3:])
    eh2 = int(event2[1][:2]) * 60
    em2 = int(event2[1][3:])
    smin1 = sh1 + sm1
    emin1 = eh1 + em1
    smin2 = sh2 + sm2
    emin2 = eh2 + em2

 
    if smin1 <= smin2 <= emin1 or smin1 <= emin2 <= emin1 or\
        smin2 <= smin1 <= emin2 or smin2 <= emin1 <= emin2:
        return True
    
    return False

print(haveConflict(["01:15","02:00"], ["02:00","03:00"]))
print(haveConflict(["01:00","02:00"], ["01:20","03:00"]))
print(haveConflict(["10:00","11:00"], ["14:00","15:00"]))