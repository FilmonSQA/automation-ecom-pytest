

import pytest
import logging as logger
from demostore_automation.src.utilities.genericUtilities import generate_random_string
from demostore_automation.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from demostore_automation.src.dao.products_dao import ProductsDAO


@pytest.mark.estcb6
def test_create_1_simple_product():
    logger.info("ABC")

    #create a payload with random data
    payload = dict()

    # payload = {}
    payload['name'] = generate_random_string(length=30)
    payload['regular_price'] = '10.99'
    payload['type'] = 'simple'
    
    #make api call with the payload
    Product_api_helper = ProductsAPIHelper()
    product_rs = Product_api_helper.call_create_product(payload)

    #verify the response
    #verify the response is not empty
    assert product_rs, f"Create product api response is empty. Payload: {payload}"
    assert product_rs['name'] == payload['name'], f"Create product api call response has" \
        f"unexprected name. Expected: {payload['name']}, Actual: {product_rs['name']}"
    
    assert product_rs['price'] == ['regular_price'], f"The price in the request and response do not match" \
    f"for creat product api with payload={payload}"

    #verify the product is created in the database
    #  look for the porduct by id
    product_id = product_rs["id"]
    products_dao = ProductsDAO()
    db_product = products_dao.get_product_by_id(product_id)

    assert db_product, f"Unable to find the product in database. Create product payload={payload}"
    db_title = db_product[0]['post_title']
    assert db_title ==payload['name'], f"Create product the 'post_title' field in DB is not same as the 'name' field in payload."



    