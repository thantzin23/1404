color = {"White":'#FFFFFF',"Black":'#000000',"Red":'FF0000',"Yellow":'#FFFF00',"Lime":'00FF00'
    ,"Aqua":'00FFFF',"Blue":'0000FF',"Purple":'800080',"Gray":'808080',"Maroon":'800000'}

print(color)

color_name = input("Enter color name:").title()

while color_name != "":
    if color_name in color:
        print( color[color_name])
    else:
        print("Invalid options>")
    color_name = input("Enter color namr:").title()