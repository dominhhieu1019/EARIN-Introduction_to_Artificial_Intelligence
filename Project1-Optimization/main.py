from inout import (read_input_file, save_path_png)
from graph import create_graph
from algorithm import find_path


def main():
    cities, w1, w2 = read_input_file("data.txt")
    no_cities = len(cities)
    graph = create_graph(cities)
    path = find_path(graph, no_cities, w1, w2)
    output_file_name = "Graph/" + str(w1) + "_" + str(w2) + ".png"
    save_path_png(output_file_name, path, cities)


if __name__ == "__main__":
    main()
