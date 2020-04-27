import matplotlib.pyplot as plt


def read_input_file(input_file):
    """Read the data cities file and class id of each point.

    Args:
        input_file (str): Data file

    Returns:
        tuple: Returns list of cities, w1 and w2 
    """
    cities = []
    with open(input_file, 'r') as f:
        for i, line in enumerate(f.readlines()):
            x, y = list(map(float, line.split()))
            cities.append((i, x, y))
    j, w1, w2 = cities.pop()

    return cities, w1, w2


def save_path_png(filename, edges, points):
    """Save path into a png file
    Args:
        filename (str): Output filename
        edges (list): List of tuple representing edges as (src, dst, weight)
        points (list): List of tuple representing points as (x, y)
    """
    for src, dst, _ in edges:
        p, q = [points[src][1], points[dst][1]], [
            points[src][2], points[dst][2]]
        plt.plot(p, q, marker='o', ms=5, mfc='red', mec='red', color='black')
    plt.grid()
    plt.savefig(filename, dpi=300)
