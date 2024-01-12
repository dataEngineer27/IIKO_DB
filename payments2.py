from helpers.database import SessionLocal
from helpers import crud, micro
from datetime import datetime, timedelta


def payments():
    session = SessionLocal()
    key = micro.login()
    # shifts = crud.get_all_shifts(db=session)
    # last_processed_payment = crud.get_last_added_payment(db=session)
    start_date = datetime(2023, 12, 31)
    end_date = datetime(2024, 1, 11)
    current_date = start_date

    while current_date <= end_date:
        i = 0
        current_date_str = current_date.strftime("%Y-%m-%d")
        try:
            shift_payments = micro.shift_payments(key=key, current_date=current_date_str)
        except:
            key = micro.login()
            shift_payments = micro.shift_payments(key=key, current_date=current_date_str)

        # if last_processed_payment is not None:
        #     if shift.id == last_processed_payment.shift_id:
        #         for payment in shift_payments['data']:
        #             payment_id = payment['PaymentTransaction.Id'] if payment['PaymentTransaction.Id'] else None
        #             nomenclature_id = payment['DishId'] if payment['DishId'] else None
        #             available_payment_item = crud.get_payment_item(db=session,
        #                                                            shift_id=shift.id,
        #                                                            payment_id=payment_id,
        #                                                            nomenclature_id=nomenclature_id)
        #             if available_payment_item:
        #                 continue
        #             else:
        #                 crud.add_shift_payments(db=session, payment=payment)
        #     else:
        #         for payment in shift_payments['data']:
        #             crud.add_shift_payments(db=session, payment=payment)
        # else:
        for payment in shift_payments['data']:
            i += 1
            crud.add_shift_payments(db=session, payment=payment)

        print(f"Added {i} payments in", current_date_str)
        current_date += timedelta(days=1)

    micro.logout(key=key)


if __name__ == '__main__':
    payments()
