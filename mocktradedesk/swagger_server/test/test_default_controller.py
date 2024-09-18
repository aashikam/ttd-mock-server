# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.ad_group_request import AdGroupRequest  # noqa: E501
from swagger_server.models.ad_group_response import AdGroupResponse  # noqa: E501
from swagger_server.models.advertiser_details_response import AdvertiserDetailsResponse  # noqa: E501
from swagger_server.models.advertiser_overview_response import AdvertiserOverviewResponse  # noqa: E501
from swagger_server.models.advertiser_request import AdvertiserRequest  # noqa: E501
from swagger_server.models.advertiser_response import AdvertiserResponse  # noqa: E501
from swagger_server.models.bid_list_request import BidListRequest  # noqa: E501
from swagger_server.models.campaign_metrics_response import CampaignMetricsResponse  # noqa: E501
from swagger_server.models.campaign_request import CampaignRequest  # noqa: E501
from swagger_server.models.campaign_response import CampaignResponse  # noqa: E501
from swagger_server.models.creative_request import CreativeRequest  # noqa: E501
from swagger_server.models.first_party_advertiser_request import FirstPartyAdvertiserRequest  # noqa: E501
from swagger_server.models.first_party_advertiser_response import FirstPartyAdvertiserResponse  # noqa: E501
from swagger_server.models.frequency_config_request import FrequencyConfigRequest  # noqa: E501
from swagger_server.models.ip_targeting_list_request import IPTargetingListRequest  # noqa: E501
from swagger_server.models.ip_targeting_list_response import IPTargetingListResponse  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.report_schedule_response import ReportScheduleResponse  # noqa: E501
from swagger_server.models.seller_query_request import SellerQueryRequest  # noqa: E501
from swagger_server.models.seller_query_response import SellerQueryResponse  # noqa: E501
from swagger_server.models.tracking_tag_response import TrackingTagResponse  # noqa: E501
from swagger_server.models.universal_forecasting_request import UniversalForecastingRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_v3_adgroup_post(self):
        """Test case for v3_adgroup_post

        Create a new Ad Group
        """
        body = AdGroupRequest()
        response = self.client.open(
            '/v3//v3/adgroup',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_advertiser_advertiser_id_get(self):
        """Test case for v3_advertiser_advertiser_id_get

        Retrieve an advertiser by ID
        """
        response = self.client.open(
            '/v3//v3/advertiser/{advertiserId}'.format(advertiser_id='advertiser_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_advertiser_post(self):
        """Test case for v3_advertiser_post

        Create a new advertiser
        """
        body = AdvertiserRequest()
        response = self.client.open(
            '/v3//v3/advertiser',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_bidlist_post(self):
        """Test case for v3_bidlist_post

        Create a bid list
        """
        body = BidListRequest()
        response = self.client.open(
            '/v3//v3/bidlist',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_campaign_campaign_id_metrics_get(self):
        """Test case for v3_campaign_campaign_id_metrics_get

        Get metrics for an existing campaign
        """
        response = self.client.open(
            '/v3//v3/campaign/{campaignId}/metrics'.format(campaign_id='campaign_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_campaign_post(self):
        """Test case for v3_campaign_post

        Create a new campaign
        """
        body = CampaignRequest()
        response = self.client.open(
            '/v3//v3/campaign',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_creative_post(self):
        """Test case for v3_creative_post

        Create a new creative
        """
        body = CreativeRequest()
        response = self.client.open(
            '/v3//v3/creative',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_dmp_firstparty_advertiser_post(self):
        """Test case for v3_dmp_firstparty_advertiser_post

        Get First Party Data for Advertisers
        """
        body = FirstPartyAdvertiserRequest()
        response = self.client.open(
            '/v3//v3/dmp/firstparty/advertiser',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_frequency_config_post(self):
        """Test case for v3_frequency_config_post

        Create a frequency configuration
        """
        body = FrequencyConfigRequest()
        response = self.client.open(
            '/v3//v3/frequency/config',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_iptargetinglist_post(self):
        """Test case for v3_iptargetinglist_post

        Create a new IP Targeting List
        """
        body = IPTargetingListRequest()
        response = self.client.open(
            '/v3//v3/iptargetinglist',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_myreports_reportschedule_schedule_id_get(self):
        """Test case for v3_myreports_reportschedule_schedule_id_get

        Get a report schedule
        """
        response = self.client.open(
            '/v3//v3/myreports/reportschedule/{scheduleId}'.format(schedule_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_overview_advertiser_advertiser_id_get(self):
        """Test case for v3_overview_advertiser_advertiser_id_get

        Get an advertiser overview
        """
        response = self.client.open(
            '/v3//v3/overview/advertiser/{advertiserId}'.format(advertiser_id='advertiser_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_seller_query_post(self):
        """Test case for v3_seller_query_post

        Retrieve a paged, filterable list of sellers
        """
        body = SellerQueryRequest()
        response = self.client.open(
            '/v3//v3/seller/query',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_trackingtag_tracking_tag_id_get(self):
        """Test case for v3_trackingtag_tracking_tag_id_get

        Get a tracking tag
        """
        response = self.client.open(
            '/v3//v3/trackingtag/{trackingTagId}'.format(tracking_tag_id='tracking_tag_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_universalforecasting_generate_post(self):
        """Test case for v3_universalforecasting_generate_post

        Generate a forecast
        """
        body = UniversalForecastingRequest()
        response = self.client.open(
            '/v3//v3/universalforecasting/generate',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
