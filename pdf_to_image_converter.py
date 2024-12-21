from pdf2image import convert_from_path
import os

# Function to convert PDF pages to images
def pdf_to_images(pdf_path, output_folder, dpi=300):
    # Check if output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Convert PDF pages to images
    pages = convert_from_path(pdf_path, dpi=dpi)
    
    # Save each page as an image
    for i, page in enumerate(pages):
        image_path = os.path.join(output_folder, f'page_{i+1}.jpg')
        page.save(image_path, 'JPEG')
        print(f"Saved: {image_path}")

# Example usage
pdf_path = "resume.pdf"  # Replace with your PDF file path
output_folder = "output_images"  # Replace with your desired output folder
pdf_to_images(pdf_path, output_folder)
