import pandas as pd
class commonBase:
    pass
    def read_excel(self,file,sheetName):
        df=pd.read_excel(file,sheet_name=sheetName)
        return df
