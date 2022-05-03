price_kg_mackerel = float(input())
price_kg_sprat = float(input())
kg_bonito = float(input())
kg_horse_mackerel = float(input())
kg_clams = int(input())

price_bonito = (price_kg_mackerel + price_kg_mackerel * 0.60) * kg_bonito
price_horse_mackerel = (price_kg_sprat + price_kg_sprat * 0.80) * kg_horse_mackerel
price_clams = kg_clams * 7.50

result = price_bonito + price_horse_mackerel + price_clams
print(f'{result:.2f}')
