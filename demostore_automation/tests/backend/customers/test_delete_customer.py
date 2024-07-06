

import pytest
import logging as logger

from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility
from demostore_automation.src.generic_helpers.generic_customer_helpers import GenericCustomerHelpers
from demostore_automation.src.api_helpers.CustomersAPIHelper import CustomersAPIHelper


@pytest.mark.estcb8
def test_delete_a_customer_with_force_flag_true():
    logger.info("Starting 'delete customer' test...")
    # we first need a customer to be deleted
    # so get the customer from db or create a new customer
    # it is best to create a new user so when we delete it we know no one else is using that user
    cust_api_helper = CustomersAPIHelper()
    create_cust_response = cust_api_helper.call_create_customers()
    customer_id = create_cust_response['id']

    # make the call ( the function automatically validates the status code so if we get a response we know the status code is as expected) 
    delete_cust_response = cust_api_helper.call_delete_customer(customer_id, force=True)

    #verify the call is success
    assert delete_cust_response['id'] == customer_id, f"Delete customer api, the id in teh response" \
        f"does not match the id in the request. Response id: {delete_cust_response['id']}, Request id {customer_id}"
    

    # verify the customer is deleted
    # make a 'get customer' api call and verify we get nothing
    # the function will automatically verify the status code
    get_cust_response = cust_api_helper.call_get_customer_by_id(customer_id=customer_id, expected_status_code=404)

    assert get_cust_response['code'] == 'woocommerce_rest_invalid_id', f"After deleting customer, when doing get customer the " \
                                            "response does not have the correct code"
    assert get_cust_response['message'] == 'Invalid resource ID.', f"After deleting customer, when doing get customer the " \
                                        "response does not have the correct 'message'"
    assert get_cust_response['data']['status'] == 404, f"Invalid status code when doing get customer after deleting the customer"
    breakpoint()

@pytest.mark.estcb9
def test_delete_a_customer_with_force_flag_false():
    logger.info("Starting 'delete customer' test...")
    # we first need a customer to be deleted
    # so get the customer from db or create a new customer
    # it is best to create a new user so when we delete it we know no one else is usiging that user
    cust_api_helper = CustomersAPIHelper()
    create_cust_response = cust_api_helper.call_create_customers()
    customer_id = create_cust_response['id']

    # make the call ( the function automatically validates the status code so if we get a response we know the status code is as expected)
    delete_cust_response = cust_api_helper.call_delete_customer(customer_id, force=False, expected_status_code=501)

    assert delete_cust_response['code'] == 'woocommerce_rest_trash_not_supported', \
            f"Unexpected response body when calling 'delete customer'" \
            f"with force=False, Exected: 'woocommerce_rest_trash_not_supported', Actual: {delete_cust_response['code']}"
    
    assert delete_cust_response['message'] == 'Customers do not support trashing.', \
            f"Unexpected response body when calling 'delete customer'" \
            f"with force=False. Expected: 'Customers do not support trashing.', Actual: {delete_cust_response['message']}"
    
    assert delete_cust_response['data']['status'] == 501, \
            f"Unexprected response body when calling 'delete customer'" \
            f"with force=False. Expected code: '501', Actual: {delete_cust_response['data']['status']}"
    
@pytest.mark.estcb10
def test_delete_a_customer_with_out_the_force():
        logger.info("Starting 'delete customer' test...")
        # we first need a customer to be deleted
        # so get the customer from db or create a new customer
        # it is best to create a new user so when we delete it we know no one else is using the user
        cust_api_helper = CustomersAPIHelper()
        create_cust_response = cust_api_helper.call_create_customer()
        customer_id = create_cust_response['id']

        # since the helper function passes the 'force' flag automaticallly we can not use that helper
        # instead w are going to use the api helper and make the call directly

        #create api helper object
        woo_api_helper = WooAPIUtility()

        delete_cust_response = woo_api_helper.delete(f"customers/{customer_id}", expected_status_code=501)

        assert delete_cust_response['code'] == 'woocommerce_rest_trash_not_supported', \
            f"Unexpected response body when calling 'delete customer'" \
            f"with out the 'force' flag. Expected: 'woocommerce_rest_trash_not_supported', Actual: {delete_cust_response['code']}"

        assert delete_cust_response['message'] == 'Customers do not support trashing.', \
            f"Unexpected response body when calling 'delete customer'" \
            f"with out the 'force' flag Expected: 'Customers do not support trashing.', Actual: {delete_cust_response['message']}"
    
        assert delete_cust_response['data']['status'] == 501, \
            f"Unexpected response body when calling 'delete customer'" \
            f"without the 'force' flag. Expected code: '501', Actual: {delete_cust_response['data']['status']}" 
        
    
@pytest.mark.estcb11
def test_delete_a_none_existing_customer():

    logger.info("Starting 'delete customer' test...")

        # to get a customer that does not exist, get the max customer id and make the call for id bigger than that
        # it is possible customers are being created by other methods so not good idea to just increase the max id by 1.
        # to be safe lets increase it by 100 or more. Even 100 can be small for example if load test is running

        # need a function to get the maximum customer id
    cust_helper = GenericCustomersHelpers()
    max_id = cust_helper.get_max_customer_id()
    none_existing_user_id = max_id + 100
 
        # try deleting the customer
        # make the call ( the function automaticaly validates the status code so if we get a response we know the status code is as expected)
    cust_api_helper = CustomersAPIHelper()

    delete_cust_response = cust_api_helper.call_delete_customer(none_existing_user_id, force=True, expected_status_code=400)
        
    assert delete_cust_response['code'] == 'woocommerce_rest_invalid_id', "Bad response body when delete non existing customer call is made."
    assert delete_cust_response['message'] == 'Invalid resource id.', "Bad response body when delete non existing customer call is made."
    assert delete_cust_response['data']['status'] == 400, "Bad response body when delete non existing customer call is made."

