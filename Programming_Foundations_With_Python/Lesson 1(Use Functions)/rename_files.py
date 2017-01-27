import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\KARAN PC\Desktop\prank")
    
    #print(file_list)
    saved_path = os.getcwd() #it stands for current working directory.

    #print("Current directory is: "+saved_path)
    os.chdir(r"C:\Users\KARAN PC\Desktop\prank")  # It is called as Change the current directory function

    #(2) for each file, rename filename
    for file_name in file_list :
        print("Old Name : " + file_name)
        print("New Name is : " + file_name.translate(None,"0123456789") )
        os.rename(file_name,file_name.translate(None, "0123456789") )

    os.chdir(saved_path)
    print("Current directory is: "+saved_path)

rename_files()
