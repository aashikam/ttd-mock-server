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

// Authentication Types
type AuthenticationRequest record {|
    string Login;
    string Password;
    int? TokenExpirationInMinutes?;
|};

type AuthenticationResponse record {|
    string Token;
|};

// Start of the Ballerina service definition
service /v3 on new http:Listener(9090) {

    // POST /v3/advertiser
    resource function post advertiser(@http:Header {name: "TTD-Auth"} string apiKey,
                                      AdvertiserRequest advertiserReq)
                                      returns AdvertiserResponse|http:Unauthorized {
        if apiKey != "mockToken1234567890" {
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
        if apiKey != "mockToken1234567890" {
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

    // POST /v3/adgroup
    resource function post adgroup(@http:Header {name: "TTD-Auth"} string apiKey,
                                   AdGroupRequest adGroupReq)
                                   returns AdGroupResponse|http:Unauthorized|http:BadRequest {
        if apiKey != "mockToken1234567890" {
            return http:UNAUTHORIZED;
        }

        // Mock response
        AdGroupResponse adGroupResponse = {
            AdGroupId: "adgroup_123",
            AdGroupName: "Sample Ad Group",
            CampaignId: "campaign_12345"
        };
        return adGroupResponse;
    }

    // POST /v3/creative
    resource function post creative(@http:Header {name: "TTD-Auth"} string apiKey,
                                    CreativeRequest creativeReq)
                                    returns CreativeRequest|http:Unauthorized|http:BadRequest {
        if apiKey != "mockToken1234567890" {
            return http:UNAUTHORIZED;
        }

        // Mock response - Echo back the request for simplicity
        return creativeReq;
    }

    // POST /v3/bidlist
    resource function post bidlist(@http:Header {name: "TTD-Auth"} string apiKey,
                                   BidListRequest bidListReq)
                                   returns BidListRequest|http:Unauthorized|http:BadRequest {
        if apiKey != "mockToken1234567890" {
            return http:UNAUTHORIZED;
        }

        // Mock response - Echo back the request for simplicity
        return bidListReq;
    }

    // POST /v3/campaign
    resource function post campaign(@http:Header {name: "TTD-Auth"} string apiKey,
                                    CampaignRequest campaignReq)
                                    returns CampaignResponse|http:Unauthorized|http:BadRequest {
        if apiKey != "mockToken1234567890" {
            return http:UNAUTHORIZED;
        }

        // Mock response
        CampaignResponse campaignResponse = {
            CampaignId: "campaign_12345",
            AdvertiserId: "advertiser_12345",
            CampaignName: "My New Campaign",
            Budget: {
                Amount: 10000.00,
                CurrencyCode: "USD"
            },
            StartDate: "2024-01-01T00:00:00Z",
            EndDate: "2024-12-31T23:59:59Z"
        };
        return campaignResponse;
    }

    // GET /v3/campaign/{campaignId}/metrics
    resource function get campaign/[string campaignId]/metrics(@http:Header {name: "TTD-Auth"} string apiKey)
                                      returns CampaignMetricsResponse|http:Unauthorized|http:NotFound {
        if apiKey != "mockToken1234567890" {
            return http:UNAUTHORIZED;
        }

        // Mock data
        if campaignId == "campaign_12345" {
            CampaignMetricsResponse metricsResponse = {
                CampaignFlightId: 1234567890,
                CampaignId: "campaign_12345",
                GoalInfo: {
                    CPAInAdvertiserCurrency: {
                        Amount: 4.5,
                        CurrencyCode: "USD",
                        Target: 5.0
                    },
                    CPCInAdvertiserCurrency: {
                        Amount: 1.2,
                        CurrencyCode: "USD",
                        Target: 1.0
                    },
                    CTRInPercent: {
                        Amount: 2.5,
                        Target: 3.0
                    },
                    Impressions: 100000,
                    LastCalculatedAt: "2024-09-22T12:34:56Z"
                },
                CurrentSpendInAdvertiserCurrency: 5000.00,
                FlightBudgetInAdvertiserCurrency: 10000.00,
                ProjectedSpendInAdvertiserCurrency: 8000.00
            };
            return metricsResponse;
        } else {
            return http:NOT_FOUND;
        }
    }

    // POST /v3/dmp/firstparty/advertiser
    resource function post dmp/firstparty/advertiser(@http:Header {name: "TTD-Auth"} string apiKey,
                                                     FirstPartyAdvertiserRequest request)
                                                     returns FirstPartyAdvertiserResponse|http:Unauthorized|http:BadRequest {
        if apiKey != "mockToken1234567890" {
            return http:UNAUTHORIZED;
        }

        // Mock response
        FirstPartyAdvertiserResponse response = {
            Result: [],
            ResultCount: 0,
            TotalFilteredCount: 0,
            TotalUnfilteredCount: 0
        };
        return response;
    }

    // POST /v3/frequency/config
    resource function post frequency/config(@http:Header {name: "TTD-Auth"} string apiKey,
                                            FrequencyConfigRequest freqConfigReq)
                                            returns http:Ok|http:Unauthorized|http:BadRequest {
        if apiKey != "mockToken1234567890" {
            return http:UNAUTHORIZED;
        }

        // Mock response - Just acknowledge the creation
        return http:OK;
    }

    // GET /v3/trackingtag/{trackingTagId}
    resource function get trackingtag/[string trackingTagId](@http:Header {name: "TTD-Auth"} string apiKey)
                                      returns TrackingTagResponse|http:Unauthorized|http:NotFound {
        if apiKey != "mockToken1234567890" {
            return http:UNAUTHORIZED;
        }

        // Mock data
        if trackingTagId == "tracking_tag_123" {
            TrackingTagResponse trackingTag = {
                AdvertiserId: "advertiser_12345",
                ContainerTagBody: (),
                Currency: "USD",
                DataEventTypeId: (),
                FirstPartyDataId: 123456,
                HitCount7Day: 100,
                HouseholdEnabled: true,
                IFrameTag: (),
                ImageTag: (),
                OfflineDataProviderId: (),
                Revenue: (),
                TagRedirectUri: (),
                TrackingTagAvailability: "Available",
                TrackingTagCategory: "StaticTag",
                TrackingTagId: "tracking_tag_123",
                TrackingTagLocation: (),
                TrackingTagName: "Sample Tracking Tag",
                TrackingTagType: "Conversion",
                UniversalPixelName: ()
            };
            return trackingTag;
        } else {
            return http:NOT_FOUND;
        }
    }

    // POST /v3/seller/query
    resource function post seller/query(@http:Header {name: "TTD-Auth"} string apiKey,
                                        SellerQueryRequest sellerQueryReq)
                                        returns SellerQueryResponse|http:Unauthorized|http:BadRequest {
        if apiKey != "mockToken1234567890" {
            return http:UNAUTHORIZED;
        }

        // Mock response
        SellerQueryResponse response = {
            Result: [],
            ResultCount: 0,
            TotalFilteredCount: 0,
            TotalUnfilteredCount: 0
        };
        return response;
    }

    // POST /v3/iptargetinglist
    resource function post iptargetinglist(@http:Header {name: "TTD-Auth"} string apiKey,
                                           IPTargetingListRequest ipTargetingListReq)
                                           returns IPTargetingListResponse|http:Unauthorized|http:BadRequest {
        if apiKey != "mockToken1234567890" {
            return http:UNAUTHORIZED;
        }

        // Mock response
        IPTargetingListResponse response = {
            AdvertiserId: "advertiser_12345",
            IPTargetingDataName: "My New IP Targeting List",
            IPTargetingListId: "ip_targeting_list_123",
            IPTargetingRangesCount: 5
        };
        return response;
    }

    // GET /v3/myreports/reportschedule/{scheduleId}
    resource function get myreports/reportschedule/[int scheduleId](@http:Header {name: "TTD-Auth"} string apiKey)
                                      returns ReportScheduleResponse|http:Unauthorized|http:BadRequest {
        if apiKey != "mockToken1234567890" {
            return http:UNAUTHORIZED;
        }

        // Mock data
        ReportScheduleResponse reportSchedule = {
            ReportScheduleId: scheduleId,
            ReportScheduleName: "My Weekly Performance Report",
            AdvertiserFilters: ["advertiser_12345"],
            CampaignFilters: ["campaign_12345"],
            AdGroupFilters: ["adgroup_123"],
            PartnerFilters: ["partner_123"],
            ReportDateRange: "Last7Days",
            ReportStartDateInclusive: (),
            ReportEndDateExclusive: (),
            ReportFrequency: "Weekly",
            ReportFileFormat: "CSV",
            EmailAddresses: ["user@example.com"],
            TimeZone: "UTC",
            IsCompleted: false,
            CreationDateUtc: "2024-09-22T12:00:00Z"
        };
        return reportSchedule;
    }

    // GET /v3/overview/advertiser/{advertiserId}
    resource function get overview/advertiser/[string advertiserId](@http:Header {name: "TTD-Auth"} string apiKey)
                                      returns AdvertiserOverviewResponse|http:Unauthorized|http:BadRequest {
        if apiKey != "mockToken1234567890" {
            return http:UNAUTHORIZED;
        }

        // Mock data
        if advertiserId == "advertiser_12345" {
            AdvertiserOverviewResponse overview = {
                AdvertiserId: "advertiser_12345",
                AdvertiserName: "Sample Advertiser",
                Campaigns: [],
                Creatives: []
            };
            return overview;
        } else {
            return http:BAD_REQUEST;
        }
    }

    // POST /v3/universalforecasting/generate
    resource function post universalforecasting/generate(@http:Header {name: "TTD-Auth"} string apiKey,
                                                         UniversalForecastingRequest forecastReq)
                                                         returns ForecastResponse|http:Unauthorized|http:BadRequest {
        if apiKey != "mockToken1234567890" {
            return http:UNAUTHORIZED;
        }

        // Mock response
        ForecastResponse forecastResponse = {
            MetricResults: [
                {
                    InsightMetricType: "Impressions",
                    RangeStart: 1000000,
                    RangeEnd: 2000000
                },
                {
                    InsightMetricType: "Spend",
                    RangeStart: 5000.00,
                    RangeEnd: 10000.00
                }
            ]
        };
        return forecastResponse;
    }

    // POST /v3/authentication
    resource function post authentication(AuthenticationRequest authRequest)
            returns AuthenticationResponse|http:Unauthorized|http:BadRequest {

        // Mock authentication logic
        if authRequest.Login == "validUser" && authRequest.Password == "validPassword" {
            int tokenExpiry = authRequest.TokenExpirationInMinutes ?: 1440;

            // Generate a mock token (in a real scenario, generate a JWT or similar token)
            AuthenticationResponse authResponse = {
                Token: "mockToken1234567890"
            };
            return authResponse;
        } else {
            return http:UNAUTHORIZED;
        }
    }

    // Handle unmatched paths
    resource function default http:Any http:Resource() returns http:NotFound {
        return http:NOT_FOUND;
    }
}
