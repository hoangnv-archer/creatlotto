import streamlit as st
import random
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

# Cấu hình trang Streamlit
st.set_page_config(page_title="Máy Tạo Phiếu Lô Tô Xuân", page_icon="🧧")

def generate_grid():
    nums = random.sample(range(1, 91), 24)
    return nums[:12] + ["LỘC XUÂN"] + nums[12:]

def draw_ticket(c, x, y, t_id, studio_name):
    tw, th = 95*mm, 130*mm 
    # Tiêu đề & Logo
    c.setFont("Helvetica-Bold", 16)
    c.setFillColorRGB(0.7, 0, 0) 
    c.drawCentredString(x + tw/2, y + th - 15*mm, "LÔ TÔ XUÂN 2026")
    c.setFont("Helvetica", 9)
    c.setFillColorRGB(0, 0, 0)
    c.drawCentredString(x + tw/2, y + th - 20*mm, f"{studio_name} - Chúc mừng năm mới")

    # Vẽ lưới
    size = 15*mm
    ox, oy = x + (tw - 5*size)/2, y + 25*mm
    data = generate_grid()
    for i in range(5):
        for j in range(5):
            val = data[i*5 + j]
            cur_x, cur_y = ox + j*size, oy + (4-i)*size
            c.rect(cur_x, cur_y, size, size)
            if val == "LỘC XUÂN":
                c.setFont("Helvetica-Bold", 8)
                c.drawCentredString(cur_x + size/2, cur_y + size/2 + 1*mm, "LOC")
                c.drawCentredString(cur_x + size/2, cur_y + size/2 - 3*mm, "XUAN")
            else:
                c.setFont("Helvetica-Bold", 14)
                c.drawCentredString(cur_x + size/2, cur_y + size/2 - 4*mm, str(val))
    
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(x + tw/2, y + 18*mm, "Vạn sự như ý")

# Giao diện người dùng
st.title("🧧 Trình Tạo Phiếu Lô Tô Tết 2026")
studio = st.text_input("Tên của bạn/Studio:", "Archer Studio")
num_tickets = st.slider("Số lượng phiếu:", 4, 100, 60, step=4)

if st.button("🚀 Tạo File PDF Ngay"):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    w, h = A4
    
    for p in range(num_tickets // 4):
        pos = [(0, h/2), (w/2, h/2), (0, 0), (w/2, 0)]
        for i in range(4):
            draw_ticket(c, pos[i][0] + 5*mm, pos[i][1] + 5*mm, p*4 + i + 1, studio)
        c.showPage()
    
    c.save()
    buffer.seek(0)
    
    st.success(f"Đã tạo xong {num_tickets} phiếu!")
    st.download_button(
        label="📥 Tải file PDF về máy",
        data=buffer,
        file_name="Loto_Xuan_2026.pdf",
        mime="application/pdf"
    )
