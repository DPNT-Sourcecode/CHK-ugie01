

# noinspection PyUnusedLocal
# skus = unicode string

# We store prices in a simple dictionary, where the key is the SKU and the value is the price.
prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21,
}

normal_offers = {
    'A': [ (3, 130), (5, 200) ],
    'B': [ (2, 45) ],
    'H': [ (5, 45), (10, 80) ],
    'K': [ (2, 120) ],
    'P': [ (5, 200) ],
    'Q': [ (3, 80) ],
    'V': [ (2, 90), (3, 130) ],
}

# Structure: {SKU: (offer_count, (SKU given, number of free items))}
multi_offers = {
    'E': (2, ('B', 1)),
    'F': (3, ('F', 1)),
    'N': (3, ('M', 1)),
    'R': (3, ('Q', 1)),
    'U': (4, ('U', 1)),
}

# Structure: SKUs in the combo, (number of items, price)
combos = [
    (['S', 'T', 'X', 'Y', 'Z'], (3, 45)),
]

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

    # Sort them by price in descending order
    counts = dict(sorted(counts.items(), key=lambda x: prices[x[0]], reverse=True))

    for combo, (combo_count, combo_price) in combos:
        total_bought = sum(counts[sku] for sku in combo if sku in counts)
        while total_bought >= combo_count:
            total_price += combo_price
            
            removed = 0
            combo = sorted(combo, key=lambda x: prices[x], reverse=True)
            for sku in combo:
                if sku in counts:
                    max_removed = min(counts[sku], combo_count - removed) # Either remove all the items or just the combo count
                    counts[sku] -= max_removed
                    total_bought -= max_removed
                    removed += max_removed
                    if removed == combo_count:
                            break


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
    

