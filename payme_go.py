import requests
from typing import Dict


class PayMeGo:
    def __init__(self, merchant_id: str, key: str):
        """
        :param merchant_id: PayMe Merchant ID
        :param key:  PayMe Production Key
        """
        self.token = f'{merchant_id}:{key}'
        self.url = 'https://checkout.paycom.uz/api'

    def get_header(self) -> Dict[str, str]:
        return {'X-Auth': self.token}

    def pay(self, amount: int, kkm_id: str, device_id: str, transaction_id: str, qr_code: str):
        """
        :param amount: int 1000 UZS
        :param kkm_id: 'test-kkm'
        :param device_id:'device-0001'
        :param transaction_id: 1
        :param qr_code: 00816261728386152
        :return: dict
        >>> self.pay(amount=1000, kkm_id='test-kkm', device_id='device-0001', transaction_id='1', qr_code='test_qrcode')
        """
        receipts_create = self._receipts_create(amount, kkm_id, device_id, transaction_id)
        if 'error' in receipts_create:
            return receipts_create
        _id = receipts_create['result']['receipt']['_id']
        return self._receipts_pay(_id, qr_code)

    def _receipts_create(self, amount: int, kkm_id: str, device_id: str, transaction_id: str):
        """

        :param amount: INT 1000
        :param kkm_id: STR
        :param device_id: STR
        :param transaction_id: STR
        :return: dict
        """
        data = {
            "id": 123,
            "method": "receipts.create",
            "params": {
                "amount": amount * 100,
                "account": {
                    "kkm_id": kkm_id,
                    "device_id": device_id,
                    "document": transaction_id
                }
            }
        }
        response = requests.post(self.url, json=data, headers=self.get_header())
        response = response.json()
        return response

    def _receipts_pay(self, _id: str, qr_code: str) -> Dict[str, str]:
        """

        :param _id: STR
        :param qr_code: STR
        :return: dict
        """
        data = {
            "id": 123,
            "method": "receipts.pay",
            "params": {
                "id": _id,
                "token": qr_code,
            }
        }
        response = requests.post(self.url, json=data, headers=self.get_header())
        response = response.json()
        return response
