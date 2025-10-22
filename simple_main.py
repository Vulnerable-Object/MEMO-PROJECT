# برنامج التبرع البسيط
# كتبه: طالب مبتدئ

# استيراد المكتبات
import re

# متغيرات عامة
users = []
projects = []

def check_email(email):
    # فحص الايميل بسيط
    if "@" in email and "." in email:
        return True
    return False

def check_phone(phone):
    # فحص رقم الموبايل المصري
    if len(phone) == 11 and phone.startswith("01"):
        return True
    return False

def register():
    print("تسجيل مستخدم جديد")
    fname = input("الاسم الاول: ")
    lname = input("الاسم الاخير: ")
    
    while True:
        email = input("الايميل: ")
        if check_email(email):
            # تحقق من عدم وجود الايميل
            found = False
            for user in users:
                if user[2] == email:
                    found = True
                    break
            if not found:
                break
            else:
                print("الايميل موجود فعلا")
        else:
            print("ايميل غير صحيح")
    
    while True:
        password = input("كلمة المرور: ")
        confirm = input("تأكيد كلمة المرور: ")
        if password == confirm:
            break
        else:
            print("كلمة المرور غير متطابقة")
    
    while True:
        phone = input("رقم الموبايل: ")
        if check_phone(phone):
            break
        else:
            print("رقم موبايل غير صحيح")
    
    # حفظ المستخدم
    user = [fname, lname, email, password, phone]
    users.append(user)
    print("تم التسجيل بنجاح")

def login():
    print("تسجيل الدخول")
    email = input("الايميل: ")
    password = input("كلمة المرور: ")
    
    # البحث عن المستخدم
    for user in users:
        if user[2] == email and user[3] == password:
            print("مرحبا " + user[0])
            return email
    
    print("بيانات خاطئة")
    return None

def create_project(user_email):
    print("انشاء مشروع جديد")
    title = input("عنوان المشروع: ")
    details = input("تفاصيل المشروع: ")
    
    while True:
        try:
            target = float(input("المبلغ المطلوب: "))
            if target > 0:
                break
            else:
                print("المبلغ يجب ان يكون اكبر من صفر")
        except:
            print("ادخل رقم صحيح")
    
    start_date = input("تاريخ البداية (YYYY-MM-DD): ")
    end_date = input("تاريخ النهاية (YYYY-MM-DD): ")
    
    # حفظ المشروع
    project = [user_email, title, details, target, start_date, end_date]
    projects.append(project)
    print("تم انشاء المشروع")

def view_projects():
    print("جميع المشاريع:")
    if len(projects) == 0:
        print("لا توجد مشاريع")
        return
    
    for i, project in enumerate(projects):
        print(f"مشروع رقم {i+1}:")
        print(f"المالك: {project[0]}")
        print(f"العنوان: {project[1]}")
        print(f"التفاصيل: {project[2]}")
        print(f"المبلغ: {project[3]}")
        print(f"من {project[4]} الى {project[5]}")
        print("-" * 30)

def edit_project(user_email):
    print("تعديل مشاريعي")
    my_projects = []
    
    # البحث عن مشاريع المستخدم
    for i, project in enumerate(projects):
        if project[0] == user_email:
            my_projects.append([i, project])
    
    if len(my_projects) == 0:
        print("ليس لديك مشاريع")
        return
    
    # عرض مشاريع المستخدم
    for i, (idx, project) in enumerate(my_projects):
        print(f"{i+1}. {project[1]}")
    
    try:
        choice = int(input("اختر رقم المشروع: ")) - 1
        project_idx = my_projects[choice][0]
        
        print("اترك فارغ للاحتفاظ بالقيمة الحالية")
        new_title = input(f"العنوان الجديد [{projects[project_idx][1]}]: ")
        if new_title:
            projects[project_idx][1] = new_title
        
        new_details = input(f"التفاصيل الجديدة [{projects[project_idx][2]}]: ")
        if new_details:
            projects[project_idx][2] = new_details
        
        print("تم التعديل")
        
    except:
        print("اختيار خاطئ")

def delete_project(user_email):
    print("حذف مشروع")
    my_projects = []
    
    # البحث عن مشاريع المستخدم
    for i, project in enumerate(projects):
        if project[0] == user_email:
            my_projects.append([i, project])
    
    if len(my_projects) == 0:
        print("ليس لديك مشاريع")
        return
    
    # عرض مشاريع المستخدم
    for i, (idx, project) in enumerate(my_projects):
        print(f"{i+1}. {project[1]}")
    
    try:
        choice = int(input("اختر رقم المشروع للحذف: ")) - 1
        project_idx = my_projects[choice][0]
        
        confirm = input("هل انت متأكد؟ اكتب 'نعم' للتأكيد: ")
        if confirm == "نعم":
            projects.pop(project_idx)
            print("تم الحذف")
        else:
            print("تم الالغاء")
            
    except:
        print("اختيار خاطئ")

def search_by_date():
    search_date = input("ادخل التاريخ للبحث (YYYY-MM-DD): ")
    print(f"المشاريع النشطة في {search_date}:")
    
    found = False
    for project in projects:
        if project[4] <= search_date <= project[5]:
            print(f"العنوان: {project[1]}")
            print(f"المالك: {project[0]}")
            print(f"المبلغ: {project[3]}")
            print("-" * 20)
            found = True
    
    if not found:
        print("لا توجد مشاريع في هذا التاريخ")

def project_menu(user_email):
    while True:
        print("\nقائمة المشاريع")
        print("1. انشاء مشروع")
        print("2. عرض جميع المشاريع")
        print("3. تعديل مشاريعي")
        print("4. حذف مشروع")
        print("5. البحث بالتاريخ")
        print("6. العودة للقائمة الرئيسية")
        
        choice = input("اختر: ")
        
        if choice == "1":
            create_project(user_email)
        elif choice == "2":
            view_projects()
        elif choice == "3":
            edit_project(user_email)
        elif choice == "4":
            delete_project(user_email)
        elif choice == "5":
            search_by_date()
        elif choice == "6":
            break
        else:
            print("اختيار خاطئ")

def main():
    print("مرحبا بك في برنامج التبرعات")
    
    while True:
        print("\nالقائمة الرئيسية")
        print("1. تسجيل مستخدم جديد")
        print("2. تسجيل الدخول")
        print("3. خروج")
        
        choice = input("اختر: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            user_email = login()
            if user_email:
                project_menu(user_email)
        elif choice == "3":
            print("شكرا لك!")
            break
        else:
            print("اختيار خاطئ، حاول مرة اخرى")

# تشغيل البرنامج
if __name__ == "__main__":
    main()