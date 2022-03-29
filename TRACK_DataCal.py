import os
from os import listdir
from os.path import isfile, isdir, join
import csv
mypath = 'C:\\Users\\User\\Desktop\\data\\'
def CalData():
    files = listdir(mypath+"tmp")
    print(files)
    csvFiles = []
    # 以迴圈處理
    for f in files:
    # 產生檔案的絕對路徑
        fullpath = mypath+"tmp\\"+f
        # 判斷 fullpath 是檔案還是目錄
        csvFiles.append(f)
        
    print('目錄中csv檔:')
    print(csvFiles)
    print('轉換中...\n')
    _rows = []
    last_row = []
    for file in csvFiles:
        StockNum = file.split("_")[2]
        with open(mypath+"update\\"+StockNum+'_update.csv','w',newline='') as writefile:
            writer = csv.writer(writefile)
            writer.writerow(['Date','Open','High','Low','Close','Adj Close','Volume'])
            with open(mypath+'tmp\\'+file,newline='') as csvfile:
                rows = csv.reader(csvfile)
                rows = list(rows)
                del rows[0:2]
                del rows[-5:]
                for row in rows:
                    row[0] = row[0].split('/')
                    row[0][0] = str(int(row[0][0])+1911)
                    row[0] = '-'.join(row[0])
                    for i in range(1,7):
                        try:
                            row[i] = row[i].replace(',','')
                        except:
                            pass
                        try:
                            row[i] = float(row[i])
                        except:
                            pass
                    volume = int(row[1])
                    del row[9]
                    del row[8]
                    del row[7] 
                    del row[2]
                    del row[1]
                    row.append(row[4])
                    row.append(volume)
                    last_row = row[:]
                    writer.writerow('{:}'.format(x) if(type(x)!=float) else format(x,'.6f') for x in row)
        #writer.writerow('{:}'.format(x) if(type(x)!=float) else format(x,'.6f') for x in last_row)
                        
    print('\n---結束轉換---\n')
if __name__ == '__main__':
    CalData()
