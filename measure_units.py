from helpers.database import SessionLocal
from helpers import crud, micro


def units():
    session = SessionLocal()
    key = micro.login()
    root_type_list = ["Account", "AccountingCategory", "AlcoholClass", "AllergenGroup", "AttendanceType", "Conception",
                      "CookingPlaceType", "DiscountType", "MeasureUnit", "OrderType", "PaymentType", "ProductCategory",
                      "ProductScale", "ProductSize", "ScheduleType", "TaxCategory"]
    for root_type in root_type_list:
        try:
            unit_list = micro.unit_list(root_type=root_type, key=key)
        except:
            key = micro.login()
            unit_list = micro.unit_list(root_type=root_type, key=key)
        crud.add_units(db=session, unit_list=unit_list)

    micro.logout(key=key)


if __name__ == '__main__':
    units()
