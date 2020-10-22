def requestAttributes():

	request = {
	    'keywords': 'Evolutions Booster Box',
	    'itemFilter': [
	        {'name': 'Condition', 'value': 'New'},
	        {'name': 'ListingType', 'value': 'Auction'},
	        {'name': 'MinBids', 'value': '1'}
	    ],
	    'paginationInput': {
	        'entriesPerPage': 100,
	        'pageNumber': 1
	    },
	    'sortOrder': 'PricePlusShippingHighest'
	}

	return request