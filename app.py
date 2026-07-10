import streamlit as st
import os

# ตั้งค่าโฟลเดอร์สำหรับเก็บไฟล์งาน
UPLOAD_DIR = "assignments"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

st.set_page_config(page_title="ระบบส่งงานนักเรียน", layout="centered")
st.title("🎒 ระบบส่งงานและดาวน์โหลดไฟล์งาน")

# เมนูด้านข้างแบ่ง 4 กลุ่ม
page = st.sidebar.radio("เลือกกลุ่มของคุณ", ["กลุ่มที่ 1", "กลุ่มที่ 2", "กลุ่มที่ 3", "กลุ่มที่ 4"])

# สร้างโฟลเดอร์ย่อยแยกกลุ่ม
group_dir = os.path.join(UPLOAD_DIR, page.replace(" ", "_"))
if not os.path.exists(group_dir):
    os.makedirs(group_dir)

st.header(f"📂 พื้นที่จัดการไฟล์: {page}")
st.write("---")

# 1. ส่วนการอัปโหลด
st.subheader("📤 อัปโหลดไฟล์งาน")
uploaded_file = st.file_uploader("ลากไฟล์มาวางหรือกดค้นหาไฟล์ (จำกัดไม่เกิน 200MB)", key=page)

if uploaded_file is not None:
    file_path = os.path.join(group_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"🎉 อัปโหลดไฟล์ '{uploaded_file.name}' เข้าสู่ {page} เรียบร้อย!")

st.write("---")

# 2. ส่วนการดาวน์โหลด
st.subheader("📥 รายการไฟล์ที่สามารถดาวน์โหลดได้")
files = os.listdir(group_dir)

if len(files) == 0:
    st.info("ยังไม่มีไฟล์ถูกอัปโหลดในกลุ่มนี้")
else:
    for file_name in files:
        file_path = os.path.join(group_dir, file_name)
        with open(file_path, "rb") as file:
            st.download_button(
                label=f"📄 ดาวน์โหลด: {file_name}",
                data=file,
                file_name=file_name,
                mime="application/octet-stream"
            )