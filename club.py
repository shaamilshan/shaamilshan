club = {}

def addClub():
    n=int(input("Enter number of members in club"))
    name = input("Enter club name")
    members = set()
    for _ in range(n):
        roll = int(input("Roll No : "))
        name_m = input("Name : ")
        members.add((roll,name_m))
    club[name]= members
    print("Club added")

addClub()