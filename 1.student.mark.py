print("Number of students: 12" )

d = [ [100001, "Pham Van A", "01/01/2002"],
     [100002, "Pham Van B", "02/02/2002"],
     [100003, "Pham Van C", "03/03/2002"],
     [100004, "Pham Van D", "04/04/2002"],
     [100005, "Pham Van E", "05/05/2002"],
     [100006, "Pham Van F", "06/06/2002"],
     [100007, "Pham Van G", "07/07/2002"],
     [100007, "Pham Van H", "08/08/2002"],
     [100007, "Pham Van I", "09/09/2002"],
     [100007, "Pham Van J", "10/10/2002"],
     [100007, "Pham Van K", "11/11/2002"],
     [100007, "Pham Van L", "12/12/2002"]]
     
print ("{:<8} {:<15} {:<10}".format('ID','Name','DOB'))

for v in d:
    id, name, dob = v
    print ("{:<8} {:<15} {:<10}".format( id, name, dob))

print("Courses: 3")
courses = ['Python Programming', 'Java Programming', 'C++ Programming']
print(courses)
print("Courses Information")
from tabulate import tabulate
data = [ ["ICT1.1", 111001],
         ["ICT2.1", 111002],
         ["ICT3.1", 111003]] 

print (tabulate(data, headers=["Name", "ID"]))


print("Marks:")
from tabulate import tabulate
data = [ ["Pham Van A", 15, 20, 10],
      ["Pham Van B", 10, 18, 13],
      ["Pham Van C", 14, 18, 13],
      ["Pham Van D", 7, 10, 10],
      ["Pham Van E", 18, 18, 13],
      ["Pham Van F", 14, 18,9],
      ["Pham Van G", 14, 18, 13],
      ["Pham Van H", 11, 13, 15],
      ["Pham Van I", 5, 10, 10],
      ["Pham Van J", 0, 20, 20],
      ["Pham Van K", 20, 20, 20],
      ["Pham Van L", 16, 13, 15]] 
      
print (tabulate(data, headers=["Name", "Python Programming", "Java Programming", "C++ Programming"]))

