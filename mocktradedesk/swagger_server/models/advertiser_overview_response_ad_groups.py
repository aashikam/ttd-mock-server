# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.advertiser_overview_response_creatives import AdvertiserOverviewResponseCreatives  # noqa: F401,E501
from swagger_server import util


class AdvertiserOverviewResponseAdGroups(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ad_group_id: str=None, ad_group_name: str=None, description: str=None, is_enabled: bool=None, availability: str=None, creatives: List[AdvertiserOverviewResponseCreatives]=None):  # noqa: E501
        """AdvertiserOverviewResponseAdGroups - a model defined in Swagger

        :param ad_group_id: The ad_group_id of this AdvertiserOverviewResponseAdGroups.  # noqa: E501
        :type ad_group_id: str
        :param ad_group_name: The ad_group_name of this AdvertiserOverviewResponseAdGroups.  # noqa: E501
        :type ad_group_name: str
        :param description: The description of this AdvertiserOverviewResponseAdGroups.  # noqa: E501
        :type description: str
        :param is_enabled: The is_enabled of this AdvertiserOverviewResponseAdGroups.  # noqa: E501
        :type is_enabled: bool
        :param availability: The availability of this AdvertiserOverviewResponseAdGroups.  # noqa: E501
        :type availability: str
        :param creatives: The creatives of this AdvertiserOverviewResponseAdGroups.  # noqa: E501
        :type creatives: List[AdvertiserOverviewResponseCreatives]
        """
        self.swagger_types = {
            'ad_group_id': str,
            'ad_group_name': str,
            'description': str,
            'is_enabled': bool,
            'availability': str,
            'creatives': List[AdvertiserOverviewResponseCreatives]
        }

        self.attribute_map = {
            'ad_group_id': 'AdGroupId',
            'ad_group_name': 'AdGroupName',
            'description': 'Description',
            'is_enabled': 'IsEnabled',
            'availability': 'Availability',
            'creatives': 'Creatives'
        }
        self._ad_group_id = ad_group_id
        self._ad_group_name = ad_group_name
        self._description = description
        self._is_enabled = is_enabled
        self._availability = availability
        self._creatives = creatives

    @classmethod
    def from_dict(cls, dikt) -> 'AdvertiserOverviewResponseAdGroups':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AdvertiserOverviewResponse_AdGroups of this AdvertiserOverviewResponseAdGroups.  # noqa: E501
        :rtype: AdvertiserOverviewResponseAdGroups
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ad_group_id(self) -> str:
        """Gets the ad_group_id of this AdvertiserOverviewResponseAdGroups.

        The ID of the ad group.  # noqa: E501

        :return: The ad_group_id of this AdvertiserOverviewResponseAdGroups.
        :rtype: str
        """
        return self._ad_group_id

    @ad_group_id.setter
    def ad_group_id(self, ad_group_id: str):
        """Sets the ad_group_id of this AdvertiserOverviewResponseAdGroups.

        The ID of the ad group.  # noqa: E501

        :param ad_group_id: The ad_group_id of this AdvertiserOverviewResponseAdGroups.
        :type ad_group_id: str
        """

        self._ad_group_id = ad_group_id

    @property
    def ad_group_name(self) -> str:
        """Gets the ad_group_name of this AdvertiserOverviewResponseAdGroups.

        The name of the ad group.  # noqa: E501

        :return: The ad_group_name of this AdvertiserOverviewResponseAdGroups.
        :rtype: str
        """
        return self._ad_group_name

    @ad_group_name.setter
    def ad_group_name(self, ad_group_name: str):
        """Sets the ad_group_name of this AdvertiserOverviewResponseAdGroups.

        The name of the ad group.  # noqa: E501

        :param ad_group_name: The ad_group_name of this AdvertiserOverviewResponseAdGroups.
        :type ad_group_name: str
        """

        self._ad_group_name = ad_group_name

    @property
    def description(self) -> str:
        """Gets the description of this AdvertiserOverviewResponseAdGroups.

        The description of the ad group.  # noqa: E501

        :return: The description of this AdvertiserOverviewResponseAdGroups.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this AdvertiserOverviewResponseAdGroups.

        The description of the ad group.  # noqa: E501

        :param description: The description of this AdvertiserOverviewResponseAdGroups.
        :type description: str
        """

        self._description = description

    @property
    def is_enabled(self) -> bool:
        """Gets the is_enabled of this AdvertiserOverviewResponseAdGroups.

        Whether the ad group is enabled to spend.  # noqa: E501

        :return: The is_enabled of this AdvertiserOverviewResponseAdGroups.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled: bool):
        """Sets the is_enabled of this AdvertiserOverviewResponseAdGroups.

        Whether the ad group is enabled to spend.  # noqa: E501

        :param is_enabled: The is_enabled of this AdvertiserOverviewResponseAdGroups.
        :type is_enabled: bool
        """

        self._is_enabled = is_enabled

    @property
    def availability(self) -> str:
        """Gets the availability of this AdvertiserOverviewResponseAdGroups.

        The availability state of the ad group.  # noqa: E501

        :return: The availability of this AdvertiserOverviewResponseAdGroups.
        :rtype: str
        """
        return self._availability

    @availability.setter
    def availability(self, availability: str):
        """Sets the availability of this AdvertiserOverviewResponseAdGroups.

        The availability state of the ad group.  # noqa: E501

        :param availability: The availability of this AdvertiserOverviewResponseAdGroups.
        :type availability: str
        """
        allowed_values = ["Available", "Archived"]  # noqa: E501
        if availability not in allowed_values:
            raise ValueError(
                "Invalid value for `availability` ({0}), must be one of {1}"
                .format(availability, allowed_values)
            )

        self._availability = availability

    @property
    def creatives(self) -> List[AdvertiserOverviewResponseCreatives]:
        """Gets the creatives of this AdvertiserOverviewResponseAdGroups.


        :return: The creatives of this AdvertiserOverviewResponseAdGroups.
        :rtype: List[AdvertiserOverviewResponseCreatives]
        """
        return self._creatives

    @creatives.setter
    def creatives(self, creatives: List[AdvertiserOverviewResponseCreatives]):
        """Sets the creatives of this AdvertiserOverviewResponseAdGroups.


        :param creatives: The creatives of this AdvertiserOverviewResponseAdGroups.
        :type creatives: List[AdvertiserOverviewResponseCreatives]
        """

        self._creatives = creatives
