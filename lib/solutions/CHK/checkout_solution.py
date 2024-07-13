

# noinspection PyUnusedLocal
# skus = unicode string

# We store prices in a simple dictionary, where the key is the SKU and the value is the price.
prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
}

normal_offers = {
    'A': [ (3, 130), (5, 200) ],
    'B': [ (2, 45) ],
}

# Structure: {SKU: (offer_count, (SKU given, number of free items))}
multi_offers = {
    'E': (2, ('B', 1))
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

    # First apply the multi-buy offers and update the counts
    for basket_sku in multi_offers:
        if basket_sku in counts:
            offer_count, (free_sku, free_count) = multi_offers[basket_sku]
            if free_sku in counts:
                # Calculate the number of free items to give
                free_items = min(counts[basket_sku] // offer_count, counts[free_sku])
                counts[free_sku] -= free_items
    
    # Now calculate the total price with the free items "removed"
    
    for basket_sku, basket_count in counts.items():

        if basket_sku in normal_offers:
            # Sort the offers in descending order
            sorted_offers = sorted(normal_offers[basket_sku], key=lambda x: x[0], reverse=True)
            for offer in sorted_offers:
                offer_count, offer_price = offer
                while basket_count >= offer_count:
                    total_price += offer_price
                    basket_count -= offer_count

        # Add the remaining items to the total price
        total_price += basket_count * prices[basket_sku]   
        
    return total_price
    


