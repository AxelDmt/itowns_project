from .citym_cityobject import CityMCityObject, CityMCityObjects

class CityMFurniture(CityMCityObject):
    """
    Implementation of the Tunnel Model objects from the CityGML model.
    """

    def __init__(self, database_id=None, gml_id=None):
        super().__init__(database_id, gml_id)
        self.objects_type = CityMFurnitures


class CityMFurnitures(CityMCityObjects):
    """
    A decorated list of CityMFurniture type objects.
    """

    object_type = CityMFurniture

    def __init__(self, features=None):
        super().__init__(features)

    @staticmethod
    def sql_query_objects(city_furnitures):
        """
        :param city_furnitures: a list of CityMFurniture type objects that should be sought
                        in the database. When this list is empty, all the objects
                        encountered in the database are returned.

        :return: a string containing the right SQL query that should be executed.
        """
        if not city_furnitures:
            # No specific city_furnitures were sought. Retrieve all the ones in the database:
            query = "SELECT city_furniture.id, cityobject.gmlid " + \
                    "FROM citydb.city_furniture JOIN citydb.cityobject ON city_furniture.id=cityobject.id"
        else:
            city_furniture_gmlids = [n.get_gml_id() for n in city_furnitures]
            city_furniture_gmlids_as_string = "('" + "', '".join(city_furniture_gmlids) + "')"
            query = "SELECT city_furniture.id, cityobject.gmlid " + \
                    "FROM citydb.city_furniture JOIN citydb.cityobject ON city_furniture.id=cityobject.id " + \
                    "WHERE cityobject.gmlid IN " + city_furniture_gmlids_as_string

        return query

    @staticmethod
    def sql_query_geometries(city_furniture_ids_arg, split_surfaces=False):
        """
        :param city_furniture_ids_arg: a formatted list of (city)gml identifier corresponding to
                            objects_type type objects whose geometries are sought.

        :return: a string containing the right SQL query that should be executed.
        """
        if split_surfaces:
            query = \
                "SELECT surface_geometry.id, ST_AsBinary(ST_Multi( " + \
                "surface_geometry.geometry)), " + \
                "objectclass.classname " + \
                "FROM citydb.surface_geometry JOIN citydb.city_furniture " + \
                "ON surface_geometry.root_id=city_furniture.lod2_brep_id " + \
                "JOIN citydb.objectclass ON city_furniture.objectclass_id = objectclass.id " + \
                "WHERE city_furniture.id IN " + city_furniture_ids_arg
        else:
            query = \
                "SELECT city_furniture.id, ST_AsBinary(ST_Multi(ST_Collect( " + \
                "surface_geometry.geometry))), " + \
                "objectclass.classname " + \
                "FROM citydb.surface_geometry JOIN citydb.city_furniture " + \
                "ON surface_geometry.root_id=city_furniture.lod2_brep_id " + \
                "JOIN citydb.objectclass ON city_furniture.objectclass_id = objectclass.id " + \
                "WHERE city_furniture.id IN " + city_furniture_ids_arg + " " + \
                "GROUP BY city_furniture.id, objectclass.classname"

        return query

    @staticmethod
    def sql_query_centroid(id):
        """
        param id: the ID of the cityGML object
        return: the [x, y, z] coordinates of the centroid of the cityGML object
        """

        query = \
            "SELECT " + \
            "ST_X(ST_3DClosestPoint(ST_Multi(ST_Collect(surface_geometry.geometry)) " + \
            ",ST_Centroid(ST_Multi(ST_Collect(surface_geometry.geometry))))), " + \
            "ST_Y(ST_3DClosestPoint(ST_Multi(ST_Collect(surface_geometry.geometry)) " + \
            ",ST_Centroid(ST_Multi(ST_Collect(surface_geometry.geometry))))), " + \
            "ST_Z(ST_3DClosestPoint(ST_Multi(ST_Collect(surface_geometry.geometry)) " + \
            ",ST_Centroid(ST_Multi(ST_Collect(surface_geometry.geometry))))) " + \
            "FROM citydb.surface_geometry JOIN citydb.city_furniture " + \
            "ON surface_geometry.root_id=city_furniture.lod2_brep_id " + \
            "WHERE city_furniture.id = " + str(id) + \
            "GROUP BY city_furniture.id"

        return query
