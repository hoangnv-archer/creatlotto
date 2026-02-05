import random
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

def generate_grid():
    # Lấy 24 số ngẫu nhiên từ 1-90
    nums = random.sample(range(1, 91), 24)
    # Chèn ô "LỘC XUÂN" vào chính giữa (vị trí index 12)
    grid = nums[:12] + ["LỘC XUÂN"] + nums[12:]
    return grid

def draw_ticket(c, x, y, t_id):
    # Khung phiếu (Dựa trên mẫu của bạn)
    tw, th = 95*mm, 130*mm 
    
    # Tiêu đề
    c.setFont("Helvetica-Bold", 16)
    c.setFillColorRGB(0.6, 0, 0) # Màu đỏ đậm
    c.drawCentredString(x + tw/2, y + th - 15*mm, "LÔ TÔ XUÂN 2026")
    
    c.setFont("Helvetica", 9)
    c.setFillColorRGB(0, 0, 0)
    c.drawCentredString(x + tw/2, y + th - 20*mm, "Archer Studio - Chuc mung nam moi")

    # Vẽ lưới 5x5
    size = 15*mm
    ox = x + (tw - 5*size)/2
    oy = y + 25*mm
    
    data = generate_grid()
    for i in range(5):
        for j in range(5):
            val = data[i*5 + j]
            cur_x, cur_y = ox + j*size, oy + (4-i)*size
            c.setLineWidth(1)
            c.rect(cur_x, cur_y, size, size)
            
            if val == "LỘC XUÂN":
                c.setFont("Helvetica-Bold", 8)
                c.drawCentredString(cur_x + size/2, cur_y + size/2 + 1*mm, "LOC")
                c.drawCentredString(cur_x + size/2, cur_y + size/2 - 3*mm, "XUAN")
            else:
                c.setFont("Helvetica-Bold", 14)
                c.drawCentredString(cur_x + size/2, cur_y + size/2 - 4*mm, str(val))

    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(x + tw/2, y + 18*mm, "Loc day nha")
    c.setFont("Helvetica", 7)
    c.drawRightString(x + tw - 5*mm, y + th - 5*mm, f"Phieu {t_id}")

def create_loto_pdf():
    c = canvas.Canvas("Loto_Xuan_60Phieu.pdf", pagesize=A4)
    w, h = A4
    for p in range(15): # 15 trang x 4 phiếu = 60 phiếu
        # Tọa độ 4 phiếu trên trang A4
        pos = [(0, h/2), (w/2, h/2), (0, 0), (w/2, 0)]
        for i in range(4):
            draw_ticket(c, pos[i][0] + 5*mm, pos[i][1] + 5*mm, p*4 + i + 1)
        c.showPage()
    c.save()

if __name__ == "__main__":
    create_loto_pdf()
    print("Xong! File 'Loto_Xuan_60Phieu.pdf' da xuat hien trong thu muc cua ban.")
