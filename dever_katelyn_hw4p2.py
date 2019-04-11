# Katelyn Dever HW4 Part 2


def main():
    # not part of the assignment specifically, but I added it for fun to
    # test additional names
    userName = input("Who do you need lines for? ")
    userName = userName.upper()
    userName = userName.strip()
    
    # creates a list for storing the lines
    linesSeq = []
    try:
        # 6.3.2 open and read the lines of of the file
        linesFile = open("lines.txt" ,"r")
        f = linesFile.readlines()
        # 6.3.2 read each line of the linesFile into a list of strings
        for line in f:
            linesSeq.append(line)
        # 6.3.2 close the linesFile
        linesFile.close()

        # 6.3.2 open the script file
        scriptFile = open("script.txt", "r")
        # declare a variable as a string to hold names from script file

        # 6.3.3 matches name to user's input name
        # included are both the professor's and programmer's name for testing
        for line in scriptFile:
            line = line.upper()
            line = line.strip()
            if line == userName:
                userName = line
                print("Found your name! Loading lines..")
                # prints name ": " and one line of lines.txt on each line
                index = 0
                while index < len(linesSeq) - 1:
                    string1 = linesSeq[index]
                    print(userName + ": " + string1)
                    index = index+1
                break
            # prints searching message while not found
            else:
                print("Searching for your name on the list...")
                
        scriptFile.close()
        
        
    # 6.3.2 exception handler if the files can't be found
    except IOError:
        print("Your file was not found, IO Error")
        input("Press <Enter> to exit")
        exit()

main()
