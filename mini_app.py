# برنامج التبرع المصغر
users = []
projects = []

def register():
    fname = input("الاسم الاول: ")
    lname = input("الاسم الاخير: ")
    
    email = input("الايميل: ")
    while "@" not in email or "." not in email:
        email = input("ايميل صحيح: ")
    
    password = input("كلمة المرور: ")
    confirm = input("تأكيد كلمة المرور: ")
    while password != confirm:
        password = input("كلمة المرور: ")
        confirm = input("تأكيد كلمة المرور: ")
    
    phone = input("رقم الموبايل: ")
    while len(phone) != 11 or not phone.startswith("01"):
        phone = input("رقم موبايل صحيح (01xxxxxxxxx): ")
    
    users.append([fname, lname, email, password, phone])
    print("تم التسجيل")

def login():
    email = input("الايميل: ")
    password = input("كلمة المرور: ")
    
    for user in users:
        if user[2] == email and user[3] == password:
            print("مرحبا " + user[0])
            return email
    print("خطأ في البيانات")
    return None

def create_project(user_email):
    title = input("عنوان المشروع: ")
    details = input("التفاصيل: ")
    target = float(input("المبلغ: "))
    start = input("تاريخ البداية: ")
    end = input("تاريخ النهاية: ")
    
    projects.append([user_email, title, details, target, start, end])
    print("تم انشاء المشروع")

def view_projects():
    for i, p in enumerate(projects):
        print(f"{i+1}. {p[1]} - {p[0]} - {p[3]} جنيه")

def edit_project(user_email):
    my_projects = [i for i, p in enumerate(projects) if p[0] == user_email]
    if not my_projects:
        print("لا توجد مشاريع")
        return
    
    for i, idx in enumerate(my_projects):
        print(f"{i+1}. {projects[idx][1]}")
    
    choice = int(input("اختر رقم المشروع: ")) - 1
    idx = my_projects[choice]
    
    new_title = input("عنوان جديد: ")
    if new_title:
        projects[idx][1] = new_title
    print("تم التعديل")

def delete_project(user_email):
    my_projects = [i for i, p in enumerate(projects) if p[0] == user_email]
    if not my_projects:
        print("لا توجد مشاريع")
        return
    
    for i, idx in enumerate(my_projects):
        print(f"{i+1}. {projects[idx][1]}")
    
    choice = int(input("اختر رقم المشروع للحذف: ")) - 1
    idx = my_projects[choice]
    
    projects.pop(idx)
    print("تم الحذف")

def search_by_date():
    date = input("التاريخ: ")
    for p in projects:
        if p[4] <= date <= p[5]:
            print(f"{p[1]} - {p[0]}")

def project_menu(user_email):
    while True:
        print("\n1.انشاء 2.عرض 3.تعديل 4.حذف 5.بحث 6.خروج")
        choice = input("اختر: ")
        
        if choice == "1": create_project(user_email)
        elif choice == "2": view_projects()
        elif choice == "3": edit_project(user_email)
        elif choice == "4": delete_project(user_email)
        elif choice == "5": search_by_date()
        elif choice == "6": break

def main():
    while True:
        print("\n1.تسجيل 2.دخول 3.خروج")
        choice = input("اختر: ")
        
        if choice == "1": register()
        elif choice == "2":
            user = login()
            if user: project_menu(user)
        elif choice == "3": break

main()