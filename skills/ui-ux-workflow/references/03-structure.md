# 03 · Nội dung, luồng và wireframe

## Tổ chức nội dung

Kiểm kê nội dung thật, trạng thái xuất bản, độ dài, nguồn, lứa tuổi và hành động khả dụng. Giữ sự khác biệt giữa dữ liệu thật, nội dung minh hoạ và nội dung chưa có. Đặt tên theo cách người dùng hiểu; đừng giữ nguyên cấu trúc tổ chức nếu làm khó tìm nội dung.

Sitemap mô tả nơi nội dung nằm; user flow mô tả đường đi để hoàn thành tác vụ. Dự án nhỏ có thể dùng bảng luồng thay cho sơ đồ. Luồng cần có điểm bắt đầu/kết thúc và nhánh lỗi, quay lại, chưa đăng nhập, dữ liệu trống nếu liên quan.

Ví dụ: vào trang → chọn tuổi → chọn truyện có bản nghe → nghe/tạm dừng → kết thúc. Nhánh phim chưa xuất bản phải nói rõ trạng thái và đường thay thế, không có nút “Xem ngay” gây hiểu nhầm.

## Wireframe trước mức độ trang trí

- Vẽ lượng chi tiết vừa đủ cho quyết định: phân cấp, hành động chính, điều hướng, thông tin cần thiết.
- Dùng nhãn tiếng Việt và nội dung đủ thật để thấy chỗ dài; tránh mọi thẻ đều “Lorem ipsum”.
- Kiểm tra thứ tự nội dung ở mobile và khả năng tìm hành động chính; không thu nhỏ nguyên desktop.
- Khi cần so sánh, thay đổi một hướng cấu trúc có ý nghĩa, nêu tradeoff. Không tự sinh nhiều phương án nếu người dùng chỉ cần một bản.
- Thử giả thuyết rủi ro trên wireframe trước khi hoàn thiện UI nếu tác vụ cho phép.

Khi người dùng cần hình để thống nhất bố cục trước hi-fi, chuyển từ wireframe sang quy trình [ảnh layout tham chiếu và khóa hướng thị giác](visual-direction.md). Ảnh này minh họa quyết định cấu trúc; wireframe và UI cuối vẫn phải giữ lớp chỉnh sửa được.

Đầu ra `03-structure.md`: danh mục nội dung, cấu trúc mục, luồng tác vụ, wireframe và câu hỏi chưa giải quyết. Tiêu chí chuyển: đường đi chính rõ, các trạng thái ảnh hưởng tác vụ có chỗ xử lý, không còn thiếu quyết định cấu trúc khiến UI không thể dựng. “Đã review nội bộ” không đồng nghĩa “đã test người dùng”.
