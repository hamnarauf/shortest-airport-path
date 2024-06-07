from graph import Graph
import json
from dijkstra import dijkstra


def get_user_input():
    """Gets the start and end airports from the user.

    Returns:
        Tuple[str, str]: The start and end airports.
    """
    start_airport = input('Enter the start airport: ')
    end_airport = input('Enter the end airport: ')

    return start_airport, end_airport


def calculate_shortest_path(airports, start, end):
    """Calculates the shortest path from the start airport to the end airport.

    Args:
        airports (List[Dict[str, str]]): A list of dictionaries representing the airports and their connections.
        start (str): The start airport.
        end (str): The end airport.

    Returns:
        List[str]: A list of airports in the shortest path from the start airport to the end airport.
        float: The cost of the shortest path.
    """

    airports_graph = Graph()

    for airport in airports:
        airports_graph.add_edge(
            airport['start'], airport['end'], airport['cost'])

    return dijkstra(airports_graph.graph, start, end)


def main():
    start_airport, end_airport = get_user_input()

    # Load the data from airports_data.json
    with open('data/airports_data.json') as f:
        airports = json.load(f)

        path, cost = calculate_shortest_path(
            airports, start_airport, end_airport)

        print("\nShortest Path:", path)
        print("Cost:", cost)


if __name__ == '__main__':
    main()
