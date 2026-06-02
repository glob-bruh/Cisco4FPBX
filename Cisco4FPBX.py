
import xml.etree.ElementTree as xmlp

print("=======================================")
print("CISCO4FPBX")
print("----------")
print("Cisco IP phone configurator for FreePBX")
print("GlobBruh - https://tech.beyondgone.xyz/")
print("=======================================")
tftpPath = input("Please enter path to TFTP directory (default: /tftpboot/): ")
if tftpPath == "" or tftpPath == None: tftpPath = "/tftpboot/"
print("----------")
print("MENU:")
print("----------")
print("1 - PHONE CONFIGURATIONS")
print("2 - PHONE WALLPAPERS")
x = int(input("Selection [1-9]: "))

match x: 
    case 1: # PHONE CONFIGS
        print("Not implemented")
    case 2: # WALLPAPERS
        x = input("Please enter path to wallpaper directory (default: /tftpboot/Desktops/800x480x24/): ")
        if x == "" or x == None: x = "/tftpboot/Desktops/800x480x24/"
        tree = xmlp.parse(x + "List.xml") ; root = tree.getroot()
        array = []
        for i in root.findall("ImageItem"):
            x = [ i.get("URL").split(":")[1], i.get("Image").split(":")[1] ]
            array.append(x)
        print("-------------------")
        print("Current Wallpapers:")
        print("-------------------")
        for i in array:
            name = i[0].split("/")[1]
            print(f"Name: {name} -> URL: {i[0]} (thumbnail: {i[1]})")