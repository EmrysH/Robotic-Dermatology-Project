from crop_img_by_clicking import crop_image

## Example how to use the cropping algorithm
# 1 - you need to call the method below with a full path (or a path from content root)
# 2 - left click to add crop points.
# 3 - Right click when you want to finish and crop (selection will close with first point)
image_cropped_return = crop_image("sample_qr.jpg")

print("finished, continue your program and do whatever!")

# If you want to see the resulting image you can pass True as second parameter
image_cropped_return = crop_image("sample_qr.jpg", show_resulting_image=True)
