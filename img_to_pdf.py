import os
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def convert_images_to_pdf(image_paths, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=A4)

    for img_path in image_paths:
        img = Image.open(img_path)
        img_w, img_h = img.size
        c.setPageSize((img_w, img_h))
        c.drawImage(img_path, 0, 0, width=img_w, height=img_h)
        c.showPage()

    c.save()

def get_valid_directory(prompt, default=os.getcwd()):
    directory = input(prompt)
    if not directory:
        directory = default
    if not os.path.isdir(directory):
        print("Invalid directory path.")
        return None
    return directory

def main():
    input_directory = get_valid_directory("Enter the input directory containing images (leave empty for current directory): ")
    output_directory = get_valid_directory("Enter the output directory for the PDF (leave empty for current directory): ")

    if not input_directory or not output_directory:
        return

    image_extensions = (".jpg", ".jpeg", ".png")
    image_files = [filename for filename in os.listdir(input_directory) if filename.lower().endswith(image_extensions)]

    if not image_files:
        print("No image files found in the directory.")
        return

    print("Found the following image files:")
    for idx, image_file in enumerate(image_files, start=1):
        print(f"{idx}. {image_file}")

    pdf_name = input("Enter the PDF filename (without .pdf extension): ")
    if pdf_name:
        input_images = [os.path.join(input_directory, filename) for filename in image_files]
        output_pdf = os.path.join(output_directory, f"{pdf_name}.pdf")
        convert_images_to_pdf(input_images, output_pdf)
        print(f"PDF '{output_pdf}' created successfully.")
    else:
        print("PDF filename cannot be empty.")

if __name__ == "__main__":
    main()
