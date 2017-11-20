import csv

totalKill = 277
totalInjured = 68689

killPoint = totalInjured/totalKill
numEntries = 277635

def calcPoints(reader):
    # points = open('./datasets/Transportation/NYC General Transport/points', 'w', newline='')
    # with file as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',')
    #
    #     for i, line in enumerate(reader):
    #         if i == 0:
    #             continue
    #         else:
    #             for entry in line[:]
    #             points.write()

    return
    

def findX(log):
    totalPoints = int(log[0]) + int(log[1]) * killPoint
    pedePoints = int(log[2]) + int(log[3]) * killPoint
    cyclPoints = int(log[4]) + int(log[5]) * killPoint
    motorPoints = int(log[6]) + int(log[7]) * killPoint

    totalPoints = totalPoints / numEntries
    pedePoints = pedePoints / numEntries
    cyclPoints = cyclPoints / numEntries
    motorPoints = motorPoints / numEntries

    return [totalPoints, pedePoints, cyclPoints, motorPoints]

def findS(log):
    X = findX(log)
    totalPart = 0
    pedePart = 0
    cyclPart = 0
    motorPart = 0

    file = open('./datasets/Transportation/NYC General Transport/vehicle-collisions-abridged.csv', 'r')
    with file as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for i, line in enumerate(reader):
            if i == 0:
                continue
            else:
                totalPart += (int(line[4]) + float(line[5]) * killPoint - X[0]) ** 2
                pedePart += (int(line[6]) + float(line[7]) * killPoint - X[0]) ** 2
                cyclPart += (int(line[8]) + float(line[9]) * killPoint - X[0]) ** 2
                motorPart += (int(line[10]) + float(line[11]) * killPoint - X[0]) ** 2


    totalS = (totalPart / (numEntries - 1)) ** (0.5)
    pedeS = (pedePart / (numEntries - 1)) ** (0.5)
    cyclS = (cyclPart / (numEntries - 1)) ** (0.5)
    motorS = (motorPart / (numEntries - 1)) ** (0.5)

    return [totalS, pedeS, cyclS, motorS]

file = open('./datasets/Transportation/NYC General Transport/vehicle-collisions-abridged.csv', 'r')
newfile = open('./datasets/Transportation/NYC General Transport/injury-death-points', 'w', newline='')
with file as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    N = -1

    log = [0] * 8

    for i, line in enumerate(reader):
        print(line)
        N += 1
        # if i == 100:
        #     break

        for j in range(0, len(line)):
            if i == 0:
                line.append("TOTAL POINTS")
                line.append("PEDESTRIAN POINTS")
                line.append("CYCLIST POINTS")
                line.append("MOTORCYCLIST POINTS")
                continue
            elif j > 3 and j < 12 and int(line[j]) != 0:
                value = int(line[j])
                log[j - 4] += value

    print(log)
    newfile.write(str(log) + '\n')
    newfile.write("total kill: " + str(log[1]) + '\n')
    newfile.write("total injured: " + str(log[0]) + '\n')
    newfile.write("pedeK :" + str(log[3]) + '\n')
    newfile.write("pedeI :" + str(log[2]) + '\n')
    newfile.write("cyclK: " + str(log[5]) + '\n')
    newfile.write("cyclI: " + str(log[4]) + '\n')
    newfile.write("motoK: " + str(log[7]) + '\n')
    newfile.write("motoI: " + str(log[6]) + '\n')
    newfile.write("\nNumber of entries: " + str(N) + '\n')

    X = findX(log)

    newfile.write('totalX:' + str(X[0]) + '\n')
    newfile.write('pedeX:' + str(X[1]) + '\n')
    newfile.write('cyclX:' + str(X[2]) + '\n')
    newfile.write('motorX:' + str(X[3]) + '\n')

    S = findS(log)

    newfile.write('totalS:' + str(S[0]) + '\n')
    newfile.write('pedeS:' + str(S[1]) + '\n')
    newfile.write('cyclS:' + str(S[2]) + '\n')
    newfile.write('motorS:' + str(S[3]) + '\n')

file.close()
newfile.close()