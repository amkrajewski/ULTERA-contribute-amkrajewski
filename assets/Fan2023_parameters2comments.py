with open('Fan2023_parametersComments.csv', 'w+') as outFile:
    parsePointer = 'Fan2023_Database_ImpactEnergy.csv'
    print(parsePointer)
    outFile.write('--> '+parsePointer+'\n')
    with open(parsePointer, 'r') as inFile:
        print(inFile.readline())
        for line in inFile:
            data = line.split(',')
            comment = ''
            for prefix, field in zip(['processing details',
                                      'grain size (micrometers)',
                                      'original composition note',
                                      'Fan2023ID'],
                                     [data[4], data[6], data[1], data[0]]):
                if field!='   ':
                    comment += prefix+': '+field+'; '
            #print(comment)
            outFile.write(comment+'\n')
    outFile.write('\n\n')

    parsePointer = 'Fan2023_Database_ImpactToughness.csv'
    print(parsePointer)
    outFile.write('--> '+parsePointer+'\n')
    with open(parsePointer, 'r') as inFile:
        print(inFile.readline())
        for line in inFile:
            data = line.split(',')
            comment = ''
            for prefix, field in zip(['processing details',
                                      'grain size (micrometers)',
                                      'original composition note',
                                      'Fan2023ID'],
                                     [data[4], data[6], data[1], data[0]]):
                if field != '   ':
                    comment += prefix + ': ' + field + '; '
            #print(comment)
            outFile.write(comment + '\n')
    outFile.write('\n\n')

    parsePointer = 'Fan2023_Database_FractureToughness.csv'
    print(parsePointer)
    outFile.write('--> '+parsePointer+'\n')
    with open(parsePointer, 'r') as inFile:
        print(inFile.readline())
        for line in inFile:
            data = line.split(',')
            #print(data)
            materialComment = ''
            for prefix, field in zip(['processing details',
                                      'grain size (micrometers)',
                                      'original composition note',
                                      'Fan2023ID'],
                                     [data[4], data[6], data[1], data[0]]):
                if field != '   ':
                    materialComment += prefix + ': ' + field + '; '
            #print(materialComment)
            outFile.write(materialComment + ',')

            propertyComment = ''
            for prefix, field in zip(['test type',
                                      'standard',
                                      'geometry',
                                      'size (mm)',
                                      'notch geometry (mm)'],
                                        [data[16],
                                         data[17],
                                         data[18],
                                         data[19],
                                         data[20]]):
                if field != '   ':
                    propertyComment += prefix + ': ' + field + '; '
            #print(propertyComment)
            outFile.write(propertyComment + '\n')

