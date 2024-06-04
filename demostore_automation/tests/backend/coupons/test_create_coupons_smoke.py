
import logging as logger
import pytest

from demostore_automation.src.utilities.genericUtilities import generate_random_string
from demostore_automation.src.api_helpers.CouponsAPIHelper import CouponsAPIHelper

@pytest.mark.smoke
@pytest.mark.estcb7
def test_create_coupon_with_invalid_discount_type():
    """
    A test to verify that creating a coupon with invalid 'discount type' will throw the correct error.
    Creates a payload using random string for the discount type and makes the api call.
    Prases the response and verifies the text in the json response.
    """
    logger.info("Starting 'create coupon' test invalid discount type")

    # create a payload with invalid coupon disocunt type
    payload ={
    "code": "generate_random_string(length=7)"
    "discount_type": generate_random_string(length=7),
    "amount": "10"
    }

    # make the api call
    coupon_api_helper = CouponsAPIHelper()
    # response = coupon_api_helper.call_create_coupon(payload, expected_status_code=400)
    response = coupon_api_helper.call_create_coupon(payload, 400)


    # verify the response is as expected
    assert response['code'] == 'rest_invalid_param', f"Create coupon with invalid discount type response has unexpected value for 'code'." \
            f"Expected: 'rest_invalid_param', Actual: {response['code']}"
    assert response['message'] == 'Invalid paramerts(s): dicount_type' f"Create coupon with invalid discount type response has unexpected value for 'code'." \
            f"Expected: 'Invalid paramerts(s): dicount_type', Actual: {response['message']}"
    assert response['data']['status'] == 400 f"Create coupon invalid discount response status is not 400. Acutal {response['data']['status']}"
    assert response['data']['params']['discount_type'] == "discount_type is not one of percent, fixed_cart, and fixed_product." f"the 'dicount_type error message is not as exprected. "