

# noinspection PyUnusedLocal
# skus = unicode string

# We store prices in a simple dictionary, where the key is the SKU and the value is the price.
prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

# We store special offers in a dictionary, where the key is the SKU and the value is a tuple containing the number of items in the offer and the price of the offer.
special_offers = {
    'A': (3, 130),
    'B': (2, 45)
}

def checkout(skus):

    total_price = 0

    # Ensure skus in a string
    if not isinstance(skus, str):
        return -1
    # Ensure basket only contains valid skus
    if not all(sku in prices for sku in skus):
        return -1

    # Count the number of each item in the basket
    counts = {sku: skus.count(sku) for sku in set(skus)}

    # Check for special offers
    for sku, count in counts.items():

        # If the item has a special offer, apply it
        if sku in special_offers:
            offer_count, offer_price = special_offers[sku]

            # Apply the offer as many times as possible (i.e. until the count is less than the offer count - the remainder will be charged at the normal price)
            while count >= offer_count:
                total_price += offer_price
                count -= offer_count
            # Charge the remainder at the normal price
            total_price += count * prices[sku]
        else:
            # If the item does not have a special offer, charge the normal price
            total_price += count * prices[sku]

    return total_price
    

