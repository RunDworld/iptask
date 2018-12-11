from faker import Faker
from pydbgen import pydbgen
import csv
import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def rand_data(faker):
	# category = ["TV, Appliances, Electronics", "Men's Fashion","Women's Fashion", "Sports, Fitness, Bags, Luggage","Toys, Baby Products, Kids' Fashion", "Home, Kitchen, Pets", "Car, Motorbike, Industrial", "Books & Audible", "Movies, Music & Video Games", "Gift Cards & Mobile Recharges" ]
	fake_record = {
	"Name" : faker.name(),
	"Email" : faker.email(),
	"Job" : faker.job(),
	"Age": int(random.randint(18,103)),
	"Country" : faker.country(),
	"City": faker.city(),
	"Credit_Card": faker.credit_card_provider(),
	"Money_Spend":random.randint(0,50)
	}
	return fake_record


def create_data():
	pd.set_option('precision', 0)
	fake = Faker()
	r_val = pd.DataFrame()
	

	for i in range(1000):
		rd = rand_data(fake)
		rtemp = pd.DataFrame(rd,index=[i])
		r_val = r_val.append(rd,ignore_index=True)
	r_val['Age'] = r_val['Age'].apply(np.int64)
	r_val['Money_Spend'] = r_val['Money_Spend'].apply(np.int64)
	r_val.to_csv('final.csv',index= False)


def country():
	plt.xlabel("Country") 
	plt.ylabel('Money spend in thousands') 
	plt.title(' Money spend by the users by Country')
	data = pd.read_csv(r"final.csv")
	kl = data.head(20)
	# print(kl)
	plot_data = kl.groupby('Country')['Money_Spend'].sum()
	print(plot_data)
	plt.show(plot_data.plot.bar())

def city():
	plt.xlabel("City") 
	plt.ylabel('Money Spent') 
	plt.title('distribution of money spent in the city of a country')
	data = pd.read_csv(r"final.csv")
	# print(data)
	plotData = data[data.Country=="Suriname"]
	print(plotData)
	plotData = plotData.groupby("City")["Money_Spend"].sum()
	plt.show(plotData.plot.bar())

def credit():
	plt.xlabel("Credit Card company") 
	plt.ylabel('Money_Spend (Amt. from credit cards)') 
	plt.title('Popular credit card used to make payment')
	data = pd.read_csv(r"final.csv")
	plot_data = data.groupby('Credit_Card')['Money_Spend'].sum()
	print(plot_data)
	plt.show(plot_data.plot.bar())
	# plt.show(x) 

def age():
	plt.xlabel("Age Bracket") 
	plt.ylabel('No. of users') 
	plt.title(' Number of credit card user ')
	data = pd.read_csv(r"final.csv")
	plot_data = data.groupby('Credit_Card')['Name'].count()
	# plot_data = plot_data.astype(int)
	print(plot_data)
	plt.show(plot_data.plot.bar())
	# plt.show(x) 


def main():
	pd.set_option('precision', 0)
	create_data()
	# country()
	# city()
	credit()
	age()

if __name__ == '__main__':
	main()