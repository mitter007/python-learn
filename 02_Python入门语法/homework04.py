name= "传播智客"
stock_price=19.99
stock_code="003032"
print(f"公司：{name}，股票代码{stock_code}，当前股价：{stock_price}")
stock_price_daily_growth_factor=1.2
growth_days=7
print("每日的增长系数是：%f，经过%d天的增长，股价达到了：%4.2f"%(stock_price_daily_growth_factor,growth_days,stock_price*stock_price_daily_growth_factor**growth_days))
"""
公司：传播智客，股票代码003032，当前股价：19.99
每日的增长系数是：1.200000，经过7天的增长，股价达到了：71.63
"""