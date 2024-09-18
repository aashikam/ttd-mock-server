import connexion
import six

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
from swagger_server import util


def v3_adgroup_post(body):  # noqa: E501
    """Create a new Ad Group

    This endpoint allows you to create a new Ad Group within a campaign. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: AdGroupResponse
    """
    if connexion.request.is_json:
        body = AdGroupRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v3_advertiser_advertiser_id_get(advertiser_id):  # noqa: E501
    """Retrieve an advertiser by ID

    Get details of an existing advertiser using the advertiser&#x27;s platform ID. # noqa: E501

    :param advertiser_id: The platform ID of the advertiser to retrieve.
    :type advertiser_id: str

    :rtype: AdvertiserDetailsResponse
    """
    return 'do some magic!'


def v3_advertiser_post(body):  # noqa: E501
    """Create a new advertiser

    Create a new advertiser entity with the necessary details for attribution and domain address. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: AdvertiserResponse
    """
    if connexion.request.is_json:
        body = AdvertiserRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v3_bidlist_post(body):  # noqa: E501
    """Create a bid list

    Create a bid list, returning the created bid list. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: BidListRequest
    """
    if connexion.request.is_json:
        body = BidListRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v3_campaign_campaign_id_metrics_get(campaign_id):  # noqa: E501
    """Get metrics for an existing campaign

    Retrieve the performance metrics for a campaign, including spend, impressions, and other key metrics. # noqa: E501

    :param campaign_id: The ID of the campaign to retrieve metrics for
    :type campaign_id: str

    :rtype: CampaignMetricsResponse
    """
    return 'do some magic!'


def v3_campaign_post(body):  # noqa: E501
    """Create a new campaign

    Create a new campaign entity with the necessary details such as name, budget, and start date. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CampaignResponse
    """
    if connexion.request.is_json:
        body = CampaignRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v3_creative_post(body):  # noqa: E501
    """Create a new creative

    Create a new creative under an advertiser. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreativeRequest
    """
    if connexion.request.is_json:
        body = CreativeRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v3_dmp_firstparty_advertiser_post(body):  # noqa: E501
    """Get First Party Data for Advertisers

    Retrieve the First Party Data matching the provided query for an advertiser. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: FirstPartyAdvertiserResponse
    """
    if connexion.request.is_json:
        body = FirstPartyAdvertiserRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v3_frequency_config_post(body):  # noqa: E501
    """Create a frequency configuration

    Creates a frequency configuration, associating entities to increment the counter and applying the frequency configuration to bid lists. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = FrequencyConfigRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v3_iptargetinglist_post(body):  # noqa: E501
    """Create a new IP Targeting List

    Create a new IP Targeting List for an advertiser. Each Advertiser has a quota for the number of IP targeting ranges they may include across all of their IP Targeting Lists. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: IPTargetingListResponse
    """
    if connexion.request.is_json:
        body = IPTargetingListRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v3_myreports_reportschedule_schedule_id_get(schedule_id):  # noqa: E501
    """Get a report schedule

    Retrieve details of a report schedule by its ID. # noqa: E501

    :param schedule_id: The ID of the report schedule to retrieve.
    :type schedule_id: int

    :rtype: ReportScheduleResponse
    """
    return 'do some magic!'


def v3_overview_advertiser_advertiser_id_get(advertiser_id):  # noqa: E501
    """Get an advertiser overview

    Retrieve an overview of an advertiser, including descendant relationships for campaigns, ad groups, and creatives. # noqa: E501

    :param advertiser_id: The platform ID of the advertiser.
    :type advertiser_id: str

    :rtype: AdvertiserOverviewResponse
    """
    return 'do some magic!'


def v3_seller_query_post(body):  # noqa: E501
    """Retrieve a paged, filterable list of sellers

    Retrieve a paged, filterable list of sellers, seller domains, and whether they can be targeted as a SellerDomain in a bid list. Only returns sellers that have spent through our platform. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SellerQueryResponse
    """
    if connexion.request.is_json:
        body = SellerQueryRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v3_trackingtag_tracking_tag_id_get(tracking_tag_id):  # noqa: E501
    """Get a tracking tag

    Retrieve a tracking tag by its ID. # noqa: E501

    :param tracking_tag_id: The ID of the tracking tag to retrieve.
    :type tracking_tag_id: str

    :rtype: TrackingTagResponse
    """
    return 'do some magic!'


def v3_universalforecasting_generate_post(body):  # noqa: E501
    """Generate a forecast

    Generate a forecast based on the data available at the time of the request. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = UniversalForecastingRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
