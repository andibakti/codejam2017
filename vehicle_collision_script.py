import csv

def calcFactor(array):
    temparr = array
    array = trim(array)
    INJURED = 51410
    EMPTY = 225949
    factor = INJURED/EMPTY

    if array == None or len(array) == 1:
        return 0.1*factor
    elif noOther(array):
        return factor * (len(array) - 1)
    else:
        return factor * (len(array) - (othernum(array) + 1)) + factor * othernum(array)

def trim(array):
    for entry in range(len(array)-1, -1, -1):
        if array[entry] == '':
            array = array[:-1]
        else:
            return array

def noOther(array):
    cars = {'SPORT UTILITY/STATION WAGON', 'PASSENGER VEHICLE', 'BUS', 'TAXI', 'VAN', 'LIVERY VEHICLE'}
    other = False
    for entry in array:
        for vehicle in cars:
            if entry != vehicle:
                other = True
            else:
                other = False
                break
        if other:
            return False
    return True

def othernum(array):
    other = {'UNKNOWN', 'OTHER'}

    othercount = 0

    for entry in array:
        for smth in other:
            if entry == smth:
                othercount += 1
                break

    return othercount

def isEmpty(array):
    for value in array:
        if int(value) != 0:
            return False
    return True

file = open('./datasets/Transportation/NYC General Transport/NYC-vehicle-collisions.csv', 'r')
newfile = open('./datasets/Transportation/NYC General Transport/vehicle-collisions-abridged.csv', 'w', newline='')
with file as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    with newfile as csvnewfile:
        writer = csv.writer(csvnewfile, delimiter=',')

        skipline = 0
        totalentry = 0
        totalempty = 0
        totalinjury = 0

        empty = ['0'] * 5

        for i, row in enumerate(reader):
            nrow = []

            for j in range(0, len(row)):
                if j > 18:
                    break
                elif j == 0 or j == 1 or j == 3 or j == 4 or j == 7 or j == 9 or j == 10:
                    continue
                elif i == 0:
                    nrow.append(row[j])
                    continue
                elif row[j] == '':
                    skipline = 1
                    #print("thrash here")
                    break
                elif j == 2:
                    x = row[j].split(':')
                    minute = float(x[1]) / 60
                    time = float(x[0]) + minute
                    row[j] = str(time)

                nrow.append(row[j])

            if i == 0:
                nrow.append('OFFSET')
                writer.writerow(nrow)
                print(nrow)
                continue

            nrow.append(calcFactor(row[19:24]))

            if skipline:
                skipline = 0
                continue

            if isEmpty(row[11:18]):
                totalempty += 1

            if int(nrow[4]) > 0 and int(nrow[5]) == 0:
                totalinjury += 1

            # if i < 100:
            #     writer.writerow(nrow)
            #     totalentry += 1
            #     print(nrow)
            # else:
            #     break
            writer.writerow(nrow)
            totalentry += 1
            print(nrow)

        print(totalentry)
        print(totalinjury)
        print(totalempty)

file.close()
newfile.close()



