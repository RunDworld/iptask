import requests
from faker import Faker
import csv
import random
import pandas as pd
from matplotlib import pyplot as plt


def data_generator(faker,url):
	r_val = pd.DataFrame()
	for i in range(150):
		ip = faker.ipv4()
		temp_url = url+ip
		r = requests.get(temp_url)
		data = r.json()
		# print(data['country'])
		rcd = createRecord(ip,data)
		rtemp = pd.DataFrame(rcd,index=[i])
		r_val = r_val.append(rcd,ignore_index=True)
	r_val.to_csv('random1.csv',index= False)

		
def createRecord(ip,data):
	fake_record = {
		"IP" : ip,
		"Country" : data["country"],
		"City" : data["city"],
		"Region": data["regionName"],
		"Zip":data["zip"],
		"ISP" :data["isp"]		
		}

	return fake_record

def visualize():
	pd.set_option('precision', 0)
	data = pd.read_csv(r"random1.csv")
	
	plot_data = data.groupby('Country')['City'].count()
	plot_data = plot_data.astype(int)
	draw(plot_data.plot.bar())


def visualize_2():
	data = pd.read_csv(r"random1.csv")
	plotData = data[data.Country=="United States"]
	plotData = plotData.groupby("Region")["Zip"].size()
	print(plotData)
	plt.xlabel("City") 
	plt.ylabel('No. of Requests') 
	plt.title('For USA')
	plt.show(plotData.plot.bar())
	plt.show(plotData.plot.pie())

def draw(x):
	plt.xlabel("Country") 
	plt.ylabel('No. of Requests') 
	# plt.title('Trend in Number of Registrations per Year')
	plt.show(x) 
def main():
	url = "http://ip-api.com/json/"
	fake = Faker()
	# data_generator(fake,url)
	visualize_2()
	visualize()


	

if __name__ == '__main__':
	main()