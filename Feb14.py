#programming Feb 14

def absval(num):
    if num >= 0:
        return num
    return -1 * num

class participant:
    part_id = 0
    name = ""
    country = ""

    def __init__(self, pid, name, country):
        self.part_id = pid
        self.name = name
        self.country = country

    def __str__(self):
        return self.name + "  " + self.country
    
    def input_cid(self):
        mycid = input("Please enter country abbrev: ")
        if mycid in ['BN', 'MM', 'KH', 'ID', 'LA',
                     'MY', 'PH', 'SG', 'TH','VN']:
            self.cid = mycid
        else:
            self.cid = ""

mypart1 = participant(1,"John", "Myanmar")
mypart2 = participant(2,"Mary", "Thailand")
mypart1.input_cid()
mypart2.cid = 'TH'
event_participants = [mypart1, mypart2]
for part in event_participants:
    if part.cid == 'TH':
        print(part)
