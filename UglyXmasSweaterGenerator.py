from PIL import Image
import random
import os

#PATHS
def combinePaths(listofpaths, outputlist, path):
    for x in listofpaths:
        outputlist.append(path + "/" + x)

PATH_PRIMARY = "\Feed Stock\Primary Color"
list_primary = os.listdir(PATH_PRIMARY)
paths_primary = []
combinePaths(list_primary, paths_primary, PATH_PRIMARY)

PATH_SECONDARY = "\Feed Stock\Secondary Color"
list_secondary = os.listdir(PATH_SECONDARY)
paths_secondary = []
combinePaths(list_secondary, paths_secondary, PATH_SECONDARY)

PATH_DESIGN_NO_SECONDARY = "\Feed Stock\Design\All Over"
list_designA = os.listdir(PATH_DESIGN_NO_SECONDARY)
paths_designA = []
combinePaths(list_designA, paths_designA, PATH_DESIGN_NO_SECONDARY)

PATH_DESIGN_SECONDARY_ALLOVER = "\Feed Stock\Design\Part\All Over"
list_designB1 = os.listdir(PATH_DESIGN_SECONDARY_ALLOVER)
paths_designB1 = []
combinePaths(list_designB1, paths_designB1, PATH_DESIGN_SECONDARY_ALLOVER)

PATH_DESIGN_SECONDARY_ARMS = "\Feed Stock\Design\Part\Arms"
list_designB2 = os.listdir(PATH_DESIGN_SECONDARY_ARMS)
paths_designB2 = []
combinePaths(list_designB2, paths_designB2, PATH_DESIGN_SECONDARY_ARMS)

PATH_DESIGN_SECONDARY_CHEST = "\Feed Stock\Design\Part\Chest"
list_designB3 = os.listdir(PATH_DESIGN_SECONDARY_CHEST)
paths_designB3 = []
combinePaths(list_designB3, paths_designB3, PATH_DESIGN_SECONDARY_CHEST)

PATH_DESIGN_SECONDARY_SHOULDERS = "\Feed Stock\Design\Part\Shoulders"
list_designB4 = os.listdir(PATH_DESIGN_SECONDARY_SHOULDERS)
paths_designB4 = []
combinePaths(list_designB4, paths_designB4, PATH_DESIGN_SECONDARY_SHOULDERS)

PATH_FINISHING_TOUCHES = "\Feed Stock\Finishing Touches/1.png"
PATH_OUTPUT = "\Output"

RARE_ADDON = "\Feed Stock/Rare Addons/Snow Outline.png"

# COLORS
red = (161,16,41)
red2 = (175,6,11)
yellow = (255,217,125)
white = (255,255,240)
white2 = (237,237,237)
white3 = (202, 210, 213)
brown = (78,39,24)
green = (31,64,10)
green2= (116, 149,122)
green3 = (33,85,36)
green4= (46,75,57)
colors = [('red', red),('red', red2), ('yellow',yellow), ('brown', brown), ('green',green), ('green', green2), ('green', green3), ('green', green4)]

def generate_sweater_random(iteration, file):
    index_base = random.randint(0, len(paths_primary)-1)
    ledg_base = list_primary[index_base].replace(".png", "")
    base = Image.open(paths_primary[index_base])       #open random primary
    if random.randint(1,101) > 90:                  #10% chance of getting All Over design
        index_designA = random.randint(0,len(paths_designA)-1)
        secondary = Image.open(r"Feed Stock/empty.png")
        designA = Image.open(paths_designA[index_designA])
        designB1 = Image.open(r"Feed Stock/empty.png")
        designB2 = Image.open(r"Feed Stock/empty.png")
        designB3 = Image.open(r"Feed Stock/empty.png")
        designB4 = Image.open(r"Feed Stock/empty.png")
        ledgA = list_designA[index_designA].replace(".png", "")
        ledgSecondary = "None"
        ledgB1 = "None"
        ledgB2 = "None"
        ledgB3 = "None"
        ledgB4 = "None"
    else:                                           #90% chance of getting Composite design
        index_secondary = random.randint(0, len(paths_secondary)-1)
        secondary = Image.open(paths_secondary[index_secondary])
        designA = Image.open(r"Feed Stock/empty.png")
        ledgA = "None"
        ledgSecondary = list_secondary[index_secondary].replace(".png", "")
        if random.randint(1,101) > 90:              #Of the above 90%, 10% chance of getting Composite color All Over design
            index_designB1 = random.randint(0,len(paths_designB1)-1)
            designB1 = Image.open(paths_designB1[index_designB1])
            designB2 = Image.open(r"Feed Stock/empty.png")
            designB3 = Image.open(r"Feed Stock/empty.png")
            designB4 = Image.open(r"Feed Stock/empty.png")
            ledgB1 = list_designB1[index_designB1].replace(".png", "")
            ledgB2 = "None"
            ledgB3 = "None"
            ledgB4 = "None"
        else:                                       #Of the above 90%, 90% chance of getting composite design
            index_designB2 = random.randint(0,len(paths_designB2)-1)
            index_designB3 = random.randint(0,len(paths_designB3)-1)
            index_designB4 = random.randint(0,len(paths_designB4)-1)
            designB1 = Image.open(r"Feed Stock/empty.png")
            designB2 = Image.open(paths_designB2[index_designB2])
            designB3 = Image.open(paths_designB3[index_designB3])
            designB4 = Image.open(paths_designB4[index_designB4])
            ledgB1 = "None"
            ledgB2 = list_designB2[index_designB2].replace(".png", "")
            ledgB3 = list_designB3[index_designB3].replace(".png", "")
            ledgB4 = list_designB4[index_designB4].replace(".png", "")
            
    finishingTouches = Image.open(PATH_FINISHING_TOUCHES)
    rareAddon = Image.open(RARE_ADDON)
    
    #SET UP BACKGROUND
    bgcolor = random.choice(colors)[1]
    background_size = [50,50]
    background = Image.new(mode="RGB", size=background_size, color=bgcolor)
    area = (0,0)

    #ASSEMBLE SWEATER
    background.paste(base, area, base)
    background.paste(secondary, area, secondary)
    background.paste(designA, area, designA)
    background.paste(designB1, area, designB1)
    background.paste(designB2, area, designB2)
    background.paste(designB3, area, designB3)
    background.paste(designB4, area, designB4)
    background.paste(finishingTouches, area, finishingTouches)
    if random.randint(1,1226) > 1213:       # ~1% chance of getting snowy background
        background.paste(rareAddon, area, rareAddon)
        snow = "Present"
    else:
        snow = "Not present"

    #RESIZE AND SAVE
    resized_img = background.resize((300, 300), resample=Image.NEAREST)
    resized_img.save(PATH_OUTPUT + "/" + str(iteration) +  '.png', "PNG")

    #WRITE TO LEDGER
    file.write(str(iteration) + "\t" + ledg_base + "\t" + ledgSecondary + "\t" + ledgA + "\t" + ledgB1 + "\t" + ledgB2 + "\t" + ledgB3 + "\t" + ledgB4 + "\t" + snow + "\t" + "\n")
def iterate(quantity):
    file = open("ledger.csv", "w")
    iteration = 1
    for n in range(quantity):
        generate_sweater_random(iteration, file)
        iteration += 1
    print("Done")
    file.close()

iterate(100)
