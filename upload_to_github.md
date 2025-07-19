# 📤 رفع المشروع على GitHub

## الطريقة السهلة (من الموقع):

### 1. انشاء Repository:
- ادخل على `github.com`
- اضغط زر "New" الأخضر
- اكتب اسم المشروع: `crowdfunding-console-app`
- خليه Public
- اضغط "Create repository"

### 2. رفع الملفات:
- اضغط "uploading an existing file"
- ارفع الملفات دي:
  - `mini_app.py` (الملف الرئيسي)
  - `README_MINI.md` (الشرح)

### 3. Commit:
- اكتب رسالة: "Add crowdfunding console app"
- اضغط "Commit changes"

## الطريقة من Terminal:

```bash
# 1. انشئ repository جديد على GitHub الاول
# 2. بعدين اعمل كده:

git init
git add mini_app.py README_MINI.md
git commit -m "Add simple crowdfunding app"
git branch -M main
git remote add origin https://github.com/USERNAME/crowdfunding-console-app.git
git push -u origin main
```

## ملاحظات مهمة:
- غير `USERNAME` باسم المستخدم بتاعك
- تأكد إن Repository اتعمل الأول على GitHub
- لو طلب منك Username/Password استخدم Personal Access Token

## الملفات المطلوبة:
✅ `mini_app.py` - البرنامج الرئيسي  
✅ `README_MINI.md` - شرح المشروع  

**بكده المشروع هيبقى على GitHub ومنتورك يقدر يشوفه! 🚀**