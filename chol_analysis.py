def HDL_analysis(HDL_Level):
    if HDL_Level >= 60:
        return "Normal"
    elif 40 <= HDL_Level < 60:
        return "Borderline low"
    else:
        return "Low"


def LDL_analysis(LDL_Level):
    if LDL_Level < 130:
        return "Normal"
    elif 130 <= LDL_Level <= 159:
        return "Borderline High"
    elif 160 <= LDL_Level <= 189:
        return "High"
    else:
        return "Very High"


def new_feature():
    pass


def fever_check(temp_list):
    fever = False
    for temperature in temp_list:
        if temperature > 98.6:
            fever = True
    return fever


def cholesterol_analysis():
    print("cholesterol_analysis")
    HDLinput = input("Enter test result: ")
    test_info = HDLinput.split("=")
    if test_info[0] == "HDL":
        answer = HDL_analysis(int(test_info[1]))
        print("The HDL level is {}".format(answer))
    elif test_info[0] == "LDL":
        answer = LDL_analysis(int(test_info[1]))
        print("Your LDL level is {}".format(answer))


def interface():
    choice = 0
    while choice != "9":
        print("Cholesterol Calculator")
        print("Options: ")
        print(" 1 - HDL Analysis")
        print(" 9 - Quit")
        choice = input("Enter your option: ")
        if choice == '9':
            return
        elif choice == "1":
            cholesterol_analysis()


if __name__ == "__main__":
    interface()
