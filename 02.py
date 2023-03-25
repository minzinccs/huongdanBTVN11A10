import math  # import thư viện toán học của Python để sử dụng hằng số pi.

r = float(input('Nhập r là bán kính của hình tam giác:'))  # nhập bán kính của hình tròn từ bàn phím và lưu giá trị đó vào biến r. Lưu ý rằng giá trị nhập vào phải là một số thực (float).

s = r * math.pi  # tính diện tích hình tròn bằng công thức S = r^2 * pi và lưu giá trị đó vào biến s.

print('Diện tích hình tròn là', s)  # in ra màn hình diện tích hình tròn.
