# show, add, delete, edit, search, exit, dataflow diagram, save to file
import json

from tkinter import *
from tkinter import messagebox

Student = [{"id": 0, "name": "a", "grade": 10, "email": "@"}, 
		   {"id": 1, "name": "c", "grade": 11, "email": "@"},
			{"id": 2, "name": "b", "grade": 10, "email": "@"}]
json_object = json.dumps(Student, indent=4, sort_keys= False) # The json.dumps() function is used to serialize the dictionary into a JSON-formatted string. The indent parameter is set to 4 for better readability, adding indentation to the output.
# If sort_keys is set to False (the default), the keys will appear in the order they were originally present in the dictionary.

window= Tk()
window.eval("tk::PlaceWindow %s center" % window.winfo_toplevel())
window.geometr
window.withdraw()

def update_file():
	with open('C:/IB/Computer Science/DataBase.json', 'w') as f:
		json.dump(Student, f, indent = 4)
		
def show():
	for x in Student:
		print(x)

	
def add():
	new_student = {"id": int(input("id: ")),
				 "name": input("name: "),
				 "grade": input("grade: "),
				 "email": input("email: ")
				 }
	Student.append(new_student)
	update_file()
	
def delete():
	student_ID = int(input("Enter students ID: "))
	
	for i in range (len(Student)):
		if student_ID == Student[i]["id"]:
			Student.pop(i)
			break
		elif student_ID != Student[i]["id"] and i == len(Student) -1:
			messagebox.showerror(title = "Error", message= "Not found")
			
			
	update_file()
	
def edit():
	obj_atr = int(input("Enter the ID of a student to edit: "))
	attribute = str(input("Enter attribute that you want to edit: "))
	edited_atr = input("Eddited: ")
	for i in range (len(Student)):
		print(Student[i]["id"])
		if obj_atr == Student[i]["id"]:
			print("k")
			Student[i][attribute] = edited_atr
			break
		elif obj_atr != Student[i]["id"] and i == len(Student):
			messagebox.showerror(titile = "Error", message= "Not found")
			
	update_file()		
				
	
def search(): 
	student_ID = int(input("Enter the ID of a Student: "))
	for i in range (len(Student)):
		if student_ID == Student[i]["id"]:
			print(Student[i])

def filter_by_grade(): 
	student_grade = int(input("Enter the grade: "))
	for i in range (len(Student)):
		if student_grade == Student[i]["grade"]:
			print(Student[i])

def sort(): 
	sorted_std = sorted(Student, key= lambda x: x['name'])
	for std in sorted_std:
		print(std)

def menu():
	print('''
	   1) show
	   2) add
	   3) delete
	   4) edit
	   5) search 
	   6) filter (by grade)
	   7) sort (by name)
	   8) exit
	   ''')
	choice = int(input())
	return choice


while True:	
	match menu():
		case 1:
			show() 
			# shows all DataBase
		case 2:
			add()
			# adds a Student, appends to the file
		case 3:
			delete()
			# deletes a student by ID, rewrites the file
		case 4:
			edit()
			# changes attributes of Student, rewrites the file
		case 5:
			search()
			# searches by ID, outputs rest attributes 
		case 6:
			filter_by_grade()
			# inputs grade, outputs students 
		case 7:
			sort()
			# sorts by names in alphabetical order
		case 8:
			break
		case _:
			print("Invalid")
