from helpers.database import SessionLocal
from helpers import crud, micro


def department_revenue():
    session = SessionLocal()
    department_list = crud.get_all_departments(db=session)
    d = 0
    for department in department_list:
        key = micro.login()
        d += 1
        department_id = department.id
        if department.is_added == 0:
            try:
                revenue_list = micro.department_revenue(key=key, department=department_id)['dayDishValues']['dayDishValue']
            except:
                crud.update_department(db=session, id=department_id)
                continue
            for item in revenue_list:
                date = item['date'] if "date" in item and item['date'] else None
                nomenclature_id = item['productId'] if "productId" in item and item['productId'] else None
                crud.add_department_revenue(db=session, item=item, department_id=department_id)
                print(f"Was inserted department №{d} - {department_id}: product-{nomenclature_id} in {date}")
            crud.update_department(db=session, id=department_id)
            # for item in revenue_list:
            #     date = item['date'] if "date" in item and item['date'] else None
            #     nomenclature_id = item['productId'] if "productId" in item and item['productId'] else None
            #     available_item = crud.get_revenue_item(db=session, date=date, department_id=department_id,
            #                                            nomenclature_id=nomenclature_id)
            #     if available_item:
            #         print(f"Exist item of department №{d} ({department_id}) in {date}: product - {nomenclature_id}")
            #         continue
            #     else:
            #         crud.add_department_revenue(db=session, item=item, department_id=department_id)
            #         crud.update_department(db=session, id=department_id)
            #         print(f"Was inserted department №{d} - {department_id}: in {date}")

        micro.logout(key=key)


if __name__ == '__main__':
    department_revenue()
