# ttd-mock-server

This document provides an overview of the mock server implemented using Ballerina. The server simulates various endpoints for testing API clients or for integration testing purposes.

## Overview

The mock server exposes several RESTful endpoints under the `/v3` base path. It utilizes Ballerina's HTTP module to handle HTTP requests and responses, including header parameter binding and payload data binding.

## Prerequisites

- **Ballerina Language**: Ensure you have Ballerina installed on your system. You can download it from the [Ballerina Downloads](https://ballerina.io/downloads/) page.

## Running the Mock Server

Open a terminal and navigate to the directory containing `server.bal`. Run the server using the command:

```bash
   bal run server.bal
```

The server will start listening on port 9090.

## Testing the Endpoints

You can test the endpoints using tools like curl, Postman, or any other HTTP client.

1. Example: Creating an Advertiser

Request:

```bash
curl -X POST "http://localhost:9090/v3/advertiser" \
-H "Content-Type: application/json" \
-H "TTD-Auth: valid-api-key" \
-d '{
"AdvertiserName": "Sample Advertiser",
"AttributionClickLookbackWindowInSeconds": 3600,
"AttributionImpressionLookbackWindowInSeconds": 3600,
"ClickDedupWindowInSeconds": 0,
"ConversionDedupWindowInSeconds": 0,
"DefaultRightMediaOfferTypeId": 12345,
"DomainAddress": "https://www.advertiser.com",
"PartnerId": "partner_123"
}'
```

**Explanation:**

**Method**: POST
**URL**: http://localhost:9090/v3/advertiser
**Headers**:
Content-Type: application/json
TTD-Auth: valid-api-key (This header is required for API key validation)
Payload: JSON object containing advertiser details.

**Expected Response:**

```json
{
"AdvertiserId": "advertiser_12345"
}
```

**Explanation:**

The server responds with a JSON object containing the AdvertiserId of the newly created advertiser.
If the TTD-Auth header is missing or invalid, the server will respond with a 401 Unauthorized status.
If the request payload is invalid or missing required fields, the server will respond with a 400 Bad Request status.

## Other Endpoints
The mock server includes several other endpoints, each simulating different operations. Below are brief descriptions and examples for each.

### Get Advertiser Details
Endpoint: GET /v3/advertiser/{advertiserId}

Example Request:

```bash
curl -X GET "http://localhost:9090/v3/advertiser/advertiser_12345" \
-H "TTD-Auth: valid-api-key"
```

**Expected Response:**

```json
{
"AdvertiserId": "advertiser_12345",
"AdvertiserName": "Sample Advertiser",
"AttributionClickLookbackWindowInSeconds": 3600,
"AttributionImpressionLookbackWindowInSeconds": 3600,
"ClickDedupWindowInSeconds": 0,
"ConversionDedupWindowInSeconds": 0,
"DefaultRightMediaOfferTypeId": 12345,
"DomainAddress": "https://www.advertiser.com",
"PartnerId": "partner_123"
}
```

### Create an Ad Group
Endpoint: POST /v3/adgroup

**Example Request:**

```bash
curl -X POST "http://localhost:9090/v3/adgroup" \
-H "Content-Type: application/json" \
-H "TTD-Auth: valid-api-key" \
-d '{
"AdGroupName": "Sample Ad Group",
"CampaignId": "campaign_12345",
"BudgetSettings": {
"BudgetInAdvertiserCurrency": 5000.00
},
"PacingMode": "Even"
}'
```

**Expected Response:**

```json
{
"AdGroupId": "adgroup_123",
"AdGroupName": "Sample Ad Group",
"CampaignId": "campaign_12345"
}
```

### Create a Campaign
Endpoint: POST /v3/campaign

Example Request:

```bash
curl -X POST "http://localhost:9090/v3/campaign" \
-H "Content-Type: application/json" \
-H "TTD-Auth: valid-api-key" \
-d '{
"AdvertiserId": "advertiser_12345",
"CampaignName": "My New Campaign",
"Budget": {
"Amount": 10000.00,
"CurrencyCode": "USD"
},
"StartDate": "2024-01-01T00:00:00Z",
"EndDate": "2024-12-31T23:59:59Z"
}'
```

**Expected Response:**

```json
{
"CampaignId": "campaign_12345",
"AdvertiserId": "advertiser_12345",
"CampaignName": "My New Campaign",
"Budget": {
"Amount": 10000.0,
"CurrencyCode": "USD"
},
"StartDate": "2024-01-01T00:00:00Z",
"EndDate": "2024-12-31T23:59:59Z"
}
```

## Error Handling
The mock server handles errors using standard HTTP status codes:

400 Bad Request: Returned when the request payload is invalid or missing required fields.
401 Unauthorized: Returned when the TTD-Auth header is missing or contains an invalid API key.
404 Not Found: Returned when the requested resource does not exist.
