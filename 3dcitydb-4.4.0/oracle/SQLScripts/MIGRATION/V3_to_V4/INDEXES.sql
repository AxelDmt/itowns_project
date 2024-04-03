-- 3D City Database - The Open Source CityGML Database
-- https://www.3dcitydb.org/
--
-- Copyright 2013 - 2021
-- Chair of Geoinformatics
-- Technical University of Munich, Germany
-- https://www.lrg.tum.de/gis/
--
-- The 3D City Database is jointly developed with the following
-- cooperation partners:
--
-- Virtual City Systems, Berlin <https://vc.systems/>
-- M.O.S.S. Computer Grafik Systeme GmbH, Taufkirchen <http://www.moss.de/>
--
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
--
--     http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.
--

/*************************************************
* create indexes new in v4.0.0
*
**************************************************/
CREATE INDEX BREAKLINE_REL_OBJCLASS_FKX ON BREAKLINE_RELIEF (OBJECTCLASS_ID);

CREATE INDEX BRIDGE_OBJECTCLASS_FKX ON BRIDGE (OBJECTCLASS_ID);

CREATE INDEX BRIDGE_CONSTR_OBJCLASS_FKX ON BRIDGE_CONSTR_ELEMENT (OBJECTCLASS_ID);

CREATE INDEX BRIDGE_FURN_OBJCLASS_FKX ON BRIDGE_FURNITURE (OBJECTCLASS_ID);

CREATE INDEX BRIDGE_ROOM_OBJCLASS_FKX ON BRIDGE_ROOM (OBJECTCLASS_ID);

CREATE INDEX BUILDING_OBJECTCLASS_FKX ON BUILDING (OBJECTCLASS_ID);

CREATE INDEX BLDG_FURN_OBJCLASS_FKX ON BUILDING_FURNITURE (OBJECTCLASS_ID);

CREATE INDEX CITY_FURN_OBJCLASS_FKX ON CITY_FURNITURE (OBJECTCLASS_ID);

CREATE INDEX GROUP_OBJECTCLASS_FKX ON CITYOBJECTGROUP (OBJECTCLASS_ID);

CREATE INDEX GEN_OBJECT_OBJCLASS_FKX ON GENERIC_CITYOBJECT (OBJECTCLASS_ID);

CREATE INDEX LAND_USE_OBJCLASS_FKX ON LAND_USE (OBJECTCLASS_ID);

CREATE INDEX MASSPOINT_REL_OBJCLASS_FKX ON MASSPOINT_RELIEF (OBJECTCLASS_ID);

CREATE INDEX OBJECTCLASS_BASECLASS_FKX ON OBJECTCLASS (BASECLASS_ID);

CREATE INDEX PLANT_COVER_OBJCLASS_FKX ON PLANT_COVER (OBJECTCLASS_ID);

CREATE INDEX RELIEF_FEAT_OBJCLASS_FKX ON RELIEF_FEATURE (OBJECTCLASS_ID);

CREATE INDEX ROOM_OBJECTCLASS_FKX ON ROOM (OBJECTCLASS_ID);

CREATE INDEX SCHEMA_REFERENCING_FKX1 ON SCHEMA_REFERENCING (REFERENCED_ID);

CREATE INDEX SCHEMA_REFERENCING_FKX2 ON SCHEMA_REFERENCING (REFERENCING_ID);

CREATE INDEX SCHEMA_TO_OBJECTCLASS_FKX1 ON SCHEMA_TO_OBJECTCLASS (SCHEMA_ID);

CREATE INDEX TRAN_COMPLEX_OBJCLASS_FKX ON TRANSPORTATION_COMPLEX (OBJECTCLASS_ID);
CREATE INDEX SCHEMA_TO_OBJECTCLASS_FKX2 ON SCHEMA_TO_OBJECTCLASS (OBJECTCLASS_ID);

CREATE INDEX SOL_VEG_OBJ_OBJCLASS_FKX ON SOLITARY_VEGETAT_OBJECT (OBJECTCLASS_ID);

CREATE INDEX TIN_RELIEF_OBJCLASS_FKX ON TIN_RELIEF (OBJECTCLASS_ID);

CREATE INDEX TUNNEL_OBJECTCLASS_FKX ON TUNNEL (OBJECTCLASS_ID);

CREATE INDEX TUNNEL_FURN_OBJCLASS_FKX ON TUNNEL_FURNITURE (OBJECTCLASS_ID);

CREATE INDEX TUN_HSPACE_OBJCLASS_FKX ON TUNNEL_HOLLOW_SPACE (OBJECTCLASS_ID);

CREATE INDEX WATERBODY_OBJCLASS_FKX ON WATERBODY (OBJECTCLASS_ID);

CREATE INDEX CITYOBJ_CREATION_DATE_INX ON CITYOBJECT (CREATION_DATE);

CREATE INDEX CITYOBJ_LAST_MOD_DATE_INX ON CITYOBJECT (LAST_MODIFICATION_DATE);

CREATE INDEX CITYOBJ_TERM_DATE_INX ON CITYOBJECT (TERMINATION_DATE);

CREATE INDEX IMPLICIT_GEOM_INX ON IMPLICIT_GEOMETRY (GMLID, GMLID_CODESPACE);