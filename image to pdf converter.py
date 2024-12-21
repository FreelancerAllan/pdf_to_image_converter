from PIL import Image

# Paths to the images
image1_path = '1.jpg'
image2_path = '2.jpg'
image3_path = '3.jpg'
image4_path = '4.jpg'

# Open the images
image1 = Image.open(image1_path)
image2 = Image.open(image2_path)
image3 = Image.open(image3_path)
image4 = Image.open(image4_path)


# Ensure all images are in RGB mode
image1 = image1.convert('RGB')
image2 = image2.convert('RGB')
image3 = image3.convert('RGB')
image4 = image4.convert('RGB')

# List of images to be added to the PDF
image_list = [image2, image3,image4]

# Save images as a single PDF
pdf_path = 'RESUME.pdf'
image1.save(pdf_path, save_all=True, append_images=image_list)

print(f"PDF saved successfully at {pdf_path}")
