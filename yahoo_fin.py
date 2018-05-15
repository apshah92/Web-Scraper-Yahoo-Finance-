import fix_yahoo_finance as yf

def pull_data(ticker_symbol,start,end):    
    data = yf.download(ticker_symbol, start=start, end=end)
    #print(data)
    closeIndex=data['Close']
    return closeIndex

if __name__=='__main__':
    ticker_symbol='QQQ'
    start='2008-04-04'
    end='2018-04-04'

    dailyQuotes=pull_data(ticker_symbol,start,end)
    
    #print(dailyQuotes)

    path='D:\Python\Daweili\\'          #provide path where you want to save your file.
    dailyQuotes.to_csv(path+'QQQ.csv',index=True,header=['Close'])
    print('File Written')

    
