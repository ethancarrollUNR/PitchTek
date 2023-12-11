def most_airports_func(search):

    # Group the data frame by country
    grouped_data = search._airports.groupby("Country")

    # Group the airports by country and get the size of each group.
    group_sizes = grouped_data.size()

    # Sort the countries by number of airports 
    sorted_groups = group_sizes.sort_values(ascending=False)

    # Keep only the top 25 countries
    sorted_groups = sorted_groups.head(25)

    # Print the top 25 countries
    for group in sorted_groups.index:
        print(group," - ", group_sizes[group])

