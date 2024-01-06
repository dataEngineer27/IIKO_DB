from helpers.database import SessionLocal
from helpers import crud, micro


def nomenclatures():
    session = SessionLocal()
    key = micro.login()
    try:
        nomenclature_list = micro.nomenclature_list(key=key)
    except:
        key = micro.login()
        nomenclature_list = micro.nomenclature_list(key=key)

    crud.add_nomenclatures(db=session, nomenclature_list=nomenclature_list)
    micro.logout(key=key)


if __name__ == '__main__':
    nomenclatures()
