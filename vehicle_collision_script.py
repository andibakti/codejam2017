import csv
file = open('./datasets/Transportation/NYC General Transport/NYC-vehicle-collisions.csv', 'r')
newfile = open('./datasets/Transportation/NYC General Transport/vehicle-collisions-abridged.csv', 'w', newline='')
with file as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    with newfile as csvnewfile:
        writer = csv.writer(csvnewfile, delimiter=',')

        skipline = 0
        totalentry = 0
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

            if skipline:
                skipline = 0
                continue
            # elif i < 100:
            #     writer.writerow(nrow)
            #     totalentry += 1
            #     print(nrow)
            else:
                #break
                writer.writerow(nrow)
                totalentry += 1
                print(nrow)

        print(totalentry)

file.close()
newfile.close()
