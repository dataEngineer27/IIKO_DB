from helpers.database import SessionLocal
from helpers import crud, micro


def stores():
    session = SessionLocal()
    key = micro.login()
    try:
        store_list = micro.store_list(key=key)
    except:
        key = micro.login()
        store_list = micro.store_list(key=key)
    crud.add_stores(db=session, store_list=store_list)
    micro.logout(key=key)


if __name__ == '__main__':
    stores()
