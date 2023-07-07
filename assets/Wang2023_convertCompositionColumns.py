with open('Wang2023_DatasetForML_Hardness.csv', 'r') as inFile:
    with open('Wang2023_DatasetForML_Hardness_converted.csv', 'w+') as outFile:
        print(inFile.readline())
        print(inFile.readline())
        print(inFile.readline())
        outFile.write('Composition,Hardness,Ref/Uncertainty\n')
        for line in inFile:
            data = line.split(',')[1:]
            print(data)
            comp = ''
            for d, el in zip(data[:7], ['Al', 'Co', 'Cr', 'Cu', 'Fe', 'Ni', 'Mn']):
                if float(d)>0:
                    comp += el+d+' '
            print(comp)

            hardness = float(data[7])
            print(hardness)

            refuncertain = data[8].replace('\n', '').replace(' ', '')
            print(refuncertain)

            outFile.write(comp+','+str(hardness)+','+str(refuncertain)+'\n')