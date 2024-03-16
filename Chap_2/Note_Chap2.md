# Note chap 2: 
## Đặt vấn đề 
- Thiết kế cửa ra vào cho nhà cho chó mở tự động với một nút ấn

## Thiết kế ban đầu 
- Ban đầu thiết kế gồm 2 lớp : 
    1. DogDoor : trực tiếp điều khiển cửa đóng mở 
    2. Remote : đưa tín hiệu để door mở đóng qua thao tác nhấn nút 

![image](Image\Implement_1.png)

=> Tuy nhiên thiết kế chưa tốt khi động vật khác có thể vào 
=> Thao tác đóng mở gây phiền toái nếu người dùng quên 

## Thu thập yêu cầu người dùng 
1. Thu thập yêu cầu từ dog door 
2. Tìm xem door nên hoạt động như thế nào 
3. Lấy thêm thông tin bổ sung từ khách hàng 
4. Xây dụng door đúng 


## Yêu cầu người dùng 
- Yêu cầu của người dùng nhiều hơn những gì họ muốn. Một tập yêu cầu tốt không chỉ là những điều mà khách hàng nói còn phải đảm bảo hệ thống hoạt động, tránh trường hợp bất thường, không như kì vọng 

## Sơ đồ use case : 
1. Là kĩ năng dùng để nắm bắt những yêu cầu tiềm năng của hệ thống mới và thay đổi phần mềm. Mỗi use case là một hoặc nhiều tình huống biểu diễn sao hệ thống tương tác với người dùng cuối và đạt được mục tiêu cụ thể <br>
- Một use case phải có 3 yếu tố : <br>
    1. Một use case phải có một giá trị cụ thể dành cho người dùng <br>
    2. Một use case phải có điểm đầu và điểm kết thúc <br>
    3. Một use case phải bắt đầu từ một đối tượng bên ngoài hệ thống 


## Requirement 
1. Cửa phải có chiều cao 12' <br>
2. Nút trên điều khiển mở cửa nếu nó đóng và đóng nó nếu nó mở cửa <br>
3. Khi của được mở, nó nên được đóng tự động 