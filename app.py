import streamlit as st
import os

# ตั้งค่าโฟลเดอร์สำหรับเก็บไฟล์งาน
UPLOAD_DIR = "assignments"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# ตั้งค่าหัวข้อเว็บและหน้าตาเว็บ (เปลี่ยนชื่อระบบเป็น Electives AI Robotics)
st.set_page_config(page_title="Electives AI Robotics", layout="centered", page_icon="🤖")
st.title("🤖 Electives AI Robotics")
st.subheader("สำหรับส่งไฟล์งานแต่ละกลุ่ม")

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
    # สั่งให้แอปรีรันเพื่อแสดงไฟล์ใหม่ในรายการทันที
    st.rerun()

st.write("---")

# 2. ส่วนการจัดการไฟล์ (ดาวน์โหลด และ ลบไฟล์)
st.subheader("📥 รายการไฟล์ในกลุ่ม")
files = os.listdir(group_dir)

if len(files) == 0:
    st.info("ยังไม่มีไฟล์ถูกอัปโหลดในกลุ่มนี้")
else:
    for file_name in files:
        file_path = os.path.join(group_dir, file_name)
        
        # จัดระเบียบหน้าจอเป็น 2 คอลัมน์: คอลัมน์ที่ 1 โชว์ปุ่มดาวน์โหลด, คอลัมน์ที่ 2 โชว์ปุ่มลบไฟล์
        col1, col2 = st.columns([4, 1.2])
        
        with col1:
            with open(file_path, "rb") as file:
                st.download_button(
                    label=f"📄 ดาวน์โหลด: {file_name}",
                    data=file,
                    file_name=file_name,
                    mime="application/octet-stream",
                    key=f"download_{file_name}_{page}"  # ป้องกันไม่ให้ Key ซ้ำกัน
                )
        
        with col2:
            # เพิ่มปุ่มสำหรับลบไฟล์ออก
            if st.button("🗑️ ลบไฟล์", key=f"delete_{file_name}_{page}", type="secondary"):
                try:
                    os.remove(file_path)
                    st.toast(f"ลบไฟล์ {file_name} สำเร็จ!")
                    # สั่งรีรันเพื่อลบไฟล์นั้นออกจากรายการหน้าจอทันที
                    st.rerun()
                except Exception as e:
                    st.error(f"ไม่สามารถลบไฟล์ได้เนื่องจาก: {e}")
                    
        st.write("") # เพิ่มช่องว่างเว้นระยะห่างเล็กน้อยระว่างบรรทัดของแต่ละไฟล์
```
eof

---

### 🛠️ วิธีการอัปเดตไฟล์บน GitHub ของคุณครู:

อ้างอิงจากรูปภาพประกอบ `image_19279d.png` ที่คุณครูส่งมา ให้ทำตามขั้นตอนง่ายๆ ดังนี้ครับ:

1. เปิดหน้าเว็บ GitHub ไปที่คลัง `samtnp123-svg/student-upload-web` ของครู
2. คลิกเข้าไปที่ไฟล์ **`app.py`** 
3. มองหา **สัญลักษณ์รูปดินสอ (Edit this file)** บริเวณมุมขวาบนของหน้าต่างโค้ด แล้วกดเข้าไป
4. ทำการลบโค้ดเก่าทั้งหมดทิ้ง แล้ว**คัดลอกโค้ดใหม่ด้านบนไปวางแทนที่**
5. เลื่อนหน้าจอลงมาด้านล่างสุด กดปุ่มสีเขียวที่เขียนว่า **"Commit changes..."** เพื่อบันทึกไฟล์

**หลังจากบันทึกเสร็จเรียบร้อยแล้ว:**
ระบบของ Streamlit Cloud ที่เปิดออนไลน์อยู่จะตรวจจับการอัปเดตนี้โดยอัตโนมัติ และจะทำการอัปเกรดหน้าเว็บให้เป็นเวอร์ชันใหม่ที่มีปุ่มลบไฟล์และชื่อใหม่ให้เลยภายในเวลาไม่เกิน 1 นาทีครับ! ลองกดเล่นดูได้เลยนะครับ หากติดตรงไหนสามารถสอบถามได้เสมอครับ