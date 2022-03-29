import os
from os import listdir
from os.path import isfile, isdir, join
import csv
# 指定要查詢的路徑

def mergeFiles(StockNums):
    for StockNum in StockNums.split(' '):
        mypath = 'C:\\Users\\KK\\Desktop\\data\\stock_data\\'+str(StockNum)
        files = listdir(mypath)
        csvFiles = []
        # 以迴圈處理
        for f in files:
        # 產生檔案的絕對路徑
            fullpath = join(mypath, f)
            # 判斷 fullpath 是檔案還是目錄
            if isfile(fullpath):
                csvFiles.append(f)
            
        print('目錄中csv檔:')
        print(csvFiles)
        print('合併儲存中...\n')
        _rows = []
        last_row = []
        with open(StockNum+'_save.csv','w',newline='') as writefile:
            writer = csv.writer(writefile)
            writer.writerow(['Date','Open','High','Low','Close','Adj Close','Volume'])
            for file in csvFiles:
                with open(mypath+'\\'+file,newline='') as csvfile:
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
    StockNums = input("輸入要合併的股號資料(可批量處裡)：")
    mergeFiles(StockNums)
