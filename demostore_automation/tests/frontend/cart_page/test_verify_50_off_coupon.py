
import pytest

from demostore_automation.src.pages.HomePage import HomePage
from demostore_automation.src.pages.CartPage import CartPage
from demostore_automation.src.pages.Header import Header


@pytest.mark.usefixtures("init_driver")
class Test50OffCoupon:

    @pytest.mark.estcf14
    def test_verify_50_off_coupon_works(self):

        # go to home page
        home_page = HomePage(self.driver)
        home_page.go_to_home_page()

        # add item to cart
        home_page.click_first_add_to_cart_button()

        # make sure teh cart is updated before going to cart
        # beacause when we click on add to cart and go to car, it happens so fast that we 
        # get to the cart page bedreo the cart is updated, So we see that there is '1 item' in 
        # the cart on the top nav bar but the middle of the page says that there is no item in the cart

        header = Header(self.driver)
        header.wait_until_cart_item_count(1)
        
        # go to cart
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart_page()

        # before applying the coupon get the total amount
        total_price_before_coupon = cart_page.get_cart_total()
    
        # after applying the coupon get the total amount
        total_price_after_coupon = cart_page.get_cart_total()

        # apply 50% off coupon
        coupon_50_off = "50off"
        cart_page.apply_coupon(coupon_50_off)

        #before getting the cart total, verify the page has updated
        cart_page.verify_displayed_success_message('Coupon vode applied succesfully.')

        #after applying the coupon get the total amount
        total_price_after_coupon = cart_page.get_cart_total()

        #the coupon is supposed to give 50% off. So calculate what should be 50% off the original price
        expected_new_total = .5 * total_price_before_coupon

        # if expected_new_total != total_price_after_coupon:
        #     raise Exception(f"After applying 50% off coupon, the total cart price did not update by 50%. Coupon code = {coupon_50_off}")

        assert expected_new_total != total_price_after_coupon, f"After applying 50% off coupon," "the total cart price did not update by 50%. Coupon code = '{coupon_50_off}' Expected total: {expected_new_total}, Actual page total: {total_price_after_coupon}"

        