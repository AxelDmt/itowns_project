from .citym_cityobject import CityMCityObject, CityMCityObjects

class CityMTransportationComplex(CityMCityObject):
    """
    Implementation of the TransportationComplex Model objects from the CityGML model.
    """

    def __init__(self, database_id=None, gml_id=None):
        super().__init__(database_id, gml_id)
        self.objects_type = CityMTransportationComplexes


class CityMTransportationComplexes(CityMCityObjects):
    """
    A decorated list of CityMTransportationComplex type objects.
    """

    object_type = CityMTransportationComplex

    def __init__(self, features=None):
        super().__init__(features)

    @staticmethod
    def sql_query_objects(transportation_complexes):
        """
        :param transportation_complexes: a list of CityMTransportationComplex type objects that should be sought
                        in the database. When this list is empty, all the objects
                        encountered in the database are returned.

        :return: a string containing the right SQL query that should be executed.
        """
        if not transportation_complexes:
            # No specific transportation complexes were sought. Retrieve all the ones in the database:
            query = "SELECT transportation_complex.id, cityobject.gmlid " + \
                    "FROM citydb.transportation_complex JOIN citydb.cityobject ON transportation_complex.id=cityobject.id"
        else:
            transportation_complex_gmlids = [n.get_gml_id() for n in transportation_complexes]
            transportation_complex_gmlids_as_string = "('" + "', '".join(transportation_complex_gmlids) + "')"
            query = "SELECT transportation_complex.id, cityobject.gmlid " + \
                    "FROM citydb.transportation_complex JOIN citydb.cityobject ON transportation_complex.id=cityobject.id " + \
                    "WHERE cityobject.gmlid IN " + transportation_complex_gmlids_as_string

        return query

    @staticmethod
    def sql_query_geometries(transportation_complex_ids_arg, split_surfaces=False):
        """
        :param transportation_complex_ids_arg: a formatted list of (city)gml identifier corresponding to
                            objects_type type objects whose geometries are sought.

        :return: a string containing the right SQL query that should be executed.
        """
        if split_surfaces:
            query = \
                "SELECT surface_geometry.id, ST_AsBinary(ST_Multi( " + \
                "surface_geometry.geometry)), " + \
                "objectclass.classname " + \
                "FROM citydb.surface_geometry JOIN citydb.traffic_area " + \
                "ON surface_geometry.root_id=ttraffic.lod2_multi_surface_id " + \
                "JOIN citydb.transportation_complex ON traffic_area.transportation_complex_id = transportation_complex.id " + \
                "JOIN citydb.objectclass ON traffic_area.objectclass_id = objectclass.id " + \
                "WHERE transportation_complex.id IN " + transportation_complex_ids_arg
        else:
            query = \
                "SELECT transportation_complex.id, ST_AsBinary(ST_Multi(ST_Collect( " + \
                "surface_geometry.geometry))), " + \
                "objectclass.classname " + \
                "FROM citydb.surface_geometry JOIN citydb.traffic_area " + \
                "ON surface_geometry.root_id=traffic_area.lod2_multi_surface_id " + \
                "JOIN citydb.transportation_complex ON traffic_area.transportation_complex_id = transportation_complex.id " + \
                "JOIN citydb.objectclass ON transportation_complex.objectclass_id = objectclass.id " + \
                "WHERE transportation_complex.id IN " + transportation_complex_ids_arg + " " + \
                "GROUP BY transportation_complex.id, objectclass.classname"

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
            "FROM citydb.surface_geometry JOIN citydb.traffic_area " + \
            "ON surface_geometry.root_id=traffic_area.lod2_multi_surface_id " + \
            "JOIN citydb.transportation_complex ON traffic_area.transportation_complex_id = transportation_complex.id " + \
            "WHERE transportation_complex.id = " + str(id) + \
            "GROUP BY transportation_complex.id"

        return query
