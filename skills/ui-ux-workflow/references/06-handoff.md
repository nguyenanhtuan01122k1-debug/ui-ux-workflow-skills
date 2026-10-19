# 06 · Bàn giao và QA bản dựng

Hợp tác với phát triển từ sớm khi quyết định ảnh hưởng dữ liệu, API hay chi phí triển khai. Bàn giao phải đủ để lập trình viên hiểu hành vi, không chỉ đo được khoảng cách.

## Gói bàn giao theo phạm vi

- Màn hình nguồn và luồng prototype, chỉ rõ phiên bản được triển khai.
- Token/style/component, font và asset được phép sử dụng; tên và định dạng xuất.
- Hành động và trạng thái tương ứng: loading, empty, error, selected, disabled khi có.
- Responsive: thứ tự, wrap, sticky, overflow, kích thước tối thiểu/tối đa và điểm thay đổi theo nội dung.
- Nội dung thật, nhãn trạng thái, quy tắc rút gọn và trường hợp nội dung chưa có.
- Tiếp cận: semantic control, tên truy cập, thứ tự focus, thông báo lỗi, hành vi bàn phím.
- Định nghĩa event cần đo, giới hạn thu dữ liệu và trách nhiệm triển khai.
- Quyết định còn mở, người phụ trách và tiêu chí nghiệm thu.

Trong Figma, trạng thái Ready for dev là tín hiệu tài sản sẵn sàng cho lập trình viên xem/triển khai; không có nghĩa code đã hoàn thành, UX đã kiểm chứng hoặc đã đạt WCAG. Chỉ dùng khi công cụ và quyền hiện có hỗ trợ.

## Kiểm tra bản dựng

So ở cùng viewport và dữ liệu: bố cục, font, nội dung, hình, tương phản. Sau đó thử tác vụ thật trên trình duyệt: touch/keyboard, lỗi mạng, tải chậm, back, refresh, zoom và các thiết bị trong phạm vi. Kiểm tra riêng hành vi khó thấy trên ảnh như focus bị sticky header che, chuyển trang mất bộ lọc và nút disabled vẫn bấm được.

Ghi mỗi lỗi với bước tái hiện, mong đợi, thực tế, ảnh/video nếu cần, thiết bị và mức ảnh hưởng. Phân biệt design QA, kiểm thử chức năng và audit tiếp cận; không thay thế nhau.

Đầu ra `06-handoff.md`. Hoàn thành khi tài sản và hành vi đủ rõ, lỗi chặn trong phạm vi đã sửa hoặc được ghi là giới hạn chưa giải quyết. Không đánh dấu release thành công khi chưa xác minh sản phẩm thực tế.
