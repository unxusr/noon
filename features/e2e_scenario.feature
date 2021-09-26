Feature: EndToEnd Scenario
	Scenario: Signing in to Noon and make purchase 
		Given i open noon.com
			And i create new user
		Then i logged in successfully
		And i can search for item
		And i can sort the result from high to low price
		And i can select an item to review its specs
		And i can add an item to wish list by liking it
		And i moved to the wish list
		And i can move the item to the cart
		And i click on checkout button
		And i confirm my location
		And i insert address details
		And i save the address
		


