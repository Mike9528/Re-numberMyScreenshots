import os



def Numbering_Screenshots():
    """Iterates through the screenshots directory and renames them"""
    """Compensates for deletions in the directory by reordering the numbers"""


    src = "C:\\Users\\Micha\\OneDrive\\Pictures\\TestScreenshots"
    dest = "C:\\Users\\Micha\\OneDrive\\Pictures\\TestScreenshots\\"


    try:
#Change to the screenshots directory, and read the contents, sort in ascending order.
        os.chdir(src)
        directory = sorted(os.listdir())
#Iterates through the list of files.
        for img in directory:
#Screenshots are all .png files. Prevent any stray files from being renamed.
            if img.endswith(".png"):
#The format of the screenshots is Screenshot().png, and we use the index of the img
#in the directory list. And maintain the original order of the screenshots.
                os.rename(img, f"Screenshot({directory.index(img) + 1}).png")
        print("Renumbering Completed.")
#If an error occurs, print the error message.    
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    Numbering_Screenshots()
