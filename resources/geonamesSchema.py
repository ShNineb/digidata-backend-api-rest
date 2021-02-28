""" Schema Class
Schema class including its metaclass

@author: Mei, Lara & Sheherazade
"""

from . import ma

class GeonamesSchema(ma.Schema):
    class Meta:
        """
        Returns
        -------
        MApping of class attributes
        """
        fields = ("geonameid", "name", "asciiname", "alternatenames",\
                    "latitude", "longitude", "feature_class",\
                    "feature_code", "country_code", "cc2", \
                    "admin1_code", "admin2_code", "admin3_code", "admin4_code",\
                    "population", "elevation", "dem", "timezone", \
                    "modification", "modified_by")
