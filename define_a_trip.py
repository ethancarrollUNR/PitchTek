import pandas as pd
import networkx as nx
pd.options.mode.chained_assignment = None  # None or 'raise'

def define_a_trip_func(search):

    #print(search._routes)

    #print(search._airports_extended)
    
    # Extract source and destination columns
    source_destination = search._routes[["Source Airport", "Destination Airport"]]

    # Drop duplicates to prevent a weird error
    search._airports_extended = search._airports_extended.drop_duplicates(subset='IATA')
    
    # Change city name to "city, country"
    search._airports_extended['City'] = search._airports_extended['City'] + " - " + search._airports_extended['Country']

    # Replace airport name with city name
    source_destination['Source Airport'] = source_destination['Source Airport'].map(search._airports_extended.set_index('IATA')['City'])#.fillna(df1['Value1'])
    source_destination['Destination Airport'] = source_destination['Destination Airport'].map(search._airports_extended.set_index('IATA')['City'])#.fillna(df1['Value1'])

    # Drop duplicate rows
    source_destination = source_destination.drop_duplicates()

    # Drop rows that dont have strings as values
    mask = source_destination.map(lambda x: isinstance(x, str))
    source_destination = source_destination[mask.all(axis=1)]

    # Drop rows that contain the same two cities, regardless of order
    source_destination = source_destination.apply(sorted, axis=1)
    source_destination = source_destination[~source_destination.duplicated(keep='first')]
  
    # The last step turns two columns into one column where the two values are in a list.
    # This code splits the list back into two columns,
    source_destination = source_destination.apply(pd.Series)

    print(type(search._airports_extended))
    print(source_destination)