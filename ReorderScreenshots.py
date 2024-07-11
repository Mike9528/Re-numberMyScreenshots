
import os



def Numbering_Screenshots():
    """Iterates through the screenshots directory and renames them"""
    """Compensates for deletions in the directory by reordering the numbers"""


    src = "C:\\Users\\Micha\\OneDrive\\Pictures\\TestScreenshots"
    dest = "C:\\Users\\Micha\\OneDrive\\Pictures\\TestScreenshots\\"


    try:
#change to the screenshots directory, and list the contents.
        os.chdir(src)
        directory = os.listdir()
#If the directory is empty, print an informational message.
        if not directory:
            print("No images found in the directory")
#for each image in the directory, rename using the default format Screenshot().png, reordering the
#numbers, starting from 1. This is to compensate for deletions in the directory.
        #directory.sort() #didn't alter the results as expected.
        for img in directory:
#Screenshots are all saved as .png files.
            if img.endswith(".png"):
#The format of the screenshots is Screenshot().png, so we use the index of the img
#in the directory list.
                os.rename(img, f"Screenshot({directory.index(img)}).png")
        print("Renumbering Completed.")
#If an error occurs, print the error message.    
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    Numbering_Screenshots()
