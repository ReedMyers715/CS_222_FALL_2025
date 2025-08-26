def Main():
    current_Tuition = 8000

    for i in range(5):
        tuition_increase = current_Tuition * 0.03
        new_Tuition = current_Tuition + tuition_increase
        print("Tuition after 5 years would be $" + str(new_Tuition))

Main()