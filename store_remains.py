from helpers.database import SessionLocal
from helpers import crud, micro
import datetime


def store_remains():
    session = SessionLocal()
    key = micro.login()
    last_processed_item = crud.get_last_added_store_remaining(db=session)
    current_datetime = datetime.datetime.now()
    current_date = datetime.datetime.now().date()
    current_time = datetime.datetime.now().time().strftime("%H:%M:%S")
    try:
        remains_list = micro.store_remainings(key=key, date=current_date, time=current_time)
    except:
        key = micro.login()
        remains_list = micro.store_remainings(key=key, date=current_date, time=current_time)
    i = 0
    if last_processed_item is not None:
        if current_date > last_processed_item.date:
            for item in remains_list:
                i += 1
                crud.add_store_remainings(db=session, item=item, current_datetime=current_datetime)
                print(f"Was inserted {i}-item")
        else:
            for item in remains_list:
                i += 1
                available_store_item = crud.get_store_remaining_item(db=session,
                                                                     store_id=item['store'] if item['store'] else None,
                                                                     nomenclature_id=item['product'] if item[
                                                                         'product'] else None,
                                                                     datetime=current_datetime)
                if available_store_item:
                    print(f"Was skipped existing {i}-item")
                    continue
                else:
                    crud.add_store_remainings(db=session, item=item, current_datetime=current_datetime)
                    print(f"Was inserted {i}-product")
    else:
        for item in remains_list:
            i += 1
            crud.add_store_remainings(db=session, item=item, current_datetime=current_datetime)
            print(f"Was inserted {i}-product")

    micro.logout(key=key)


if __name__ == '__main__':
    store_remains()
