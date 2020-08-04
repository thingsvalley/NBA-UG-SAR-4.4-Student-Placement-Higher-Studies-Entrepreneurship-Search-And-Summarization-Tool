import pandas as pd
def readexcel():
    data = pd.read_excel (r'C:\Users\Sunaina hosmani\Desktop\Internship\record.xlsx') #(use "r" before the path string to address special character, such as '\'). Don't forget to put the file name at the end of the path + '.xlsx'
    
    names = []
    
    for row in data.as_matrix() :
        
        names.append( [  row[0] , row[1]  ]  )
    
    return names
