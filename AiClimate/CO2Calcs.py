###
#average grams per kilometer
#compact: 216.6
#fullsize: 263.2
#midsize: 222.4
#minicompact: 236.6
#minivan 262.3
#pickuptruck: 296.3
#stationwagon: 206.7
#subcompact: 246.4
#small SUV: 236.3
#standard SUV: 304.8
#two seaters: 277.6
#van:388.3
###

import json

CO2_per_mile = None

#for the image insert makes a Car that is gas and not a ev
def get_car_report(output_findImage):
    return

# def write_to_json():
#     values= {
#         "Type": type,
#         "hybrid": hybrid,
#         "gas": gas,
#         "diesel": diesel,
#         "co2PerMile": co2_per_mile
#     }
    
#     with open("MyCar.json", "w") as outfile:
#         json.dump(values, outfile, indent= 3)

type: str

def calculte_co2_per_mile(type:str ):
    co2_per_km:float = 0.0
    if type == "Compact": co2_per_km += 216.6
    elif type == "Fullsize": co2_per_km += 263.2
    elif type == "Midsize": co2_per_km += 222.4
    #elif type == "minicompact": co2_per_km += 236.6
    elif type == "MiniVan": co2_per_km += 262.3
    elif type == "PickupTruck": co2_per_km += 296.3
    elif type == "StationWagon": co2_per_km += 206.7
    #elif type == "subcompact": co2_per_km += 246.4
    elif type == "CompactSUV": co2_per_km += 236.3
    elif type == "SUV": co2_per_km += 304.8
    elif type == "TwoSeater": co2_per_km += 277.0
    elif type == "FullsizeVan": co2_per_km += 388.3
    print(co2_per_km)
    return co2_per_km
    


def co2Report():
    write = "-----------------------\n"
    write+= "- CO2 EMMISION REPORT -\n"
    write+= "-----------------------\n"
    