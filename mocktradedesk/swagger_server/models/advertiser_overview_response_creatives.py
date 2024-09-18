# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AdvertiserOverviewResponseCreatives(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, creative_id: str=None, creative_name: str=None, description: str=None):  # noqa: E501
        """AdvertiserOverviewResponseCreatives - a model defined in Swagger

        :param creative_id: The creative_id of this AdvertiserOverviewResponseCreatives.  # noqa: E501
        :type creative_id: str
        :param creative_name: The creative_name of this AdvertiserOverviewResponseCreatives.  # noqa: E501
        :type creative_name: str
        :param description: The description of this AdvertiserOverviewResponseCreatives.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'creative_id': str,
            'creative_name': str,
            'description': str
        }

        self.attribute_map = {
            'creative_id': 'CreativeId',
            'creative_name': 'CreativeName',
            'description': 'Description'
        }
        self._creative_id = creative_id
        self._creative_name = creative_name
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'AdvertiserOverviewResponseCreatives':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AdvertiserOverviewResponse_Creatives of this AdvertiserOverviewResponseCreatives.  # noqa: E501
        :rtype: AdvertiserOverviewResponseCreatives
        """
        return util.deserialize_model(dikt, cls)

    @property
    def creative_id(self) -> str:
        """Gets the creative_id of this AdvertiserOverviewResponseCreatives.

        The ID of the creative.  # noqa: E501

        :return: The creative_id of this AdvertiserOverviewResponseCreatives.
        :rtype: str
        """
        return self._creative_id

    @creative_id.setter
    def creative_id(self, creative_id: str):
        """Sets the creative_id of this AdvertiserOverviewResponseCreatives.

        The ID of the creative.  # noqa: E501

        :param creative_id: The creative_id of this AdvertiserOverviewResponseCreatives.
        :type creative_id: str
        """

        self._creative_id = creative_id

    @property
    def creative_name(self) -> str:
        """Gets the creative_name of this AdvertiserOverviewResponseCreatives.

        The name of the creative.  # noqa: E501

        :return: The creative_name of this AdvertiserOverviewResponseCreatives.
        :rtype: str
        """
        return self._creative_name

    @creative_name.setter
    def creative_name(self, creative_name: str):
        """Sets the creative_name of this AdvertiserOverviewResponseCreatives.

        The name of the creative.  # noqa: E501

        :param creative_name: The creative_name of this AdvertiserOverviewResponseCreatives.
        :type creative_name: str
        """

        self._creative_name = creative_name

    @property
    def description(self) -> str:
        """Gets the description of this AdvertiserOverviewResponseCreatives.

        The description of the creative.  # noqa: E501

        :return: The description of this AdvertiserOverviewResponseCreatives.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this AdvertiserOverviewResponseCreatives.

        The description of the creative.  # noqa: E501

        :param description: The description of this AdvertiserOverviewResponseCreatives.
        :type description: str
        """

        self._description = description
