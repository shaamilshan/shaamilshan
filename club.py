club = {}

def addClub():
    n=int(input("Enter number of members in club"))
    name = input("Enter club name")
    members = set()
    for _ in range(n):
        roll = int(input("Roll No : "))
        name_m = input("Name : ")
        members.add((roll,name_m))
    club[name] = members
    print("Club added")

def addMember():
    club = input("Enter club name")
    if club not in club:
        print("Club not found")
        return
    roll = int(input("Enter roll num "))
    name_m = input("Enter member name ")
    club[club].add((roll,name_m))
    print("Member added")

def commonMembers():
    
