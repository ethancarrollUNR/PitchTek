
def airlines_with_code_share_func(search):


    routes_with_codeshare = search._routes[search._routes['Codeshare'] == "Y"]

    grouped_data = routes_with_codeshare.groupby("Airline ID")


    for key in grouped_data.groups.keys():

        matching_row = search._airlines[search._airlines['Airline ID'] == key]

        cell_value = matching_row["Name"].iloc[0]

        print(cell_value)
