import json
import pytest
from pytest_bdd import scenarios, given, when, then
from apiservice.config.apis_utils import apis_utils, RequestTypes
from Wealth_App.configs.apis_endpoint import Apis_End_point

# Load the feature file
scenarios('../features/fetch_address_types.feature')

# Initialize the API endpoint object
apis_endpoint = Apis_End_point()

@pytest.fixture
def context():
    return {}

@given('the API endpoint is configured with parameters')
def configure_api_endpoint(context):
    context['url'] = apis_endpoint.FETCH_ADDRESS_TYPES % (1, 1)

@given('the API endpoint is configured with valid parameters')
def configure_api_endpoint_valid_params(context):
    context['url'] = apis_endpoint.FETCH_ADDRESS_TYPES % (1, 1)

@given('a successful response from fetchAddressTypes')
def successful_response(context):
    context['url'] = apis_endpoint.FETCH_ADDRESS_TYPES % (1, 1)
    context['_fetchAddressTypes_response'] = apis_utils.call_api(
        context['url'], RequestTypes.GET)
    context['json_data'] = json.loads(context['_fetchAddressTypes_response'].text)
    apis_utils.verify_status_codes(context['_fetchAddressTypes_response'], 200)

@given('the API endpoint is configured with invalid param limit')
def configure_invalid_param_limit(context):
    context['url'] = apis_endpoint.FETCH_ADDRESS_TYPES % ("test", 1)

@given('the API endpoint is configured with invalid param offset')
def configure_invalid_param_offset(context):
    context['url'] = apis_endpoint.FETCH_ADDRESS_TYPES % (1, "test")

@given('the API endpoint is configured with only param limit')
def configure_only_param_limit(context):
    context['url'] = (Apis_End_point.default_endpoint +
                      "MasterData/AddressType/fetchAddressTypes?limit=%s") % (1)

@given('the API endpoint is configured with only param offset')
def configure_only_param_offset(context):
    context['url'] = (Apis_End_point.default_endpoint +
                      "MasterData/AddressType/fetchAddressTypes?offset=%s") % (1)

@given('the API endpoint is configured with empty params')
def configure_empty_params(context):
    context['url'] = Apis_End_point.default_endpoint + \
        "MasterData/AddressType/fetchAddressTypes"

@when('I send a GET request to the API')
def send_get_request(context,logger):
    logger.debug("URL -- {}".format(context['url']))
    context['_fetchAddressTypes_response'] = apis_utils.call_api(
        context['url'], RequestTypes.GET)
    context['json_data'] = json.loads(context['_fetchAddressTypes_response'].text)

@when('I send a POST request to the API')
def send_post_request(context,logger):
    logger.debug("URL -- {}".format(context['url']))
    context['_fetchAddressTypes_response'] = apis_utils.call_api(
        context['url'], RequestTypes.POST, {})
    context['json_data'] = json.loads(context['_fetchAddressTypes_response'].text)

@then('the response status code should be 200')
def verify_status_code_200(context):
    try:
        apis_utils.verify_status_codes(context['_fetchAddressTypes_response'], 200)
    except Exception as e:
        raise Exception("Exception:", e)

@then('the response status code should be 491')
def verify_status_code_491(context):
    try:
        apis_utils.verify_status_codes(context['_fetchAddressTypes_response'], 491)
    except Exception as e:
        raise Exception("Exception:", e)

@then('the response should contain valid address types data')
def verify_response_data(context,logger):
    logger.info(context['_fetchAddressTypes_response'].json())

@then('the response should contain a valid AddressType id')
def verify_address_type_id(context,logger):
    id = context['json_data'][0]["id"]
    try:
        assert type(id) == int
        logger.info(context['_fetchAddressTypes_response'].json())
    except Exception as e:
        raise Exception("Exception:", e)

@then('the response should contain the AddressType name "Residential"')
def verify_address_type_name(context,logger):
    name = context['json_data'][0]["name"]
    try:
        assert name == "Residential"
        assert type(name) == str
        logger.info(context['_fetchAddressTypes_response'].json())
    except Exception as e:
        raise Exception("Exception:", e)