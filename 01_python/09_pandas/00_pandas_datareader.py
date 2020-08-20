from pandas_datareader import data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2015, 12, 1)
end = datetime.datetime(2016, 3, 1)

# 애플: AAPL
# 구글: GOOG
# 삼성: 005930.KS
 
gs = web.get_data_yahoo('005930.KS')
gs.tail()

plt.figure(figsize=(15, 5))
plt.plot(gs['Close'])
plt.show()

# print(gs.to_json(None, orient="records"))
# gs['Close'].plot(figsize=(15, 5))
