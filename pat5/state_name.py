print("welcome to the query")
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
CODE_TO_smallNAME = {"qld": "Queensland", "nsw": "New South Wales", "nt": "Northern Territory", "wa": "Western Australia",
                "act": "Australian Capital Territory", "vic": "Victoria", "tas": "Tasmania"}
CODE_TO_endNAME = ["QLD is Queensland", "NSW is New South Wales", "NT is Northern Territory", "WA is Western Australia",
                "ACT is Australian Capital Territory", "VIC is Victoria", "TAS is Tasmania"]
print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "":

    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    elif state_code in CODE_TO_smallNAME:
        print(state_code, "is", CODE_TO_smallNAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
print("If you want to see all of information please enter 1,exist enter 0")
nextone = int(input("Enter your choice: "))
if nextone>0:
    for item in CODE_TO_endNAME:
        print(item)
#state.name