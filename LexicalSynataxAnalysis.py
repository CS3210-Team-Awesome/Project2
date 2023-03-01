"""
TEAM AWESOM(EST)
02/28/2023

GITHUB LINK: https://github.com/CS3210-Team-Awesome/Project2/tree/main
----------------
Team Members:
----------------
Sarah Barnes (sarahbarnes1994)
Samuel Han (samhanahmas)
Jessica Gardner (babybeans)
Jada Sachetti (jsachetti)
Erika Sadsad (krisellecodes)
Adriana Miller (millerac38)
----------------
PROJECT 2: LEXICAL AND SYNTAX ANALYSIS

Write a program (language of your choice) that takes in a Python program as an input and does the 
following tasks:
"""

# Have use input the file to test
input_file = input("Enter a python file (path) to test: ")
print("You entered: " + input_file)

with open(input_file, encoding="utf8") as file:
    print("Reading file...")
    read = file.readlines()
    #print('test')

    # print(read)
    # TODO 1.) Check to make sure all the indentation in the input program is used correctly. If not, fix it. 

    tabCheck = i = 0 # if val is 0 newline not expected. if val 1 it is
    statement_list = read
    number_of_spaces = 0
    stack = [0]
    conditional_words = ["for", "if", "while", "else", "def", "elif", "try", "except",
                         "for ", "if ", "while ", "else ", "def ", "elif ", "try ", "except "]
    
    # traverse the statement list
    for it in statement_list:
        if it == "\n":
            i += 1
            continue
        string_whithout_whitespace = it.lstrip() # ignore tab before to check statement
        number_of_spaces = len(it) - len(string_whithout_whitespace)

        # if there is a missing, expected indent because of a conditional word
        if tabCheck == 1 or number_of_spaces == 0:
            if not string_whithout_whitespace.startswith('def'):
                if not number_of_spaces == stack[len(stack) - 1]:
                    statement_list[i] = (" " * stack[len(stack) - 1]) + it.lstrip()
                    number_of_spaces = stack[len(stack) - 1]
                tabCheck = 0

        # if there is an indent that is unexpected not after conditional word
        elif number_of_spaces > stack[len(stack) - 1]:
            number_of_spaces = stack[len(stack) - 1]
            statement_list[i] = (" " * stack[len(stack) - 1]) + it.lstrip()

        #checks if there is a conditional word
        for word in conditional_words:
            if string_whithout_whitespace.startswith(word):
                stack.append(number_of_spaces + 4)
                tabCheck = 1
                break
        
        i += 1 #updates counter

    fixed_code = statement_list
    #print(statement_list)

    # TODO 2.) Check to make sure all the function headers are syntactically correct. If not, fix it.

    statement_list_2 = []
    for current_list in fixed_code:
        line = current_list
        if line.lstrip().startswith("def"):
            if not line.startswith("def "):
                fix = line[:3] + " "
                remainder = line[3:].split(" ")
                for char in remainder:
                    fix = fix + char
                    if char.endswith(","):
                        fix = fix + " "
                line = fix

            current_line = ""
            word = ""
            for t in line:
                if t == "(":
                    word = word + t
                    current_line = current_line + word
                    word = ""
                elif t.isspace():
                    current_line = current_line + word + t
                    word = ""
                else:
                    word = word + t

                if line.endswith(word + "\n") and word != "":
                    if word.endswith("):") == False:
                        if word.endswith(")"):
                            word = word[:len(word)] + ":"
                        elif word.endswith(":"):
                            word = word[:len(word) - 1] + "):"

                    current_line += word + "\n"
                    statement_list_2.append(current_line)
        else:
            statement_list_2.append(current_list)
    fixed_code = statement_list_2

    # 3.) Count how many time the keyword “print” is used as keywords in the input program.
    str_file = str(read)
    print_1 = str_file.count("print(\"")
    print_2 = str_file.count("print (\"")
    print_3 = str_file.count("print(f\"")
    print_4 = str_file.count("print( f\"")
    print_5 = str_file.count("print (f\"")
    print_6 = str_file.count("print ( f\"")

    print_1_2 = str_file.count("print(\'")
    print_2_2 = str_file.count("print (\'")
    print_3_2 = str_file.count("print(f\'")
    print_4_2 = str_file.count("print( f\'")
    print_5_2 = str_file.count("print (f\'")
    print_6_2 = str_file.count("print ( f\'")

    total_print_count = (print_1 + print_2 + print_3 + print_4 + print_5 + print_6 + 
                        print_1_2 + print_2_2 + print_3_2 + print_4_2 + print_5_2 + print_6_2)

    print("Total number of 'print' statements: " + str(total_print_count))
    # 4.) Print to a text file the original input program, the updated input program, and the number of time keyword “print” is used.

    """ This segment of code saves a .txt copy of the input file """
    name = str(input_file)
    txt_file = name[:-3]
    #print(txt_file)
    txt_file = txt_file + '.txt'

    with open(txt_file, "w") as file1, open(input_file,'r') as file2:
        # Writes the original code to the new txt file: 
        file1.write("# ORIGINAL CODE:\n")
        for line in file2:
            file1.write(line)
        
        file1.write("\n\n# FIXED CODE: \n")
        for line in fixed_code:
            file1.write(line)

        file1.write("\n\n# Total number of 'print' statements: " + str(total_print_count))
        file1.close

    file.close