# Kiểm tra bản bàn giao

Ngày kiểm tra: 19/10/2026.

| Kiểm tra | Kết quả |
|---|---|
| `scripts/check_repo.py` | Đạt: file bắt buộc, tên/mô tả skill, liên kết Markdown nội bộ, 9 mẫu, default prompt |
| `unittest` | 11/11 đạt: 6 kiểm tra tạo dự án và 5 kiểm tra token/alias, gồm target thiếu, resolve sai, màu sai và lệch kiểu |
| `check_tokens.py` | Đạt: 104 token Base và 24 Alias; mọi target có thật và giá trị resolve khớp |
| Bản token đóng gói | Giữ nguyên byte của hai file export người dùng cung cấp; chỉ đổi tên để tách Base/Alias |
| Chạy CLI tạo dự án thật trong thư mục làm việc riêng | Đạt: 9 tài liệu UTF-8 và project.json; mọi giai đoạn `not_started` |
| `quick_validate.py` của skill-creator | Đã thử; không chạy xong vì Python đi kèm môi trường chưa có PyYAML |

Trong môi trường sandbox Windows của lần kiểm tra này, thư mục temp mặc định không ghi được. Các test được chạy lại thành công bằng thư mục temp nằm trong workspace. Không thay cấu hình máy hoặc cài thêm package.

Kiểm tra này không phải forward-test bằng agent độc lập, không kiểm thử tài khoản Tavily/Figma và không chứng minh một sản phẩm đạt tiêu chuẩn UX/WCAG. Repo không tự gọi dịch vụ bên ngoài, không chứa token và không đóng gói dữ liệu nghiên cứu cá nhân.

Để chạy thêm validator chính thức ở môi trường có PyYAML: dùng `quick_validate.py` của skill-creator với đường dẫn `skills/ui-ux-workflow`.
