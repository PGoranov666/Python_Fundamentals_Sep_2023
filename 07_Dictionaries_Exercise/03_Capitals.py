countries = input().split(', ')
capitals = input().split(', ')
# final_information = {countries[index]: capitals[index] for index in range(len(capitals))}
final_information = dict(zip(countries, capitals))
for countries, capitals in final_information.items():
    print(f"{countries} -> {capitals}")
