employees = [
    {"name": "Luca", "level": 1, "points": 40},
    {"name": "Marco", "level": 2, "points": 95},
    {"name": "Sofia", "level": 1, "points": 55}
]
#Add points
def add_points(data_list):
    for points in data_list:
        points["points"] += 10
#Up levrl
def upgrade_level(data_list):
    for employee in data_list:
        if employee["points"] >= 60:
            employee["level"] = 2
#show status
def dislay_status(data_list):
    for display in data_list:
        print(f"Name {display['name']} Level {display['level']} Points{display['points']}")

#run 
print ("Before Score")
dislay_status(employees)

print ("Score after getting points")
add_points(employees)
upgrade_level(employees)

print ("Current Score")
dislay_status(employees)


        
        