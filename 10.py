diem = float(input("Nhập điểm của học sinh: "))  # Nhập điểm của học sinh từ bàn phím và lưu giá trị đó vào biến diem.

if diem >= 8.0:  # Nếu điểm của học sinh lớn hơn hoặc bằng 8.0
    print("Học lực của học sinh là giỏi.")  # In ra màn hình "Học lực của học sinh là giỏi."
elif diem >= 6.5:  # Nếu điểm của học sinh lớn hơn hoặc bằng 6.5
    print("Học lực của học sinh là khá.")  # In ra màn hình "Học lực của học sinh là khá."
elif diem >= 5.0:  # Nếu điểm của học sinh lớn hơn hoặc bằng 5.0
    print("Học lực của học sinh là trung bình.")  # In ra màn hình "Học lực của học sinh là trung bình."
else:  # Nếu điểm của học sinh nhỏ hơn 5.0
    print("Học lực của học sinh là yếu.")  # In ra màn hình "Học lực của học sinh là yếu."
