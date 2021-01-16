import pandas as pd
import environment as env
import numpy as np



class All_fun:
    def __init__(self):
        self.a = 3
        
    def sum_fun(self, n):
        if n>=0:
            ans = n*(n+1)/2

        else:
            ans = "Please enter a valid number"
        df = pd.DataFrame({"sum": [ans], "input_number": [n]})
        df.to_excel(env.table_name + '.xlsx')
        print(df)
        return df
   