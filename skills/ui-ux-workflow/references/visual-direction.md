# Hướng thị giác và cổng khóa thương hiệu

Đọc tài liệu này khi cần tạo ảnh layout tham chiếu, moodboard/style tile hoặc chốt brand trước khi dựng UI hi-fi. Đây là phương án thiết kế cần duyệt, không phải kết quả nghiên cứu người dùng.

## 1. Chuẩn bị brief thị giác

Ghi mục tiêu màn hình, người xem, hành động chính, nội dung bắt buộc, cảm xúc cần truyền tải và các ràng buộc thương hiệu. Thu thập logo gốc, font có quyền sử dụng, bảng màu, ảnh hiện có, ví dụ được thích/không thích và kênh triển khai. Đánh dấu phần nào là tài sản chính thức, tham chiếu, giả thuyết hoặc còn thiếu.

## 2. Tạo ảnh layout tham chiếu

Ảnh layout tham chiếu dùng để chốt bố cục và nhịp thị giác trước hi-fi; không được dùng như lớp nền thay cho UI chỉnh sửa được.

1. Vẽ wireframe có nội dung đủ thật và chọn 1–3 đoạn quan trọng cần thể hiện: hero, danh sách/card và hành động chính.
2. Tạo một board có mục tiêu, 3–5 từ khóa, màu, chữ, ảnh, texture, icon và 1–3 composition tham chiếu. Ghi nguồn cạnh từng ảnh.
3. Tạo tối đa ba hướng khi quyết định còn mở. Mỗi hướng phải khác nhau ở một giả thuyết có ý nghĩa như mật độ, phân cấp hoặc cách dùng ảnh; không chỉ đổi màu.
4. Ghép một ảnh layout tham chiếu cho viewport chính bằng nội dung thật hoặc dữ liệu minh họa có nhãn. Chú thích grid, vùng ưu tiên, tỷ lệ ảnh, thứ tự đọc và phần sẽ reflow.
5. Review ở kích thước hiển thị thực. Ghi phần giữ lại, loại bỏ và lý do; chọn một hướng làm đầu vào cho brand lock.

Đầu ra tối thiểu: link/file board, ảnh export, viewport, nguồn từng tham chiếu, quyết định chọn hướng và phần chưa xác minh. Không cần ép số lượng ảnh cố định; board phải đủ cô đọng để người duyệt hiểu được hướng và đủ cụ thể để người thiết kế tái tạo.

## 3. Khóa brand guideline theo phạm vi

“Khóa” nghĩa là có một baseline được đặt phiên bản và người có thẩm quyền đã chấp nhận cho phạm vi hiện tại. Nó không làm guideline bất biến; thay đổi sau đó phải được ghi thành quyết định mới.

Chốt các nhóm sau:

| Nhóm | Cần ghi |
|---|---|
| Nền tảng | Tính cách, từ khóa nên/không nên, đối tượng, bối cảnh sử dụng |
| Logo | File gốc, biến thể, khoảng trống, kích thước tối thiểu, nền được phép, điều cấm |
| Màu | Base token, semantic token, cặp nền/chữ, trạng thái và kết quả tương phản |
| Chữ | Font và quyền sử dụng, role, weight, scale, line-height, fallback, quy tắc tiếng Việt |
| Bố cục | Grid, container, spacing, radius, elevation, mật độ, nguyên tắc responsive |
| Hình ảnh | Chủ đề, chủ thể, ánh sáng, màu, góc máy/minh họa, crop, điều nên tránh |
| UI | Component lõi, icon, trạng thái, focus, motion và reduced-motion |
| Nội dung | Giọng điệu, cách gọi hành động, viết hoa, số/ngày, từ bị cấm nếu có |
| Quản trị | Owner, người duyệt, version, ngày khóa, phạm vi, nơi lưu và quy trình thay đổi |

## 4. Cổng duyệt trước hi-fi

Chỉ coi baseline đã khóa khi:

- nguồn logo, font và hình có thể truy vết; quyền sử dụng đã biết hoặc được ghi là blocker;
- token lõi và semantic mapping đủ cho màn hình trong phạm vi;
- cặp màu quan trọng đã đo tương phản, không suy từ việc nhìn bằng mắt;
- ảnh layout tham chiếu có thể tái tạo bằng grid/component, không phụ thuộc một ảnh nền UI;
- quy tắc hình ảnh và responsive đã có ví dụ chấp nhận/không chấp nhận;
- người duyệt, phiên bản và quyết định được ghi trong `04-design.md` và `08-decisions.md`.

Nếu chưa đạt, vẫn có thể dựng phương án để khám phá nhưng phải ghi `proposed`; không gọi là brand đã khóa.
