### Python program to find number of sheets needed for furniture design
### Cost reduction of fall off material from sheets
import math

while True:

    print("### SHEET CALCULTOR ###")

    ### Sheet size and blade cut width
    sheet_width = float(input("Input sheet width: "))
    sheet_length = float(input("Input sheet length: "))
    sheet_area = round((sheet_width * sheet_length), 2)

    ### Input of panel size and number of panels needed
    panel_width = float(input("Input panel width: "))
    panel_length = float(input("Input panel length: "))
    panel_num = int(input("Input number of panels needed: "))
    blade_cut = float(input("Input size of blade cut: "))

    ### Number of possible panels from each sheet
    rows = sheet_length/(panel_length + blade_cut)
    columns = sheet_width/(panel_width + blade_cut)
    panels_per_sheet = math.floor(rows * columns)

    ### Panel and Sheet area
    panel_area = round((panel_length + blade_cut) * (panel_width + blade_cut), 2)

    print("\nPanel area: " + str(panel_area) + '"')
    print("Sheet area: " + str(sheet_area) + '"\n')

    ### Number of sheets needed
    sheet_num = math.ceil(panel_num/panels_per_sheet)

    print("Number of panels per sheet: " + str(panels_per_sheet))
    print("Number of sheets needed: " + str(sheet_num))

    ### Calculate fall off of n-1 sheets
    sheet_left = sheet_area - (panels_per_sheet * panel_area)
    fall_off_percent = (sheet_left/sheet_area) * 100

    ### Calculate fall off of last sheet
    last_sheet_panels = panel_num - (panels_per_sheet * (sheet_num - 1))
    print("Panels left for last sheet: " + str(last_sheet_panels))

    last_sheet_fall_off = sheet_area - (last_sheet_panels * panel_area)
    last_sheet_fop = (last_sheet_fall_off/sheet_area) * 100
    last_sheet_leftover_area = (last_sheet_fop/100) * sheet_area

    print("\nFalloff of N-1 sheets: %" + str(round(fall_off_percent, 2)))
    print("Falloff of last sheet: %" + str(round(last_sheet_fop, 2)))
    print("Area of leftover sheet: " + str(round(last_sheet_leftover_area, 2)) + '"\n')

    cont = input("Type y to restart or any other key to exit: ")
    if cont == "y":
        continue
    else:
        break