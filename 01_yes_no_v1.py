show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before 
    show_instructions = input ("Have you played this game before? ") .lower()

    # If they say yes, output 'program continues'
    if show_instructions == "yes" :
        print ("Program continues")

    elif show_instructions == "y" :
        print ("Program continues")

    elif show_instructions == "no":
        print("display instructions")  

    elif show_instructions == "n":
        print("display instructions") 

    # If they say no, output 'display instruction'
    else:
        print ("please answer yes / no")

