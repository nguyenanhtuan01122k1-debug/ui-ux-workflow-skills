# Chất lượng: tiếp cận, mobile và tiếng Việt

Đây là checklist thực hành theo phạm vi, không phải chứng nhận WCAG. Tài liệu W3C hiện hành là nguồn quyết định cho tiêu chí, mức và ngoại lệ.

## Tiếp cận

| Hạng mục | Kiểm tra thiết kế | Kiểm tra bản triển khai |
|---|---|---|
| Tương phản chữ | Chữ thường tối thiểu 4.5:1; chữ lớn theo định nghĩa WCAG tối thiểu 3:1, xét ngoại lệ | Đo màu hiển thị thực, kể cả ảnh nền/gradient |
| Thông tin bằng màu | Có nhãn/icon bổ trợ cho lỗi, selected, trạng thái | Screen reader nhận được tên/trạng thái |
| Bàn phím/focus | Thiết kế trạng thái focus và thứ tự hợp lý | Thao tác Tab/Enter/Space/Escape theo control; tránh trap |
| Focus bị che | Sticky bar/modal không che hoàn toàn phần tử đang focus | Thử scroll và focus ở các viewport |
| Vùng bấm | Xét WCAG 2.2 SC 2.5.8: 24×24 CSS px hoặc đáp ứng ngoại lệ | Đo hit area và khoảng cách thực, không chỉ icon |
| Form/lỗi | Nhãn rõ, lỗi nói cách khắc phục, giữ dữ liệu hợp lý | Semantic label, error association và thông báo trạng thái |
| Reflow/zoom | Nội dung có thể wrap và tái bố trí | Thử zoom và viewport hẹp; xét ngoại lệ nội dung hai chiều |
| Motion | Mục đích rõ, tránh nhấp nháy; có phương án giảm chuyển động | Kiểm tra cài đặt reduced-motion và khả năng dừng nếu liên quan |

24px là ngưỡng của một tiêu chí tối thiểu, không phải mặc định tối ưu cho trẻ. Có thể đề xuất control khoảng 44–48px cho thao tác chạm trong dự án này, ghi đó là quyết định thiết kế cần kiểm tra, không đồng nhất với mức AA.

## Mobile và tiếng Việt

- Làm theo [quy trình responsive](responsive.md): kiểm tra tối thiểu một viewport hẹp, một khoảng trung gian kiểu tablet/iPad, một viewport rộng, mọi điểm ngay trước/sau breakpoint và các khoảng giữa. Độ rộng cụ thể là lựa chọn dự án dựa trên nội dung và dữ liệu thiết bị khi có.
- Thử tên truyện dài, chữ có nhiều dấu, nội dung hai dòng, nhãn dài, mất hình và danh sách rỗng. Không bỏ dấu để vừa ô, không thu font đến mức khó đọc.
- Nêu cách xử lý overflow: wrap, scroll có chủ đích hay rút gọn có cách xem đầy đủ. Bảo đảm hành động chính vẫn thấy được.
- Kiểm tra mobile navigation không che nội dung, hỗ trợ safe area và bàn phím ảo khi có input. Body text và vùng bấm phải phù hợp đối tượng.
- Với UI Văn Minh Việt, giữ phân cấp cỡ/độ đậm trên font Be Vietnam Pro theo token cập nhật; không tự dùng lại serif từ mẫu cũ. Không dùng nền giấy hoặc màu đồng làm giảm tương phản.

Ghi “đã kiểm tra” kèm viewport, thiết bị/công cụ và kết quả. Không suy ra kiểm tra screen reader hay tiêu chuẩn đầy đủ từ việc xem file Figma.
