with open('Fan2023_parametersComments.csv', 'w+') as outFile:
    parsePointer = 'Fan2023_Database_ImpactEnergy.csv'
    print(parsePointer)
    outFile.write('--> '+parsePointer+'\n')
    with open('Fan2023_Database_ImpactEnergy.csv', 'r') as inFile:
        print(inFile.readline())
        for line in inFile:
            data = line.split(',')
            print(data)
            comment = ''
            for prefix, field in zip(['processing details',
                                      'grain size (micrometers)',
                                      'original composition note'],
                                     [data[4], data[6], data[1]]):
                if field!='   ':
                    comment += prefix+': '+field+'; '
            print(comment)
            outFile.write(comment+'\n')
    outFile.write('\n\n')