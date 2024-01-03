from common.commonBase import commonBase


class readExcel(commonBase):
    def __init__(self):
        super().__init__();


if __name__ == "__main__":
    re = readExcel()
    file = "../resources/TestData.xlsx"
    pd = re.read_excel(file, "Details")
    print(pd)
    row = pd[pd['Name'] == 'Ram'].index.item()
    print('Ram' + ' :: ' + str(pd['Age'][row]))
    row = pd[pd['Age'] == 10].index.item()
    print('10' + ' :: ' + str(pd['DEPT'][row]))
