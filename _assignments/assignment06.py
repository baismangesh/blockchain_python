import json
import pickle
# 1) Write a short Python script which queries the user for input 
# (infinite loop with exit possibility) and writes the input to a file.

# 2) Add another option to your user interface: 
# The user should be able to output the data stored in the file in the terminal.

# 3) Store user input in a list (instead of directly adding it to the file) 
# and write that list to the file – both with pickle and json.

# 4) Adjust the logic to load the file content to work with pickled/ json data.

waiting_for_input = True

filetxt = []

def load_file_text():
    #### using json #### 
    # with open('my_file.txt', mode='r') as f:
    #     file_content = f.read()
    #     global filetxt
    #     filetxt = json.loads(file_content)
    # print(filetxt)

    #### using pickle #### 
    with open('my_file.p', mode='rb') as f:
        global filetxt
        filetxt = pickle.loads(f.read())
        for txt in filetxt:
            print(txt)
 
load_file_text()

while waiting_for_input:
    print('Please choose option')
    print('1: Enter your text for writing to file')
    print('2: Read content from file')
    print('q: close')

    user_input = input('Your choice: ')

    if user_input == '1':
        #### using json #### 
        # with open('my_file.txt', mode='w') as f:
        #     # f.write(input('please enter your text to save in file: '))
        #     # f.write('\n')
        #     txt = input('please enter your text to save in file: ')
        #     filetxt.append(txt)
        #     f.write(json.dumps(filetxt))

        #### using pickle #### 
        with open('my_file.p', mode='wb') as f:
            txt = input('please enter your text to save in file: ')
            filetxt.append(txt)
            f.write(pickle.dumps(filetxt))
    if user_input == '2':
        #### using json ####
        # with open('my_file.txt', mode='r') as f:
        #     file_content = f.read()
        #     for txt in json.loads(file_content):
        #         print(txt)

        #### using pickle ####
        with open('my_file.p', mode='rb') as f:
            file_content = pickle.loads(f.read())
            for txt in file_content:
                print(txt)
                
    elif user_input == 'q':
        waiting_for_input = False

