"""
This is the test client cli app
"""
import Pyro4

fire = Pyro4.Proxy("PYRONAME:FireAlarm")

print("#### login ####")
email = input("Enter your email : ")
pw = input("Enter the password : ")

fire.login(email,pw)


print("--------")
print("Choices: ")
print("Add Floor: A")
print("Add Room: B")
print("Add Sensor: C")
print("List All data: any\n")

choice = input("Enter choice: ")

if choice == 'A':
    fire.add_or_edit_floor()
elif choice == 'B':
    fire.add_or_edit_floor()
elif choice == 'C':
    fire.add_or_edit_floor()
else:
    print(fire.get_sensors_updates())
