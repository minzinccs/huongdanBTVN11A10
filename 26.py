a = input("Nhập vào xâu a: ")  # Nhập xâu a từ bàn phím và lưu giá trị đó vào biến a.
b = input("Nhập vào xâu b: ")  # Nhập xâu b từ bàn phím và lưu giá trị đó vào biến b.

if a[0] == b[-1]:  # Nếu kí tự đầu tiên của xâu a giống với kí tự cuối cùng của xâu b
    print("Kí tự đầu của", a, "giống kí tự cuối của", b)  # In ra màn hình "Kí tự đầu của <xâu a> giống kí tự cuối của <xâu b>"
else:  # Nếu kí tự đầu tiên của xâu a không giống với kí tự cuối cùng của xâu b
    print("Kí tự đầu của", a, "không giống kí tự cuối của", b)  # In ra màn hình "Kí tự đầu của <xâu a> không giống kí tự cuối của <xâu b>"
