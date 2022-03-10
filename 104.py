import csv
from collections import Counter
def get_mean(totalweight, totalentries):
    mean = totalweight/ totalentries
    print("mean = ", mean)

def get_median(totalentries, sorteddata):
    if totalentries%2 == 0:
        median1 = float(sorteddata[totalentries//2])
        median2 = float(sorteddata[totalentries//2 - 1])
        median = (median1+median2)/2 
    else:
        median = float(sorteddata[totalentries//2])
    print("median = ", median)

def get_mode(sorteddata):
    data = Counter(sorteddata)
    modedataforrange = {
                        "75-85":0,
                        "85-95":0,
                        "95-105":0,
                        "105-115":0,
                        "115-125":0,
                        "125-135":0,
                        "135-145":0,
                        "145-155":0,
                        "155-165":0,
                        "165-175":0
                        }
    for weight, occurrence in data.items():
        if 75<weight<85:
            modedataforrange["75-85"]+=occurrence
        elif 85<weight<95:
            modedataforrange["85-95"]+=occurrence
        elif 95<weight<105:
            modedataforrange["95-105"]+=occurrence
        elif 105<weight<115:
            modedataforrange["105-115"]+=occurrence
        elif 115<weight<125:
            modedataforrange["115-125"]+=occurrence
        elif 125<weight<135:            
            modedataforrange["125-135"]+=occurrence
        elif 135<weight<145:
            modedataforrange["135-145"]+=occurrence
        elif 145<weight<155:
            modedataforrange["145-155"]+=occurrence
        elif 155<weight<165:
            modedataforrange["155-165"]+=occurrence
        elif 165<weight<175:
            modedataforrange["165-175"]+=occurrence
    mode_range, mode_occurence = 0,0
    for range, occurence in modedataforrange.items():
        if occurence>mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])], occurence
    mode = float((mode_range[0]+mode_range[1])/2)
    print("mode is: ", mode)

with open("data.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
totalweight = 0
totalentries = len(file_data)
sorteddata = []

for person_data in file_data:
    totalweight += float(person_data[1])
    sorteddata.append(float(person_data[1]))

sorteddata.sort()

get_mean(totalweight, totalentries)
get_median(totalentries, sorteddata)
get_mode(sorteddata)