# Ghi chú Chap 1 (English below) :

## Vấn đề 1: Thỏa mãn nhu cầu khách hàng
### 1. Cài đặt 1 : 
![image](Image\Implement_1.png)
- Đánh giá cài đặt : Cài đặt không tối ưu do xử lý tìm kiếm thông qua string dẫn tới sai kết quả. => Vi phạm điều kiện đầu tiên của một phần mềm tốt 

### 2. Cài đặt 2 : 

![image](Image\Implement_2.png)
- Đánh giá cài đặt : Loại bỏ vấn đề của cài đặt 1 : thay thế dữ liệu từ String -> Enum 
=> Đưa ra vấn đề mới : Chỉ tìm kiếm được 1 sản phẩm duy nhất trong khi 2 sản phẩm tương tự nhau khác thuộc tính string -> Cần search method đưa ra nhiều hơn 1 lựa chọn 

## Vấn đề 2 : Áp dụng các nguyên tắc OO 
- Đặt vấn đề: Người dùng muốn tìm kiếm guitar tuy nhiên chỉ đưa ra một số đặc điểm không đưa toàn bộ do đó phương thức search không hiệu quả -> cách cải tiến ? 
- Tạo một đối tượng mới (GuitarSpec) lưu nhưng properties của Guitar -> Thiết kế lặp lại code 
-  Sử dụng OO  principle để giải quyết : Thay vì tạo ra một đối tượng public lưu tính chất của guitar -> đóng gói (encapsulate) nó thành đối tượng private 
![image](Image\Implement_3.png)

## Vấn đề 3: Cố gắng cho khả năng bảo trì và tái sử dụng thiết kế 
- Đặt vấn đề : Yêu cầu thêm một thuộc tính mới  (số lượng dây đàn) vào trong thiết kế
- Phân tích thiết kế cũ :  Nếu thêm thuộc tính mới vào spec : 
    1. Cần chỉnh sửa lại constructor của đối tượng Guitar -> thêm attribute mới 
    2. Thay đổi hàm addguitar trong Inventory 
    3. Hàm search không dễ để tái sử dụng -> thêm phép so sánh spec 
=> Thay đổi code trong Inventory lẫn  Guitar để thêm thuộc tính mới cho đàn vốn do spec đảm nhiệm 
- Giải quyết : 
    1. Thêm  thuộc tính numString vào spec 
    2. Sửa lại constructor của guitar, thay vì thêm từng attribute thì chỉ cần thêm spec 
    3. Thay đổi hàm so sánh trong search thành một hàm 'delegate' hơn 
    4. Update lại test 