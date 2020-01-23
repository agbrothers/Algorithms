import numpy as np
from PIL import Image


""" IMAGE FUNCTIONS """

image = Image.open('images/albert_einstein.jpeg')
width, height = image.size
image = image.convert('L') # convert the image to monochrome

# Scale down the image to 100 pixel width
k = image.size[0]/100 
image = image.resize((int(width/k), int(height/k)))


""" ASCII CONVERSION """

# Create an array of brightness values for each pixel
pix_val = np.asarray(image) 

# Different Character Palates
char = ['M','X','x','.'] 
math_chars = ['∑','Ω','√','∫','ß','∂','µ','π','x','≤','≥','<','>','÷','≈','+','-','.',' ']  # math char's ∏∑Ω√∫ß∂yµπx≤≥<>÷≈=+-.
alt_chars = ['@','#','M','X','=','•','.',' ']  # This one gives nice results

# Create array to map characters to corresponding brightness levels
brightness = np.linspace(0,256,len(char)) 
char_line = ''

# Create a text file to write the ascii to
ascii_text = open('ascii_image.txt', 'w')

# Don't care about run time or space constraints, so naive approach works fine:
# Loop through each pixel in the image and assign it to a char based on brightness
for i in range(pix_val.shape[0]):
    for j in range(pix_val.shape[1]):
        l = 0
        char_added = False
        while char_added == False:
            if pix_val[i][j] < brightness[l]:
                char_line += (char[l])*2 #add two char's per pixel to compensate for line spacing distortion
                char_added = True
            l+=1
        #char_line += ' '
        
    ascii_text.write(char_line + '\n')
    char_line = ''

ascii_text.close()
