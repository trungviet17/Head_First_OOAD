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