*** Settings ***
Documentation		Example test cases using the keyword-driven testing approach
Library		DegreeLibrary.py    
*** Test Cases ***
Degree Change TC_C1
		Degree Change C		20
		Result Should Be	-6.67

Degree Change TC_F1
		Degree Change F		20
		Result Should Be	68

Degree Change TC_C2
		Degree Change C		20
		Result Should Be	-6.67
		

Degree Change TC_C3
		Degree Change F		0
		Result Should Be	32
		
Degree Change TC_C4
		Degree Change C		0
		Result Should Be	-17.78