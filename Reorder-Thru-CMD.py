import os
import re
import subprocess



def Numbering_Screenshots():
    """Iterates through the screenshots directory and renames them"""
    """Compensates for deletions in the directory by reordering the numbers"""
    """Attempt to fix the issue: failed"""


    src = "C:\\Users\\Micha\\OneDrive\\Pictures\\Screenshots"

 #   dest = "C:\\Users\\Micha\\OneDrive\\Pictures\\TestScreenshots\\"


    try:
#Change to the screenshots directory, and read the contents, sort in ascending orders.
        os.chdir(src)
        directory = os.listdir()
#Sort the files in the directory by the default numerical value from creation. Use the lambda function, and the re
#module to reference the numerical value in each filename.        
        directory = sorted(directory, key=lambda x: int(re.search(r'\d+', x).group()))

        for img in directory:
      
#Create a pattern that coorelates the Screenshot title with it's existing position in the directory.
                new_filename = f"Screenshot ({directory.index(img) + 1}).png"
#If the path already exists, continue to avoid file creation errors.
                if img == new_filename:
                    continue      
                
                else:
#If numbering is out of sequence, rename the file to the new filename using a subroccess() method.
                    cmd = ['cmd', '/c', 'ren', img, new_filename]
                    subprocess.run(cmd, check=True)                                             
                
        print("Renumbering Completed.")  
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    Numbering_Screenshots()
