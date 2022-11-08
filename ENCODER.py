#Christopher Overcash   800939915#
import sys

###INITIALIZE COMMON VARIABLES###
table = [] #Initializes the table
string = "" #string is NULL
compressed = [] #compressed data array
inputFileCommandLine = sys.argv[1] #Sets variable equal to input text file
MAX_TABLE_SIZE = 2 ** int(sys.argv[2]) #sets the max table size to be 2^(specified bit length)
finalCode = "" #final code is Null (will be used to encode and print and export)

###Read the Input###
inputFile = open(inputFileCommandLine, 'r') #opens the input text file
input = inputFile.read() #reads and sets the content of the input file to the variable input

def InitializeTable(table):
###For Loop to Initialize Table###
    for x in range(0,256): #for loop that gives a range of 256 numbers
        table.append(chr(x))  #sets the table to include the characters represented from 0 to 256

###CREATE FUNCTIONS TO BE CALLED###
def Encoder(input, table, string):
###For Loop for actual encoding algorithm###
    for symbols in input: #while there are still symboles in the input
        test = symbols + string #test variable STRING+SYMBOL
        if test in table:   #if test variable is in the table then string will be equal to the test variable
            string = test #string will be equal to the test variable if the test variable is in the table    
        else:   #otherwise add the test variable to the table
            compressed.append(table.index(string)) #outputting the code for the string by adding it to the compressed result array
            if len(table) < MAX_TABLE_SIZE: #if the length of the table is smaller than the max table size, add the test variable to the table
                table.append(test) #test varriable will be added to the table if the table is smaller than the max table size
            string = symbols #string is changed to be equal to symbols to add the newly added variable from the table to the compressed result

    compressed.append(table.index(string)) #add the variable that corresponds to the index of the value of string/symbols to the compressed result array

def PrintCode(compressed):
    print(compressed) #Print the compressed result array to the terminal

def ExportCode(compressed, finalCode, inputFileCommandLine):
###Code for exporting the compressed code to an output file###
    for code in compressed: #for each character in the compressed result array     
        finalCode+=chr(code) #add the corresponding unicode for each character in the compressed result array to the finalCode string
    encoded = finalCode.encode('UTF-16BE') #Encode each variable of finalCode using UTF-16BE as outlined in assignment
    compressedFile = inputFileCommandLine.split('.')[0] + ".lzw" #output file name (assignment wants it to be the same as the input file name with .lzw at the end)
    output = open(compressedFile, 'wb') #open the output file and set mode to write binary
    output.write(encoded) #write the compressed string to the output file 
    output.close() #Close output file
    inputFile.close() #close input file

###Call Functions###
InitializeTable(table) #Function to initialize table 0-256
Encoder(input, table, string) #Function to add to dictionary if not already there
PrintCode(compressed) #Function to Print the compressed Code to Terminal
ExportCode(compressed, finalCode, inputFileCommandLine) #Function to Export the Final Code to an lzw File