# PaymeGo

```python
from payme_go import PayMeGo

pay_me = PayMeGo(merchant_id='<<merchant_id>>', key='<<key>>')
transaction = pay_me.pay(
    amount=1000,
    kkm_id='test-kkm_id',
    device_id='test-device-0001',
    transaction_id='order-id_1',
    qr_code='08271612939'
)
print(transaction)
```
