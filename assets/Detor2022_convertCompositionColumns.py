with open('GE_RefractoryAlloyScreeningDataset_FINAL.csv', 'r') as inFile:
    with open('GE_RefractoryAlloyScreeningDataset_converted.csv', 'w+') as outFile:
        print('Labels: '+inFile.readline())
        outFile.write('Composition,Ductility Class,Hardness\n')
        for line in inFile:
            data = line.split(',')
            print(data)
            comp = ''
            for d, el in zip(data[:9], ['Hf', 'Mo', 'Nb', 'Re', 'Ru', 'Ta', 'Ti', 'W', 'Zr']):
                if float(d)>0:
                    comp += el+d+' '
            print(comp)
            ductilityClass = data[9]
            ductilityClassDict = {
                '0': 0,
                '1': 0.1,
                '2': 1,
                '3': 10,
                '4': 20,
                '5': 50,
            }
            ductility = ductilityClassDict[ductilityClass]
            print(ductility)

            hardness = float(data[11].replace('\n', ''))
            print(hardness)

            outFile.write(comp+','+str(ductility)+','+str(hardness)+'\n')