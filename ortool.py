"""Simple travelling salesman problem between cities."""

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import pandas as pd
import sqlite3 as sql

def obj_func(distance_matrix, actual_sequence):
    # TODO: complete
    return obj_val

def create_data_model(con,route_id):
    """Stores the data for the problem."""
    data = {}
    df1 = pd.read_sql('SELECT * FROM travel_times WHERE route_id = "{0}";'.format(route_id), con)
    #df1_data = df1.pivot().values
    data['distance_matrix'] =  df1.pivot(index='stop1',columns='stop2',values='travel_time').values
    print('data loaded for {0}'.format(route_id))
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data


def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print('Objective: {} miles'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route for vehicle 0:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Route distance: {}miles\n'.format(route_distance)


def main(route_id, con):
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model(con, route_id)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters() # TODO: change parameters
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(manager, routing, solution)


if __name__ == '__main__':
    con = sql.connect('amazon_last_mile_route.db')
    df_route = pd.read_sql('SELECT * FROM route',con)
    for index in df_route.index:
        route_id = df_route.loc[index,'route_id']
        main(route_id, con)
        break


    #for route_id in df_route['route_id']:
    #    main(route_id, con)