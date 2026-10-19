# Làm việc trực tiếp trong Figma

## Trước khi ghi

1. Dùng connector/API Figma được kết nối nếu phù hợp; đọc skill Figma tương ứng đang được môi trường cung cấp trước thao tác có yêu cầu đó. Skill này không thay thế tài liệu API và không hardcode một bộ tool duy nhất.
2. Giải quyết file đích: dùng link/file key do người dùng cung cấp. Nếu cần file mới, dùng quy trình tạo file của connector; nếu connector yêu cầu chọn nhóm trong tài khoản nhiều nhóm, hỏi lựa chọn. Không đoán node ID, nhóm hay quyền truy cập.
3. Đọc file/page liên quan: nội dung có sẵn, component, token, font và quy ước tên. Chọn chỗ đặt rõ ràng, không đè bản cũ khi yêu cầu là làm thêm phương án.
4. Xác định đầu ra: editable Design layers cho yêu cầu thiết kế UI thông thường; Code/Make hay prototype chạy là loại khác, chỉ dùng khi yêu cầu phù hợp.

## Dựng các lớp thật

- Tạo container và Auto Layout trước; đặt nội dung ngay bên trong cấu trúc đích. Dùng kích thước/constraint phù hợp cho văn bản dài, wrap và responsive.
- Tải đúng font hiện có trước sửa chữ. Kiểm tra dấu tiếng Việt ở tiêu đề và thân. Font không có phải báo/thay bằng lựa chọn tương thích có lý do, không giả vờ đã dùng đúng.
- Tái sử dụng token/style/component tương thích. Với thành phần lặp lại, tạo phần dùng chung trong phạm vi; không tự tạo cả thư viện ngoài yêu cầu.
- Text phải là text chỉnh sửa được; icon/hình trang trí có thể là vector; ảnh nội dung có thể là bitmap riêng lẻ. Không giao screenshot cả UI dưới dạng một frame rồi gọi là thiết kế editable.
- Dùng hình có quyền sử dụng và ghi nguồn đúng. Minh hoạ mới hoặc placeholder phải được ghi rõ, không tự gắn danh nghĩa đã thẩm định.
- Ghi lại ID node/file cùng kết quả thao tác ở hồ sơ dự án; không phụ thuộc biến tạm trong phiên khi công cụ không lưu trạng thái.

## Prototype và chất lượng

Đối với yêu cầu prototype, nối tác vụ chính và các trạng thái cần thử. Nếu chỉ giao màn hình tĩnh, nói đúng loại đầu ra; không gọi là prototype tương tác.

Kiểm tra cấu trúc và screenshot sau một đợt dựng hoàn chỉnh. Sửa lỗi quan sát được rồi kiểm tra lại vùng ảnh hưởng: chữ tràn, nút bị cắt, chồng lớp, kích thước thẻ, vùng điều hướng và tương phản. Không lặp chụp ảnh khi chưa có thay đổi liên quan.

Khi API báo lỗi có thể thực thi một phần, đọc lại canvas trước khi retry để tránh tạo bản trùng. Nếu không thể kiểm tra bằng ảnh, báo giới hạn thay vì khẳng định đã QA thị giác.

Giao link file và node của phương án cuối, desktop/mobile thuộc phạm vi, trạng thái static/prototype, phần chưa có dữ liệu, kết quả kiểm tra. Giữ thiết kế cũ nếu người dùng muốn so sánh.
