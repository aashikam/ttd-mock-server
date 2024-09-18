# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IPTargetingRange(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, min_ip: str=None, max_ip: str=None):  # noqa: E501
        """IPTargetingRange - a model defined in Swagger

        :param min_ip: The min_ip of this IPTargetingRange.  # noqa: E501
        :type min_ip: str
        :param max_ip: The max_ip of this IPTargetingRange.  # noqa: E501
        :type max_ip: str
        """
        self.swagger_types = {
            'min_ip': str,
            'max_ip': str
        }

        self.attribute_map = {
            'min_ip': 'MinIP',
            'max_ip': 'MaxIP'
        }
        self._min_ip = min_ip
        self._max_ip = max_ip

    @classmethod
    def from_dict(cls, dikt) -> 'IPTargetingRange':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IPTargetingRange of this IPTargetingRange.  # noqa: E501
        :rtype: IPTargetingRange
        """
        return util.deserialize_model(dikt, cls)

    @property
    def min_ip(self) -> str:
        """Gets the min_ip of this IPTargetingRange.

        The minimum IP address in the targeting range (inclusive).  # noqa: E501

        :return: The min_ip of this IPTargetingRange.
        :rtype: str
        """
        return self._min_ip

    @min_ip.setter
    def min_ip(self, min_ip: str):
        """Sets the min_ip of this IPTargetingRange.

        The minimum IP address in the targeting range (inclusive).  # noqa: E501

        :param min_ip: The min_ip of this IPTargetingRange.
        :type min_ip: str
        """
        if min_ip is None:
            raise ValueError("Invalid value for `min_ip`, must not be `None`")  # noqa: E501

        self._min_ip = min_ip

    @property
    def max_ip(self) -> str:
        """Gets the max_ip of this IPTargetingRange.

        The maximum IP address in the targeting range (inclusive).  # noqa: E501

        :return: The max_ip of this IPTargetingRange.
        :rtype: str
        """
        return self._max_ip

    @max_ip.setter
    def max_ip(self, max_ip: str):
        """Sets the max_ip of this IPTargetingRange.

        The maximum IP address in the targeting range (inclusive).  # noqa: E501

        :param max_ip: The max_ip of this IPTargetingRange.
        :type max_ip: str
        """
        if max_ip is None:
            raise ValueError("Invalid value for `max_ip`, must not be `None`")  # noqa: E501

        self._max_ip = max_ip
