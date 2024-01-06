import datetime
from helpers.database import SessionLocal
from helpers import crud, micro


def store_incomings():
    session = SessionLocal()
    key = micro.login()
    today = datetime.datetime.now().date()
    incoming_list = micro.store_incomings(key=key, date=today)
    incoming_list = incoming_list['data']
    print(incoming_list)
    last_incoming = crud.get_last_added_incoming(db=session)
    i = 0
    if last_incoming is not None:
        if today > last_incoming.last_update.date():
            for item in incoming_list:
                i += 1
                crud.add_store_incoming(db=session, item=item)
        else:
            for item in incoming_list:
                print("ITEM: ", item)
                store_name = item['Store'] if 'Store' in item and item['Store'] is not None else None
                print(store_name, item['Store'])
                nomenclature_id = item['Product.Id'] if 'Product.Id' in item and item[
                    'Product.Id'] is not None else None
                doc_number = item['Document'] if 'Document' in item and item['Document'] is not None else None
                i += 1
                available_store_item = crud.get_store_incoming_item(db=session,
                                                                    store_name=store_name,
                                                                    nomenclature_id=nomenclature_id,
                                                                    doc_number=doc_number
                                                                    )
                if available_store_item:
                    print(f"Was skipped existing {i}-item")
                    continue
                else:
                    crud.add_store_incoming(db=session, item=item)
                    print(f"Was inserted {i}-item")
    else:
        for item in incoming_list:
            i += 1
            crud.add_store_incoming(db=session, item=item)
            print(f"Was inserted {i}-item")

    micro.logout(key=key)


if __name__ == '__main__':
    store_incomings()
