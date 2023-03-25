n = int(input("Nhập số n: "))  # Nhập số n từ bàn phím và lưu giá trị đó vào biến n.

if n >= 2:  # Nếu n lớn hơn hoặc bằng 2
    sum = 0  # Khởi tạo biến sum bằng 0
    for i in range(2, n+1, 2):  # Lặp qua các số chẵn từ 2 đến n
        sum += i  # Cộng giá trị của i vào biến sum
    print("Tổng các số chẵn từ 1 đến", n, "là", sum)  # In ra màn hình tổng các số chẵn từ 1 đến n
else:  # Nếu n nhỏ hơn 2
    print("n phải lớn hơn hoặc bằng 2.")  # In ra màn hình "n phải lớn hơn hoặc bằng 2."
