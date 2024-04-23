import numpy as np
from binascii import a2b_hex
from shapely.wkb import loads as wkb_loads

def apply_transfo_to_point(matrix, point_obj, point_reel):
    """
    Apply transformation to a 3D object's local referential to get in a global referential.
    :param matrix: a 4x4 transformation matrix.
    :param point_obj: coordinates from the 3D object's local referential.
    :param point_reel: coordinates of the 3D objects in the global referential (in WKB).
    :return: Transformed point coordinates as a tuple (x, y, z).
    """
    point_homogeneous = np.array([[point_obj[0]], [point_obj[1]], [point_obj[2]], [1.0]])
    matrix_4x4 = np.array(matrix).reshape((4, 4))
    transformed_point = np.dot(matrix_4x4, point_homogeneous)

    geom = wkb_loads(a2b_hex(point_reel))
    x, y, z = geom.x, geom.y, geom.z

    res = (transformed_point[0][0] + x, transformed_point[1][0] + y, transformed_point[2][0] + z)

    return res

def transform_obj_file(input_file, output_file, matrix, point_reel):
    """
    Transform a 3D object (.obj) file based on a given transformation matrix and real-world coordinates.

    :param input_file: The path to the input 3D object file.
    :param output_file: The path to save the transformed 3D object file.
    :param matrix: A 4x4 transformation matrix.
    :param point_reel: Coordinates of the 3D object in the global referential (in WKB).
    :return: None
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()

    transformed_points = []

    for line in lines:
        if line.startswith('v '):
            vertices = line.split()[1:]
            point_obj = [float(coord) for coord in vertices]
            # Assuming point_reel is available or can be calculated somehow
            transformed_point = apply_transfo_to_point(matrix, point_obj, point_reel)
            transformed_points.append(transformed_point)
        else:
            # For lines other than vertex lines, just keep them as is
            transformed_points.append(line)

    with open(output_file, 'w') as f:
        for item in transformed_points:
            if isinstance(item, tuple):
                f.write("v " + " ".join(str(coord) for coord in item) + "\n")
            else:
                f.write(item)


# Example usage:
matrix = [                  
    1.0, 0.0, 0.0, 0.0,
    0.0, 1.0, 0.0, 0.0,        #Write your matrix as a simple List
    0.0, 0.0, 1.0, 1.0,
    0.0, 0.0, 0.0, 1.0
]
input_file = 'path/to/file.obj'  # Path to your .obj file
point_reel = "your wkb coordinate in hexadecimal"
output_file = 'output/output.obj'
transform_obj_file(input_file, output_file, matrix, point_reel)


