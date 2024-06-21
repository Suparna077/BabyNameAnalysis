import pandas as pd
import matplotlib.pyplot as pp
import zipfile

def readandconcat():

    zipfile.ZipFile('names.zip').extractall('.')
    allyears = pd.concat(pd.read_csv(f'names/yob{year}.txt',
                                     names=['name', 'sex', 'number']).assign(year=year)
                         for year in range(1880, 2019))
    allyears.to_csv('allyears.csv.gz', index=False)

def Fetchfile():
    allyears = pd.read_csv('allyears.csv.gz')
    return allyears

def Toptennmaes(allyears):

    allyearsTopten = allyears.set_index(['sex','year']).sort_index()
    YearlyToTen = pd.concat(pd.DataFrame(allyearsTopten.loc[sex, year]
                               .sort_values(['number'],ascending=True).tail(10).iloc[::-1])
                  for year in range(1880,2019)
                            for sex in ['M','F'])
    YearlyToTen.to_csv('YearlyTopTen.csv')

def NamePopularityYearly(allyears_indexed,sex,names):

    pp.figure(figsize=(12, 2.5))
    for name in names:
        sexvalue = sex[names.index(name) - 1]
        pp.plot(allyears_indexed.loc[(sexvalue, name)], label = name)
        pp.axis(xmin=1880, xmax=2018)

    pp.legend()
    pp.show()

def UniqueNames(allyears,sex):

    allyears_indexed = allyears.set_index(['sex']).sort_index()
    print(allyears_indexed.loc[sex].drop_duplicates(subset=['name'],keep = 'last')['name'])
    print('Total Count : ', len(allyears_indexed.loc[sex].drop_duplicates(subset=['name'],keep = 'last')))

def main():

    pd.options.display.max_rows = 20
    readandconcat()
    allyears = Fetchfile()

    Flag = 'Y'

    while Flag != 'N':

        print(" -----------------------Analysis Menu-------------------------","\n")
        print("\t\t 1. Display all unique names based on sex - ","\n",
              "\t\t 2. Print Csv For Top Ten Names Yearly - ","\n",
              "\t\t 3. Display Graph for popularity of names over years - ","\n")
        UserInput = input("---------Select a Option or type N to exit---------- : ")
        if UserInput == 'N':
            Flag = 'N'
        elif UserInput == '1':
            sex = input("---------Select a Option for sex M/F---------- : ")
            UniqueNames(allyears,sex)
        elif UserInput == '2':
            Toptennmaes(allyears)
        elif UserInput == '3':
            count = int(input("---------Enter Total Number Of Names To Input For Analysis ---------- : "))
            Sex = []
            Names = []
            for i in range(0,count):
                Sex.append(input("----Enter The Sex----- : "))
                Names.append(input("----Enter The Name----- : "))
            allyears_indexed = allyears.set_index(['sex', 'name', 'year']).sort_index()
            NamePopularityYearly(allyears_indexed,Sex,Names)
        else:
            print("---------Please Provide Correct Input-----------")





































if __name__ == "__main__":
    main()