
with open('Fan2023_AllCompositionsConverted.csv', 'w+') as outFile:
    for dataset in ['Fan2023_Database_FractureToughness.csv',
                    'Fan2023_Database_ImpactEnergy.csv',
                    'Fan2023_Database_ImpactToughness.csv']:
        print(f'Converting {dataset}...')
        with open(dataset, 'r') as inFile:
            print(inFile.readline())
            outFile.write(f'--> {dataset}\n')
            for line in inFile:
                data = line.split(',')
                comp = data[2]
                comp = comp.replace('-', ' ')
                outFile.write(comp+'\n')
        outFile.write('\n\n')