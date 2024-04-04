from .citym_cityobject import CityMCityObject, CityMCityObjects

class CityMTunnel(CityMCityObject):
    """
    Implementation of the Tunnel Model objects from the CityGML model.
    """

    def __init__(self, database_id=None, gml_id=None):
        super().__init__(database_id, gml_id)
        self.objects_type = CityMTunnels


class CityMTunnels(CityMCityObjects):
    """
    A decorated list of CityMTunnel type objects.
    """

    object_type = CityMTunnel

    def __init__(self, features=None):
        super().__init__(features)

    @staticmethod
    def sql_query_objects(tunnels):
        """
        :param tunnels: a list of CityMTunnel type objects that should be sought
                        in the database. When this list is empty, all the objects
                        encountered in the database are returned.

        :return: a string containing the right SQL query that should be executed.
        """
        if not tunnels:
            # No specific tunnelss were sought. Retrieve all the ones in the database:
            query = "SELECT tunnel.id, cityobject.gmlid " + \
                    "FROM citydb.tunnel JOIN citydb.cityobject ON tunnel.id=cityobject.id"
        else:
            tunnel_gmlids = [n.get_gml_id() for n in tunnels]
            tunnel_gmlids_as_string = "('" + "', '".join(tunnel_gmlids) + "')"
            query = "SELECT tunnel.id, cityobject.gmlid " + \
                    "FROM citydb.tunnel JOIN citydb.cityobject ON tunnel.id=cityobject.id " + \
                    "WHERE cityobject.gmlid IN " + tunnel_gmlids_as_string

        return query

    @staticmethod
    def sql_query_geometries(tunnel_ids_arg, split_surfaces=False):
        """
        :param tunnel_ids_arg: a formatted list of (city)gml identifier corresponding to
                            objects_type type objects whose geometries are sought.

        :return: a string containing the right SQL query that should be executed.
        """
        if split_surfaces:
            query = \
                "SELECT surface_geometry.id, ST_AsBinary(ST_Multi( " + \
                "surface_geometry.geometry)), " + \
                "objectclass.classname " + \
                "FROM citydb.surface_geometry JOIN citydb.tunnel_thematic_surface " + \
                "ON surface_geometry.root_id=tunnel_thematic_surface.lod2_multi_surface_id " + \
                "JOIN citydb.tunnel ON tunnel_thematic_surface.tunnel_id = tunnel.id " + \
                "JOIN citydb.objectclass ON tunnel_thematic_surface.objectclass_id = objectclass.id " + \
                "WHERE tunnel.id IN " + tunnel_ids_arg
        else:
            query = \
                "SELECT tunnel.id, ST_AsBinary(ST_Multi(ST_Collect( " + \
                "surface_geometry.geometry))), " + \
                "objectclass.classname " + \
                "FROM citydb.surface_geometry JOIN citydb.tunnel_thematic_surface " + \
                "ON surface_geometry.root_id=tunnel_thematic_surface.lod2_multi_surface_id " + \
                "JOIN citydb.tunnel ON tunnel_thematic_surface.tunnel_id = tunnel.id " + \
                "JOIN citydb.objectclass ON tunnel.objectclass_id = objectclass.id " + \
                "WHERE tunnel.id IN " + tunnel_ids_arg + " " + \
                "GROUP BY tunnel.id, objectclass.classname"

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
            "FROM citydb.surface_geometry JOIN citydb.tunnel_thematic_surface " + \
            "ON surface_geometry.root_id=tunnel_thematic_surface.lod2_multi_surface_id " + \
            "JOIN citydb.tunnel ON tunnel_thematic_surface.tunnel_id = tunnel.id " + \
            "WHERE tunnel.id = " + str(id) + \
            "GROUP BY tunnel.id"

        return query
