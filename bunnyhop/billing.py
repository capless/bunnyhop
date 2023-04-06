import requests

from bunnyhop.base import Record, APIKeyRecord


class BillingRecord(APIKeyRecord):

    def __init__(self, api_key, data):
        """
        BillingRecord constructor.
        Args:
            api_key (str): BunnyCDN's API key.
            data (dict): The billing record.
        Attributes:
            id (str): The record id.
            amount (float): The amount of the record.
            document_download_url (str): The document download url.
            amount (float): The amount of the record.
            invoice_available (bool): Whether an invoice is available.
            payer (str): The payer.
            payment_id (str): The payment id.
            timestamp (str): The timestamp.
            type (str): The type.
        """
        super().__init__(data)
        self.api_key = api_key

    def download(self, output_file):
        """
        Download the billing record.
        Args:
            output_file (str): The output file to write the record to.
        Returns:
            None
        """
        response = requests.get(self.document_download_url, headers={'AccessKey': self.api_key})
        response.raise_for_status()
        with open(output_file, 'wb') as f:
            f.write(response.content)


class SavedPaymentMethod(Record):
    pass


class BillingStatus(Record):

    def __init__(self, api_key, data):
        """
        BillingStatus constructor.
        Args:
            data (dict): The billing summary.
        Attributes:
            balance (float): The balance.
            this_month_charges (float): This month charges.
            billing_records (list): The billing records.
            monthly_charges_storage (float): The monthly charges storage.
            monthly_charges_eu_traffic (float): The monthly charges eu traffic.
            monthly_charges_us_traffic (float): The monthly charges us traffic.
            monthly_charges_asia_traffic (float): The monthly charges asia traffic.
            monthly_charges_af_traffic (float): The monthly charges af traffic.
            monthly_charges_sa_traffic (float): The monthly charges sa traffic.
            billing_history_chart (str): The billing history chart.
            monthly_bandwidth_used (int): The monthly bandwidth used.
            monthly_charges_optimizer (float): The monthly charges optimizer.
            monthly_charges_extra_pull_zones (float): The monthly charges extra pull zones.
            billing_enabled (bool): Whether billing is enabled.
            minimum_monthly_commit (float): The minimum monthly commit.
            automatic_payment_image_url (str): The automatic payment image url.
            automatic_payment_card_type (str): The automatic payment card type.
            automatic_payment_identifier (str): The automatic payment identifier.
            automatic_payment_amount (float): The automatic payment amount.
            automatic_recharge_treshold (float): The automatic recharge threshold.
            automatic_recharge_enabled (bool): Whether automatic recharge is enabled.
            automatic_payment_failure_count (int): The automatic payment failure count.
            saved_payment_methods (list): The saved payment methods.
            vat_rate (float): The vat rate.
            eu_us_discount (int): The eu us discount.
            south_america_discount (int): The south america discount.
            africa_discount (int): The africa discount.
            asia_oceania_discount (int): The asia oceania discount.
            last_recharge_balance (float): The last recharge balance.
        """
        super().__init__(data)
        self.billing_records = [BillingRecord(api_key, record) for record in self.billing_records]
        self.saved_payment_methods = [SavedPaymentMethod(method) for method in self.saved_payment_methods]


class Billing(APIKeyRecord):
    def __init__(self, api_key):
        """
        Initialize the Billing API.
        Args:
            api_key (str): BunnyCDN's API key.
        """
        self.api_key = api_key

    def get_billing_details(self):
        """
        Get billing details from your account.
        Args:
            None
        Returns:
            The response object from the API request.
        """
        path = '/billing'
        headers = {'AccessKey': self.api_key}
        data = self._make_request('GET', path, headers=headers)
        return BillingStatus(self.api_key, data)

    def confgiure_auto_recharge(self, enabled, payment_method_token, payment_amount, recharge_threshold):
        """
        Set autorecharge settings for your account.
        Args:
            enabled (bool): True if autorecharge is enabled, false otherwise.
            payment_method_token (str): The payment method token.
            payment_amount (float): The payment amount.
            recharge_threshold (float): The recharge threshold.
        Returns:
            The response object from the API request.

        """
        path = '/billing/payment/autorecharge'
        headers = {'AccessKey': self.api_key}
        params = {
            'AutoRechargeEnabled': enabled,
            'PaymentMethodToken': payment_method_token,
            'PaymentAmount': payment_amount,
            'RechargeThreshold': recharge_threshold
        }
        return self._make_request('POST', path, headers=headers, json=params)

    def checkout(self, recharge_amount, payment_amount, payment_request_id=None, nonce=None):
        """
        Checkout with a payment method.
        Args:
            recharge_amount (float): The recharge amount.
            payment_amount (float): The payment amount.
            payment_request_id (str, optional): The payment request id.
            nonce (str, optional): The nonce.
        Returns:
            The response object from the API request.
        """
        path = '/billing/payment/checkout'
        headers = {'AccessKey': self.api_key}
        params = {'RechargeAmount': recharge_amount, 'PaymentAmount': payment_amount}
        if payment_request_id is not None:
            params['PaymentRequestId'] = payment_request_id
        if nonce is not None:
            params['Nonce'] = nonce
        return self._make_request('POST', path, headers=headers, json=params)

    def prepare_payment_authorization(self):
        """
        Prepare payment authorization.
        Args:
            None
        Returns:
            The response object from the API request.
        """
        path = '/billing/payment/prepare-authorization'
        headers = {'AccessKey': self.api_key}
        return self._make_request('GET', path, headers=headers)

    def get_affiliate_data(self):
        """
        Get affiliate data.
        Args:
            None
        Returns:
            The response object from the API request.
        """
        path = '/billing/affiliate'
        headers = {'AccessKey': self.api_key}
        return self._make_request('GET', path, headers=headers)

    def claim_affiliate_credits(self):
        """
        Claim affiliate credits.
        Args:
            None
        Returns:
            The response object from the API request.
        """
        path = '/billing/affiliate/claim'
        headers = {'AccessKey': self.api_key}
        return self._make_request('POST', path, headers=headers)

    def get_coinify_exchange_rate(self):
        """
        Get the current exchange rate for Coinify.
        Args:
            None
        Returns:
            The response object from the API request.
        """
        path = '/billing/coinify/exchangerate'
        headers = {'AccessKey': self.api_key}
        return self._make_request('GET', path, headers=headers).get('ExchangeRate')

    def create_coinify_payment(self, amount):
        """
        Create a Coinify payment.
        Args:
            amount (float): The amount to pay.
        Returns:
            The response object from the API request.
        """
        path = '/billing/coinify/create'
        headers = {'AccessKey': self.api_key}
        params = {'amount': amount}
        return self._make_request('GET', path, headers=headers, params=params)

    def get_billing_summary(self):
        """
        Get billing summary.
        Args:
            None
        Returns:
            The response object from the API request.
        """
        path = '/billing/summary'
        headers = {'AccessKey': self.api_key}
        return self._make_request('GET', path, headers=headers)

    def apply_coupon_code(self, coupon_code):
        """
        Apply a coupon code to your account.
        Args:
            coupon_code (str): The coupon code to apply.
        Returns:
            The response object from the API request.
        """
        path = '/billing/applycode'
        headers = {'AccessKey': self.api_key}
        params = {'CouponCode': coupon_code}
        return self._make_request('GET', path, headers=headers, params=params)
