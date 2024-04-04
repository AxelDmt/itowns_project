from .citym_cityobject import CityMCityObject, CityMCityObjects

class CityMPlantCover(CityMCityObject):
    """
    Implementation of the Tunnel Model objects from the CityGML model.
    """

    def __init__(self, database_id=None, gml_id=None):
        super().__init__(database_id, gml_id)
        self.objects_type = CityMPlantCovers


class CityMPlantCovers(CityMCityObjects):
    """
    A decorated list of CityMPlantCover type objects.
    """

    object_type = CityMPlantCover

    def __init__(self, features=None):
        super().__init__(features)

    @staticmethod
    def sql_query_objects(plant_covers):
        """
        :param plant_covers: a list of CityMPlantCover type objects that should be sought
                        in the database. When this list is empty, all the objects
                        encountered in the database are returned.

        :return: a string containing the right SQL query that should be executed.
        """
        if not plant_covers:
            # No specific plantcovers were sought. Retrieve all the ones in the database:
            query = "SELECT plant_cover.id, cityobject.gmlid " + \
                    "FROM citydb.plant_cover JOIN citydb.cityobject ON plant_cover.id=cityobject.id"
        else:
            plant_cover_gmlids = [n.get_gml_id() for n in plant_covers]
            plant_cover_gmlids_as_string = "('" + "', '".join(plant_cover_gmlids) + "')"
            query = "SELECT plant_cover.id, cityobject.gmlid " + \
                    "FROM citydb.plant_cover JOIN citydb.cityobject ON plant_cover.id=cityobject.id " + \
                    "WHERE cityobject.gmlid IN " + plant_cover_gmlids_as_string

        return query

    @staticmethod
    def sql_query_geometries(plant_cover_ids_arg, split_surfaces=False):
        """
        :param plant_cover_ids_arg: a formatted list of (city)gml identifier corresponding to
                            objects_type type objects whose geometries are sought.

        :return: a string containing the right SQL query that should be executed.
        """
        if split_surfaces:
            query = \
                "SELECT surface_geometry.id, ST_AsBinary(ST_Multi( " + \
                "surface_geometry.geometry)), " + \
                "objectclass.classname " + \
                "FROM citydb.surface_geometry JOIN citydb.plant_cover " + \
                "ON surface_geometry.root_id=plant_cover.lod2_multi_surface_id " + \
                "JOIN citydb.objectclass ON plant_cover.objectclass_id = objectclass.id " + \
                "WHERE plant_cover.id IN " + plant_cover_ids_arg
        else:
            query = \
                "SELECT plant_cover.id, ST_AsBinary(ST_Multi(ST_Collect( " + \
                "surface_geometry.geometry))), " + \
                "objectclass.classname " + \
                "FROM citydb.surface_geometry JOIN citydb.plant_cover " + \
                "ON surface_geometry.root_id=plant_cover.lod2_multi_surface_id " + \
                "JOIN citydb.objectclass ON plant_cover.objectclass_id = objectclass.id " + \
                "WHERE plant_cover.id IN " + plant_cover_ids_arg + " " + \
                "GROUP BY plant_cover.id, objectclass.classname"

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
            "FROM citydb.surface_geometry JOIN citydb.plant_cover " + \
            "ON surface_geometry.root_id=plant_cover.lod2_multi_surface_id " + \
            "WHERE plant_cover.id = " + str(id) + \
            "GROUP BY plant_cover.id"

        return query
