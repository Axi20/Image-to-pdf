# Image to PDF
This is a Python console application that can be used to convert multiple images into a single PDF file.

## Usage
- To run the script, you need to have Python installed on your computer.
- First you need to run this command from the terminal (from the directory where the script is located)`pip install pillow reportlab`
- You can execute the script from the terminal using the command: `python img_to_pdf.py`
- If you encounter an error message stating "python is not recognized as an internal or external command, operable program, or batch file," you should add the path to your Python executable to the Environment Variables and then restart the terminal.
 
1. The program will prompt you to provide the directory path containing the images.
   - Please use the absolute path format, such as: "C:\Users\Username\Images"
   - If you leave this field empty (press Enter), the default directory where this script is located will be used.
2. The program will also ask for the output directory where it should save the PDF file.
   - Once again, please provide an absolute path or leave it empty.
3. If any of the directory paths are invalid, you will receive an error message saying "Invalid directory path," and the program will exit.
4. If the directories are valid, you will receive a list of the images.
   - If there are no image files, you will see the message: "No image files found in the directory."
   - Allowed image extensions: .jpg, .jpeg, .png
5. Finally, you need to enter the desired PDF name without the extension. The PDF will be saved in the provided directory.

*Feel free to customize this code according to your preferences.*
