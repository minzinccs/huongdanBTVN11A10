N = input("Nhập dãy số cách nhau bởi dấu cách: ")  # Nhập dãy số từ bàn phím và lưu giá trị đó vào biến N.
N = N.split()  # Tách các phần tử trong dãy số bằng dấu cách và lưu kết quả vào biến N.
N = [int(i) for i in N]  # Chuyển các phần tử trong dãy số thành kiểu số nguyên và lưu kết quả vào biến N.

min_element = min(N)  # Tìm phần tử bé nhất trong dãy số và lưu giá trị đó vào biến min_element.

print("Phần tử bé nhất trong dãy số là:", min_element)  # In ra màn hình "Phần tử bé nhất trong dãy số là: <min_element>"
