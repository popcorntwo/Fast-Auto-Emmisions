#plug in hybrids 42-46% higher effeciency (ICCT)
#approx 4.2% less emmiosins
#diesel get 25% more gallon/mi

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
#two seaters: 277.6'
#van:388.3
###

import json
class Car:
    #for the image insert makes a Car that is gas and not a ev
    def __init__(self,type: str,hybrid= False, gas= True ,diesel= False):
        self.type=type
        self.hybrid= hybrid
        self.gas= gas
        self.diesel= diesel
        self.co2_per_mile = self.calculte_co2_per_mile(type,hybrid,gas,diesel)
        values= {
            "Type":self.type,
            "hybrid": self.hybrid,
            "gas":self.gas,
            "diesel":self.diesel,
            "co2PerMile":self.co2_per_mile
        }
        with open("sample.json", "w") as outfile:
            json.dump(values, outfile, indent= 3)

    def calculte_co2_per_mile(self, type: str,hybrid: bool,gas: bool,diesel: bool):
        co2_per_km:float = 0.0
        if type == "compact": co2_per_km += 216.6
        elif type == "fullsize": co2_per_km += 263.2
        elif type == "midsize": co2_per_km += 222.4
        elif type == "cminicompact": co2_per_km += 236.6
        elif type == "minvan": co2_per_km += 262.3
        elif type == "pickuptruck": co2_per_km += 296.3
        elif type == "stationwagon": co2_per_km += 206.7
        elif type == "subcompact": co2_per_km += 246.4
        elif type == "smallSUV": co2_per_km += 236.3
        elif type == "standardSUV": co2_per_km += 304.8
        elif type == "twoseaters": co2_per_km += 277.
        elif type == "twoseaters": co2_per_km += 388.3
        # returns co2/mi
        co2_per_mi = co2_per_km / 0.6213711922
        if diesel: co2_per_mi/.9
        if hybrid: co2_per_mi/.65
        return co2_per_mi

car = Car("compact",)