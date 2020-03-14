# Anthony Tesoriero - Kargo Summer 2020 Software Engineering Internship Assessment
s1 = input("Please input 's1': ")
s2 = input("Please input 's2': ")

if len(s1) != len(s2):  # Check to see if strings are the same length. If not, print False
    print(False)
elif len(set(s1)) != len(s1):  # Check to see if s1 has repeated characters. If so, print False
    print(False)
else:
    print(True)
