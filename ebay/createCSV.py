import csv
from datetime import datetime

now = datetime.now()
dt_formatted = now.strftime("%d/%m/%Y %H:%M:%S")

def createCSV(response):

	with open('Output/box_prices.csv', 'w', newline='', encoding='utf-8') as file:
		writer = csv.writer(file)
		writer.writerow([dt_formatted])
		writer.writerow(["URL", "Title", "Price", "Bids", "Time Left"])
		for item in response.reply.searchResult.item:
			writer.writerow([item.viewItemURL, item.title, item.sellingStatus.convertedCurrentPrice.value, item.sellingStatus.bidCount, item.sellingStatus.timeLeft])