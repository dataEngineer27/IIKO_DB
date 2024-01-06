from helpers.database import SessionLocal
from helpers import crud, micro


def nomenclature_categories():
    session = SessionLocal()
    key = micro.login()
    try:
        categories = micro.category_list(key=key)
    except:
        key = micro.login()
        categories = micro.category_list(key=key)

    crud.add_categories(db=session, category_list=categories)
    micro.logout(key=key)


if __name__ == '__main__':
    nomenclature_categories()
