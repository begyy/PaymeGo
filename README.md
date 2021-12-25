# PaymeGo
![image](https://user-images.githubusercontent.com/44405438/147382389-9244b35f-3417-4774-8331-b36933a55bef.png)

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
