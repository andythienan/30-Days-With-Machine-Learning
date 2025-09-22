1. Tính giai thừa
Nhập vào số n, tính n! bằng vòng lặp (không dùng math.factorial)

2. Nhập chuỗi, kiểm tra xem chuỗi đó có phải palindrome (đối xứng) không.
Ví dụ: "radar": có, "hello": không

3.In hình tam giác số

Nhập số n, in ra tam giác số:

Ví dụ n=5:

1
12
123
1234
12345

4. Sudoku Validator
Cho một bảng Sudoku 9x9, viết hàm kiểm tra xem nó có hợp lệ hay không (mỗi hàng, mỗi cột và mỗi ô 3x3 không được trùng số).

5. Viết chương trình nhập vào ngày, tháng, năm (giả sử nhập đúng, không cần kiểm tra hợp lệ). Tìm xem ngày đó là ngày thứ bao nhiêu trong năm
Nếu không dùng vòng lặp, có thể dùng công thức sau:
sum = (int) (30.42 * (month - 1)) + day

Nếu month = 2, hoặc năm nhuận và month > 2 thì sum = sum + 1
Nếu 2 < month < 8 thì sum = sum - 1
