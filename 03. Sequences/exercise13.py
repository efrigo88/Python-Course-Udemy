data = ["Andromeda - Shrub",
        "Bellflower - Flower",
        "China Pink - Flower",
        "Daffodil - Flower",
        "Evening Primrose - Flower",
        "French Marigold - Flower",
        "Hydrangea - Shrub",
        "Iris - Flower",
        "Japanese Camellia - Shrub",
        "Lavender - Shrub",
        "Lilac- Shrub",
        "Magnolia - Shrub",
        "Peony - Shrub",
        "Queen Anne's Lace - Flower",
        "Red Hot Poker - Flower",
        "Snapdragon - Flower",
        "Sunflower - Flower",
        "Tiger Lily - Flower",
        "Witch Hazel - Shrub"]

flowers = []
shrubs = []

for index, element in enumerate(data):
    if 'shrub' in data[index].casefold():
        shrubs.append(element)
    else:
        flowers.append(element)

print(flowers)
print(shrubs)

