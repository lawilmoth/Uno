# Importing Image class from PIL module
from PIL import Image
 
# Opens a image in RGB mode
im = Image.open("images\\UNO_cards_deck.png")
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
# Setting the points for cropped image
card_width = width / 14
card_height = height / 8
colors = ["red", "yellow", "green", "blue"]
for col in range(14):
    for row in range(4):

        left = col * card_width
        top = row * card_height
        right = (col+1) * card_width
        bottom = (row+1) * card_height
        
        # Cropped image of above dimension
        # (It will not change original image)
        im1 = im.crop((left, top, right, bottom))
        
        if  col < 10:
            # Shows the image in image viewer
            im1.save(f"images\\{colors[row]}_{col}.png")
        elif col == 10:
            im1.save(f"images\\{colors[row]}_skip.png")
        elif col == 11:
            im1.save(f"images\\{colors[row]}_reverse.png")
        elif col == 12:
            im1.save(f"images\\{colors[row]}_draw_2.png")
        elif col == 13:
            im1.save(f"images\\wild.png")
#Wild draw 4
left = 13 * card_width
top = 4 * card_height
right = (13+1) * card_width
bottom = (4+1) * card_height

# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
im1.save(f"images\\wild_draw_4.png")