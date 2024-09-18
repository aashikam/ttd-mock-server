# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, amount: float=None, currency_code: str=None, target: float=None):  # noqa: E501
        """CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency - a model defined in Swagger

        :param amount: The amount of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.  # noqa: E501
        :type amount: float
        :param currency_code: The currency_code of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.  # noqa: E501
        :type currency_code: str
        :param target: The target of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.  # noqa: E501
        :type target: float
        """
        self.swagger_types = {
            'amount': float,
            'currency_code': str,
            'target': float
        }

        self.attribute_map = {
            'amount': 'Amount',
            'currency_code': 'CurrencyCode',
            'target': 'Target'
        }
        self._amount = amount
        self._currency_code = currency_code
        self._target = target

    @classmethod
    def from_dict(cls, dikt) -> 'CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CampaignMetricsResponse_GoalInfo_CPAInAdvertiserCurrency of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.  # noqa: E501
        :rtype: CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self) -> float:
        """Gets the amount of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.

        The calculated amount of money for the metric  # noqa: E501

        :return: The amount of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        """Sets the amount of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.

        The calculated amount of money for the metric  # noqa: E501

        :param amount: The amount of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.
        :type amount: float
        """

        self._amount = amount

    @property
    def currency_code(self) -> str:
        """Gets the currency_code of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.

        The currency code of the amount  # noqa: E501

        :return: The currency_code of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code: str):
        """Sets the currency_code of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.

        The currency code of the amount  # noqa: E501

        :param currency_code: The currency_code of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.
        :type currency_code: str
        """

        self._currency_code = currency_code

    @property
    def target(self) -> float:
        """Gets the target of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.

        The target amount for the metric  # noqa: E501

        :return: The target of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.
        :rtype: float
        """
        return self._target

    @target.setter
    def target(self, target: float):
        """Sets the target of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.

        The target amount for the metric  # noqa: E501

        :param target: The target of this CampaignMetricsResponseGoalInfoCPAInAdvertiserCurrency.
        :type target: float
        """

        self._target = target
