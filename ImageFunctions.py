from binascii import hexlify, unhexlify
import wx

def ConvertGBAPalTo25Bit(palette):
    """
    Take a GBA palette and convert it to a normal
    25bit RGB palette. This function will return a
    list of tuples like (Red, Green, Blue).
    
    Palette should be in the form of "\xFF\xFF\xFF\xFF..."
    """
    blue_mask = 0x7C00
    green_mask = 0x3E0
    red_mask = 0x1F
    
    count = 0
    new_palette = []
    for n in range(len(palette)/2):
        color = palette[count+1]+palette[count]
        color = hexlify(color)
        color = int(color,16)
        
        red = (color & red_mask)
        green = (color & green_mask) >> 5
        blue = (color & blue_mask) >> 10
        
        red = red << 3
        green = green << 3
        blue = blue << 3
        
        new_color = [red,green,blue]
        new_palette.append(new_color)
        count += 2
    return new_palette

def Convert25bitPalettetoGBA(palette):
    """
    This function will take a list of tuples of RGB values
    and convert them back into the GBA format.
    
    It will return a bytestring of length 32.
    
    This function is only for 16 color sprites.
    """
    GBAPal = ""
    for color in palette:
        red = color[0]
        green = color[1]
        blue = color[2]
        
        red = red >> 3
        green = green >> 3
        blue = blue >> 3
        
        
        green = green << 5
        blue = blue << 10
        
        color = (blue & green & red)
        hexColor = hex(color).rstrip("L").lstrip("0x").zfill(4)
        bytes = unhexlify(hexColor)
        bytes = bytes[1]+bytes[0]
        GBAPal += bytes
    for i in range(32-len(GBAPal)):
        GBAPal += "\x00"
    return GBAPal
    
def ConvertGBAImageToNormal(image, palette, size=(64,64)):
    """
    This will take a GBA image in the form of a byte string
    like "\xff\xe0\x22..." and convert it to a normal RGB image.
    
    Because GBA images are stored in 8x8 tiles, there are a lot of
    loops in the function.:P
    """
    
    indexed_image = []
    for c in image:
        pixels = hexlify(c)
        pixela = int(pixels[1],16)
        pixelb = int(pixels[0],16)
        indexed_image.append(pixela)
        indexed_image.append(pixelb)
    width = size[0]
    height = size[1]
    NumOfBlocks = (width/8) * (height/8)
    blocks = []
    n = 0
    for z in range(NumOfBlocks):
        tmp_list = indexed_image[n:n+64]
        blocks.append(tmp_list)
        n += 64
    image_data = []
    b = 0
    a = 0
    row = 0
    for x in range(height/8):
        for y in range(8):
            b = row
            for z in range(width/8):
                r = 0
                for w in range(8):
                    image_data.append(blocks[b][a+r])
                    r += 1
                b += 1
            a += 8
        a = 0
        row += width/8
    img_data = []
    for pixel in image_data:
        img_data.append(palette[pixel][0]) #Append Red
        img_data.append(palette[pixel][1]) #Append Green
        img_data.append(palette[pixel][2]) #Append Blue

    data = ""
    for color in img_data:
        data += unhexlify(hex(color)[2:].zfill(2))
    img = wx.ImageFromData(size[0], size[1], data)
    bitmap = wx.BitmapFromImage(img)
    return bitmap
    
def ConvertNormalImageToGBA(image, size=(64,64)):
    """
    This function will take a normal wx.Image and return tuple
    of (GBA_Image, Palette). Image must be already 16 colors
    and have dimensions divisible by 8.
    """
    data = image.GetData()
    height = size[1]
    width = size[0]
    palette = []
    blocks = []
    block_num = width/8
    for w in range(height/8):
        for x in range(8):
            block_num -= width/8
            for y in range(width/8):
                for z in range(8):
                    color = (int(hexlify(data[:1]),16),
                                  int(hexlify(data[1:2]),16),
                                  int(hexlify(data[2:3]),16))
                    if color not in palette:
                        palette.append(color)
                    try: blocks[block_num]
                    except: blocks.append([])
                    blocks[block_num].append(color)
                    data = data[3:]
                block_num += 1
        block_num += width/8
    GBAImage = ""
    color1 = None
    color2 = None
    for block in blocks:
        for color in block:
            if color1 == None:
                color1 = hex(palette.index(color))[2:].zfill(1)
            else:
                color2 = hex(palette.index(color))[2:].zfill(1)
                GBAImage += unhexlify(color2+color1)
                color1 = None
                color2 = None
    return (GBAImage, palette)
    
def ConvertNormalImageToGBAUnderPal(image, palette,size=(64,64)):
    """
    This function will take a normal wx.Image and return tuple
    of (GBA_Image, Palette). Image must be already 16 colors
    and have dimensions divisible by 8.
    
    The difference between this function and the last is that a palette is provided
    to index to.
    """
    data = image.GetData()
    height = size[1]
    width = size[0]
    blocks = []
    block_num = width/8
    for w in range(height/8):
        for x in range(8):
            block_num -= width/8
            for y in range(width/8):
                for z in range(8):
                    color = (int(hexlify(data[:1]),16),
                                  int(hexlify(data[1:2]),16),
                                  int(hexlify(data[2:3]),16))
                    try: blocks[block_num]
                    except: blocks.append([])
                    blocks[block_num].append(color)
                    data = data[3:]
                block_num += 1
        block_num += width/8
    GBAImage = ""
    color1 = None
    color2 = None
    for block in blocks:
        for color in block:
            if color1 == None:
                color1 = hex(palette.index(color))[2:].zfill(1)
            else:
                color2 = hex(palette.index(color))[2:].zfill(1)
                GBAImage += unhexlify(color2+color1)
                color1 = None
                color2 = None
    return (GBAImage, palette)

def GetShinyPalette(normal, shiny, normal_palette):
    """
    This function helps to ensure that the shiny and 
    normal palettes are in the same order.
    
    Just pass it the normal and shiny images,
     along with the normal palette.
    """
       
    palette = []
    norm = list(normal.getdata())
    shin = list(shiny.getdata())
    for pixel in normal_palette:
        index = norm.index(pixel)
        palette.append(shin[index])
    return palette
        