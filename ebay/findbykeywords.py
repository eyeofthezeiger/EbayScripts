#!/usr/bin/env python3
from ebaysdk.finding import Connection
from createCSV import *
from request import *

if __name__ == '__main__':
	api = Connection(config_file='ebay.yaml', siteid="EBAY-US")

	request = requestAttributes()

	response = api.execute('findItemsByKeywords', request)

	createCSV(response)

