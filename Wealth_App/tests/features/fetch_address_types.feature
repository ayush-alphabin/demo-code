Feature: fetchAddressTypes API

    @all @C12387 @staticAPI @MasterData @sanity @regression @fetchAddressTypes
    Scenario: Valid request for fetchAddressTypes
        Given the API endpoint is configured with parameters
        When I send a GET request to the API
        Then the response status code should be 200
        And the response should contain valid address types data

    @all @C12395 @staticAPI @MasterData @sanity @regression @fetchAddressTypes
    Scenario: Assert id of state from response body
        Given a successful response from fetchAddressTypes
        Then the response should contain a valid AddressType id

    @all @C12396 @staticAPI @MasterData @smoke @regression @fetchAddressTypes
    Scenario: Assert name of state from response body
        Given a successful response from fetchAddressTypes
        Then the response should contain the AddressType name "Residential"

    @all @C12388 @staticAPI @MasterData @smoke @regression @fetchAddressTypes
    Scenario: Send request with invalid param limit
        Given the API endpoint is configured with invalid param limit
        When I send a GET request to the API
        Then the response status code should be 491

    @all @C12389 @staticAPI @MasterData @regression @fetchAddressTypes
    Scenario: Send request with invalid param offset
        Given the API endpoint is configured with invalid param offset
        When I send a GET request to the API
        Then the response status code should be 491

    @all @C12390 @staticAPI @MasterData @regression @fetchAddressTypes
    Scenario: Send request with only param limit
        Given the API endpoint is configured with only param limit
        When I send a GET request to the API
        Then the response status code should be 200

    @all @C12391 @staticAPI @MasterData @regression @fetchAddressTypes
    Scenario: Send request with only param offset
        Given the API endpoint is configured with only param offset
        When I send a GET request to the API
        Then the response status code should be 200

    @all @C12392 @staticAPI @MasterData @regression @fetchAddressTypes
    Scenario: Send request with empty params
        Given the API endpoint is configured with empty params
        When I send a GET request to the API
        Then the response status code should be 200

    @all @C12393 @staticAPI @MasterData @regression @fetchAddressTypes
    Scenario: Send request using POST method
        Given the API endpoint is configured with valid parameters
        When I send a POST request to the API
        Then the response status code should be 491
