import ballerina/http;

// Define types based on the schemas from the OpenAPI specification

// Advertiser Types
type AdvertiserRequest record {|
    string AdvertiserName;
    int AttributionClickLookbackWindowInSeconds;
    int AttributionImpressionLookbackWindowInSeconds;
    int ClickDedupWindowInSeconds;
    int ConversionDedupWindowInSeconds;
    int DefaultRightMediaOfferTypeId;
    string DomainAddress;
    string PartnerId;
|};

type AdvertiserResponse record {|
    string AdvertiserId;
|};

type AdvertiserDetailsResponse record {|
    string AdvertiserId;
    string AdvertiserName;
    int AttributionClickLookbackWindowInSeconds;
    int AttributionImpressionLookbackWindowInSeconds;
    int ClickDedupWindowInSeconds;
    int ConversionDedupWindowInSeconds;
    int DefaultRightMediaOfferTypeId;
    string DomainAddress;
    string PartnerId;
|};

// Ad Group Types
type AdGroupRequest record {|
    string AdGroupName;
    string CampaignId;
    record {|
        float BudgetInAdvertiserCurrency;
        float? DailyTargetInAdvertiserCurrency?;
    |} BudgetSettings;
    string PacingMode;
    boolean? IsEnabled?;
    string[]? CreativeIds?;
|};

type AdGroupResponse record {|
    string AdGroupId;
    string AdGroupName;
    string CampaignId;
|};

// Creative Types
type CreativeRequest record {|
    string AdvertiserId;
    string CreativeName;
    string? Availability?;
    string? Description?;
    string ClickthroughUrl;
|};

// Campaign Types
type CampaignRequest record {|
    string AdvertiserId;
    string CampaignName;
    record {|
        float Amount;
        string CurrencyCode;
    |} Budget;
    string StartDate;
    string? EndDate?;
    record {|
        string GoalType;
        float Amount;
        string CurrencyCode;
    |}? PrimaryGoal?;
    string[]? TrackingTags?;
|};

type CampaignResponse record {|
    string CampaignId;
    string AdvertiserId;
    string CampaignName;
    record {|
        float Amount;
        string CurrencyCode;
    |} Budget;
    string StartDate;
    string? EndDate?;
|};

type CampaignMetricsResponse record {|
    int CampaignFlightId;
    string CampaignId;
    record {|
        record {|
            float Amount;
            string CurrencyCode;
            float Target;
        |} CPAInAdvertiserCurrency;
        record {|
            float Amount;
            string CurrencyCode;
            float Target;
        |} CPCInAdvertiserCurrency;
        record {|
            float Amount;
            float Target;
        |} CTRInPercent;
        int Impressions;
        string LastCalculatedAt;
    |} GoalInfo;
    float CurrentSpendInAdvertiserCurrency;
    float FlightBudgetInAdvertiserCurrency;
    float ProjectedSpendInAdvertiserCurrency;
|};

// First Party Advertiser Types
type FirstPartyAdvertiserRequest record {|
    string AdvertiserId;
    int PageSize;
    int PageStartIndex;
    string[]? DataTypes?;
    string[]? LookAlikeModelBuildStatuses?;
    string[]? LookAlikeModelEligibilities?;
    string[]? LookAlikeModelResultStatuses?;
    string[]? SearchTerms?;
    record {|
        string FieldId;
        boolean Ascending;
    |}[]? SortFields?;
    int? UniqueCountMaximum?;
    int? UniqueCountMinimum?;
|};

type FirstPartyAdvertiserResponse record {|
    record {|
        int ActiveHouseholdCount;
        int ActiveIDsCount;
        boolean? ActiveIDsCountExpanded?;
        string DataType;
        int FirstPartyDataId;
        record {|
            string? LastGenerationDateUTC?;
            string LastRequestDateUTC;
            string LookAlikeModelBuildStatus;
            string LookAlikeModelResultStatus;
            string LookAlikeModelEligibility;
        |} LookAlikeModelDetails;
        string? Name?;
        int ActivePersonsCount;
    |}[] Result;
    int ResultCount;
    int TotalFilteredCount;
    int TotalUnfilteredCount;
|};

// Bid List Types
type BidListRequest record {|
    record {|
        float BidAdjustment;
        string DomainFragment;
        string? AdBugPageQualityCategoryId?;
        string? AdFormatId?;
    |}[] BidLines;
    string ResolutionType;
    string BidListAdjustmentType;
    string BidListOwner;
    string Name;
|};

// Frequency Configuration Types
type FrequencyConfigRequest record {|
    record {|
        record {|
            record {|
                int Min;
                int Max;
            |} Range;
            float BidAdjustment;
        |}[] BidLines;
        string VolumeControlPriority;
        string[]? AssociatedAdGroups?;
        string[]? AssociatedAdvertisers?;
        string[]? AssociatedCampaigns?;
    |}[] BidLists;
    record {|
        string CounterName;
        int ResetIntervalInMinutes;
        boolean? IncrementByAllEntitiesAssociatedWithBidLists?;
    |} Counter;
|};

// Tracking Tag Types
type TrackingTagResponse record {|
    string AdvertiserId;
    string? ContainerTagBody?;
    string? Currency?;
    string? DataEventTypeId?;
    int FirstPartyDataId;
    int HitCount7Day;
    boolean HouseholdEnabled;
    string? IFrameTag?;
    string? ImageTag?;
    string? OfflineDataProviderId?;
    string? Revenue?;
    string? TagRedirectUri?;
    string TrackingTagAvailability;
    string TrackingTagCategory;
    string TrackingTagId;
    string? TrackingTagLocation?;
    string TrackingTagName;
    string TrackingTagType;
    string? UniversalPixelName?;
|};

// Seller Query Types
type SellerQueryRequest record {|
    int PageSize;
    int PageStartIndex;
    string[]? IncludedSellerDomains?;
    string[]? SellerNameFilters?;
    string? SellerStatusFilter?;
    record {|
        string FieldId;
        boolean Ascending;
    |}[]? SortFields?;
|};

type SellerQueryResponse record {|
    record {|
        string? AliasToSellerDomain?;
        boolean IsTargetable;
        string? SellerDomain?;
        string[]? SellerDomainAliases?;
        string? SellerName?;
        string SellerStatus;
    |}[] Result;
    int ResultCount;
    int TotalFilteredCount;
    int TotalUnfilteredCount;
|};

// IP Targeting List Types
type IPTargetingRange record {|
    string MinIP;
    string MaxIP;
|};

type IPTargetingListRequest record {|
    string AdvertiserId;
    string IPTargetingDataName;
    IPTargetingRange[] IPTargetingRanges;
|};

type IPTargetingListResponse record {|
    string AdvertiserId;
    string IPTargetingDataName;
    string IPTargetingListId;
    int IPTargetingRangesCount;
|};

// Report Schedule Types
type ReportScheduleResponse record {|
    int ReportScheduleId;
    string ReportScheduleName;
    string[] AdvertiserFilters;
    string[] CampaignFilters;
    string[] AdGroupFilters;
    string[] PartnerFilters;
    string ReportDateRange;
    string? ReportStartDateInclusive?;
    string? ReportEndDateExclusive?;
    string ReportFrequency;
    string ReportFileFormat;
    string[] EmailAddresses;
    string TimeZone;
    boolean IsCompleted;
    string CreationDateUtc;
|};

// Advertiser Overview Types
type AdvertiserOverviewResponse record {|
    string AdvertiserId;
    string AdvertiserName;
    record {|
        string CampaignId;
        string CampaignName;
        string? Description?;
        string StartDateUTC;
        string? EndDateUTC?;
        string Availability;
        record {|
            string AdGroupId;
            string AdGroupName;
            string? Description?;
            boolean IsEnabled;
            string Availability;
            record {|
                string CreativeId;
                string CreativeName;
                string? Description?;
            |}[] Creatives;
        |}[] AdGroups;
    |}[] Campaigns;
    record {|
        string CreativeId;
        string CreativeName;
        string? Description?;
    |}[] Creatives;
|};

// Universal Forecasting Types
type UniversalForecastingRequest record {|
    string AdvertiserId;
    string? AudienceId?;
    float AverageBidCPMInAdvertiserCurrency;
    record {|
        string? StartAge?;
        string? EndAge?;
        string? Gender?;
    |}? Demographic?;
    int[]? ExistingBidLists?;
    record {|
        string AdvertiserId;
        string AudienceName;
        record {|
            string AdvertiserId;
            string DataGroupName;
        |}[] IncludedDataGroups;
    |}[]? ForecastingAudiences?;
    boolean GenerateBudgetPoints;
    int TimeWindow;
    record {|
        record {|
            float BidAdjustment;
            string? AdBugPageQualityCategoryId?;
            string? AdFormatId?;
        |}[] BidLines;
    |}[]? UniversalForecastingBidLists?;
|};

type MetricResult record {|
    string InsightMetricType;
    float RangeStart;
    float RangeEnd;
|};

type ForecastResponse record {|
    MetricResult[] MetricResults;
|};

// Start of the Ballerina service definition
service /v3 on new http:Listener(9090) {

    // POST /v3/advertiser
    resource function post advertiser(@http:Header {name: "TTD-Auth"} string apiKey,
                                      AdvertiserRequest advertiserReq)
                                      returns AdvertiserResponse|http:Unauthorized {
        if apiKey != "valid-api-key" {
            return http:UNAUTHORIZED;
        }

        // Mock response
        AdvertiserResponse advertiserResponse = {
            AdvertiserId: "advertiser_12345"
        };
        return advertiserResponse;
    }

    // GET /v3/advertiser/{advertiserId}
    resource function get advertiser/[string advertiserId](@http:Header {name: "TTD-Auth"} string apiKey)
                                      returns AdvertiserDetailsResponse|http:Unauthorized|http:NotFound {
        if apiKey != "valid-api-key" {
            return http:UNAUTHORIZED;
        }

        // Mock data
        if advertiserId == "advertiser_12345" {
            AdvertiserDetailsResponse advertiserDetails = {
                AdvertiserId: "advertiser_12345",
                AdvertiserName: "Sample Advertiser",
                AttributionClickLookbackWindowInSeconds: 3600,
                AttributionImpressionLookbackWindowInSeconds: 3600,
                ClickDedupWindowInSeconds: 0,
                ConversionDedupWindowInSeconds: 0,
                DefaultRightMediaOfferTypeId: 12345,
                DomainAddress: "https://www.advertiser.com",
                PartnerId: "partner_123"
            };
            return advertiserDetails;
        } else {
            return http:NOT_FOUND;
        }
    }
}
