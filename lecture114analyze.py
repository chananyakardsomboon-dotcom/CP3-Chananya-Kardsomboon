from forex_python.converter import CurrencyRates
from datetime import datetime
import matplotlib.pyplot as plt
from tkinter import messagebox
#date 15 sampling date(one representative exchange rate was callected around the middle of each month.)
#1.ดึงHistorical Exchange Rate
def get_historical_rate(date):
    currency_rate = CurrencyRates() 
    exchange_rate=currency_rate.get_rate('USD','THB',date)
    return exchange_rate

#add month
def next_month(date):
    if date.month==12:
        return date.replace(year=date.year+1,month=1)
    return date.replace(month=date.month+1)

#2.เก็บHistorical Date
start_date=datetime(2023,9,15)
historical_rates=[]
historical_dates=[]
date_obj=start_date
for i in range(36): #ข้อมูลย้อน12เดือนภายใน3ปี แบบไม่ดึงวันหยุด
    rate=get_historical_rate(date_obj)
    historical_rates.append(rate)
    historical_dates.append(date_obj)
    print(date_obj.date(),rate)
    date_obj=next_month(date_obj)
print(historical_rates)


#3.ดึง Current Exchange rate
def get_exchange_rate():
    currency_rate = CurrencyRates()
    exchange_rate=currency_rate.get_rate('USD','THB')
    return exchange_rate
rate=get_exchange_rate()
print("Current rate:",rate)

#4.Calculate Average
def calculate_average(rates):
    average=sum(rates)/len(rates)
    return average
average=calculate_average(historical_rates)
print("Average",average)
    
#5.Analyze Trend
def analyze_trend(rates):
    midpoint=len(rates)//2 #แบ่งข้อมูล

    old_rates=rates[:midpoint] #เอาตัวแรก
    recent_rates=rates[midpoint:] #เอาข้อมูลตัวหลัง

    print("Old rates:",old_rates)
    print("Recent rates:",recent_rates)

    old_average=calculate_average(old_rates)
    recent_average=calculate_average(recent_rates)

    if recent_average>old_average:
        messagebox.showinfo("Trend Analysis","Trend : UP")
    elif recent_average<old_average:
        messagebox.showinfo("Trend Analysis","Trend: DOWN")
    else:
        messagebox.showinfo("Trend Analysis","Trend: STABLE")
analyze_trend(historical_rates)  

#6.Plot Graph
def plot_exchange_rate(dates,rates):
    plt.plot(dates,rates)
    plt.xlabel("Date")
    plt.ylabel("USD/THB")
    plt.title("USD/THB Exchange Rate")
    plt.show()
plot_exchange_rate(historical_dates,historical_rates)  
