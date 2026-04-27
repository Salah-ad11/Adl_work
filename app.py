import streamlit as st
import datetime
import pandas as pd
import os

# إعدادات الصفحة
st.set_page_config(page_title="نظام العدل الذكي", page_icon="⚖️")

# ملف حفظ البيانات
DATA_FILE = "attendance_log.csv"

# دالة لحفظ الحركة
def save_data(user, action, status):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data = pd.DataFrame([[now, user, action, status]], columns=["Time", "User", "Action", "Status"])
    if not os.path.isfile(DATA_FILE):
        new_data.to_csv(DATA_FILE, index=False)
    else:
        new_data.to_csv(DATA_FILE, mode='a', header=False, index=False)

st.title("⚖️ Al-Adl Smart System")
st.subheader("نظام العدل لإدارة الحضور والأجور")

# مدخلات المستخدم
user_name = st.text_input("اسم العامل / الموظف")
user_code = st.text_input("الرمز السري الخاص بك", type="password")

col1, col2 = st.columns(2)

with col1:
    if st.button("تسجيل دخول (Check-In)"):
        if user_code == "1234" and user_name:
            save_data(user_name, "In", "Success")
            st.success(f"تم تسجيل دخول {user_name} بنجاح")
        else:
            st.error("تأكد من الاسم والرمز السري")

with col2:
    if st.button("تسجيل خروج (Check-Out)"):
        if user_code == "1234" and user_name:
            save_data(user_name, "Out", "Success")
            st.info(f"تم تسجيل خروج {user_name}")
        else:
            st.error("تأكد من الاسم والرمز السري")

# قسم خاص بالمدير (مخفي برمز خاص)
st.divider()
admin_code = st.text_input("قسم الإدارة (للمدير فقط)", type="password")
if admin_code == "0000": # رمز الإدارة
    st.write("### سجل الحضور والانصراف")
    if os.path.isfile(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        st.dataframe(df)
        # زر لتحميل البيانات كملف Excel
        csv = df.to_csv(index=False).encode('utf-8-sig')
        st.download_button("تحميل السجل بالكامل (Excel)", data=csv, file_name="attendance_report.csv", mime="text/csv")
    else:
        st.write("لا توجد بيانات مسجلة بعد.")
