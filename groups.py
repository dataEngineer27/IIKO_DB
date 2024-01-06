from helpers.database import SessionLocal
from helpers import crud, micro


def nomenclature_groups():
    session = SessionLocal()
    key = micro.login()
    try:
        group_list = micro.nomenclature_groups(key=key)
    except:
        key = micro.login()
        group_list = micro.nomenclature_groups(key=key)

    crud.add_groups(db=session, group_list=group_list)
    micro.logout(key=key)


if __name__ == '__main__':
    nomenclature_groups()
