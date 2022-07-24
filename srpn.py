# To run code copy python SRPN/srpn.py into shell
# To test code copy python mark-code.py into shell

#This is your SRPN file. Make your changes here.

# Initialise empty stack
stack = []

# Create list of valid operators
operators = ["+", "-", "*", "/", "%", "^"]

# Create list of valid letters
letters = ["d", "r"]

# Create list of r numbers
r_list = [1804289383, 846930886, 1681692777, 1714636915, 1957747793, 424238335, 719885386, 1649760492, 596516649, 1189641421, 1025202362, 1350490027, 783368690, 1102520059, 2044897763, 1967513926, 1365180540, 1540383426, 304089172, 1303455736, 35005211, 521595368, 1804289383]

# Initialise counter to track progress through r_list
index = 0

# Create variable for checking for comments
comment = False

# Create empty number string
number_string = ""

# Create variable for checking incorrect use of hash for comment
incorrect_hash = True
        
# Function to test whether input is an integer
def is_integer(element):
    try:
        int(element)
        return True
    except ValueError:
        pass

# Function to test for saturation
def is_saturation(result):
    if result > 2147483647:
        stack.insert(0,2147483647)
    elif result < -2147483647:
        stack.insert(0,-2147483648)
    else:
        stack.insert(0, result)

# Function to add elements to stack or perform operation
def operation(command):
    # Assigning variable index and comment a global variable
    global index
    global comment

    # If not a comment
    if comment == False:
        # Checks if input is a number
        if is_integer(command):
            # Checks is stack has less than 23 elements
            if len(stack) < 23:
              # Checks for octal
                if command[0] == '0' and len(command) > 2:
                    try:
                        # Converts octal to decimal
                        is_saturation(int(command, 8))
                    except:
                        pass

                else:
                    is_saturation(int(command))
            else:
                print("Stack overflow.")
                 
        elif command in operators:
            # Checks if stack contains at least two elements
            if len(stack) >= 2:
                # Remove 2nd element from stack
                n1 = stack.pop(1)
                # Remove 1st element from stack
                n2 = stack.pop(0)

                if command == "+":
                    ans = n1+n2

                elif command == "-":
                    ans = n1-n2

                elif command == "*":
                    ans = n1*n2

                elif command == "/":
                    # Checks if dividing by 0
                    if n2 != 0:
                        ans = n1//n2
                    else:
                        print("Divide by 0.")

                elif command == "%":
                    ans = n1%n2

                elif command == "^":
                    # Checks if power is positive
                    if n2 > 0:
                        ans = n1**n2
                    else:
                        print("Negative power.")
            else:
                print("Stack underflow.")
                return
          
            # Catches divide by 0 and negative power errors 
            try:
                is_saturation(ans)
            except NameError:
                # Re-insert the two numbers back in the stack
                stack.insert(1, n1)
                stack.insert(0, n2)

        elif command == "d":
            if len(stack) == 0:
                print(-2147483648)
            else:
                for num in reversed(stack):
                    print(num)
        
        elif command == "=":
            if len(stack) == 0:
                print("Stack empty.")
            else:
                print(stack[0])

        elif command == "r":
            if len(stack) < 23:
                is_saturation(r_list[index])
                if index == 22:
                    # Reset index
                    index = 1
                else:
                    index += 1

            else:
                print("Stack overflow.")

        elif command == " ":
            pass

        elif comment == True:
            pass

        else:
            if command == "#" and incorrect_hash == False:
                pass
            else:
                print(f"Unrecognised operator or operand \"{command}\".")

def process_command(command):
    global number_string
    global comment
    global incorrect_hash
    start = 0
    neg_num = False

    # Tests for negative numbers
    if command[0] == '-' and neg_num == False:
        start = 1
        number_string += "-"
        neg_num = True

    # Iterate through the command
    for i in range(start,len(command)):
        # Checks for start of a comment
        if command[i] == "#" and comment == False:
            try:
                if command[i+1] == " ":
                    comment = True
                else:
                    incorrect_hash = True
            except:
                incorrect_hash = False
                pass
        
        # Checks for end of a comment
        elif command[i] == "#" and comment == True:
            if command[i-1] == " ":
                incorrect_hash = False
                comment = False

        if is_integer(command[i]):
            # If character is number, add to number string
            number_string += command[i]

        # If character is not a number
        else:
            # If a number already exists in the number string
            if number_string:
                # Process that number
                operation(number_string)
                # Reset number_string
                number_string = ""

            # Process non-numeric character read
            operation(command[i])

    # If whole string is read and only numbers read, process that number
    if number_string:
        operation(number_string)
        number_string = ""

#This is the entry point for the program.
#Do not edit the below
if __name__ == "__main__": 
    while True:
        try:
            cmd = input()
            pc = process_command(cmd)
            if pc != None:
                print(str(pc))
        except:
            exit()
