# Thiết kế và kiểm tra responsive

Đọc tài liệu này khi đầu ra phải hoạt động trên mobile, tablet/iPad, laptop, desktop hoặc cửa sổ có thể đổi kích thước.

## Nguyên tắc

Thiết kế theo không gian khả dụng và nội dung, không theo tên thiết bị. Mobile/iPad/desktop là nhóm kiểm tra hữu ích; breakpoint phải được đặt tại điểm nội dung, điều hướng hoặc thao tác bắt đầu không còn dùng tốt. Giữ chức năng cốt lõi nhất quán khi reflow; màn rộng có thể lộ thêm thông tin thay vì thay đổi ý nghĩa tác vụ.

## Quy trình

1. **Chốt nội dung và ưu tiên.** Liệt kê vùng bắt buộc, hành động chính, thứ tự đọc, nội dung có thể trì hoãn và độ dài xấu nhất.
2. **Dựng khung nhỏ trước.** Bắt đầu ở độ rộng nhỏ liên quan, dùng một cột, kích thước linh hoạt và thứ tự semantic. Không thu nhỏ nguyên desktop.
3. **Kéo giãn liên tục.** Quan sát lúc dòng quá dài, card quá rộng/hẹp, nhãn wrap xấu, điều hướng chật, khoảng trắng mất cân đối hoặc ảnh mất chủ thể. Ghi đúng khoảng mà vấn đề xuất hiện.
4. **Thêm breakpoint theo sự cố.** Tại đó chọn hành vi: wrap, stack, đổi grid, đổi navigation, đổi số pane, ẩn/hiện thông tin phụ hoặc giới hạn container. Dùng token/min–max/fluid sizing trước khi thêm nhiều breakpoint.
5. **Đặc tả từng component.** Ghi min/max width, hug/fill/fixed, số cột, gap, thứ tự, vùng scroll, truncate/wrap, tỷ lệ/crop ảnh và trạng thái input/keyboard.
6. **Tạo màn đại diện.** Ít nhất một màn hẹp, một kích thước trung gian kiểu tablet/iPad và một màn rộng. Thêm portrait/landscape, split view hoặc cửa sổ hẹp nếu sản phẩm thực sự gặp các trạng thái đó.
7. **Kiểm tra giữa các mốc.** Resize theo bước liên tục, không chỉ chụp đúng ba frame. Thử zoom/reflow, font lớn, safe area, bàn phím ảo, con trỏ và touch khi liên quan.

## Ma trận responsive cần bàn giao

| Vùng/component | Khoảng rộng hoặc điều kiện | Layout | Thay đổi nội dung/navigation | Ảnh | Overflow | Ghi chú tương tác |
|---|---|---|---|---|---|---|
| Ví dụ: danh sách truyện | Khi card dưới min-width | 1 cột → 2/3 cột | Giữ thứ tự | 4:3, `cover`, giữ mặt nhân vật | Tiêu đề tối đa theo quyết định nội dung | Toàn card hoặc CTA có vùng bấm rõ |

Không ghi breakpoint chỉ bằng nhãn “mobile/tablet/desktop”. Ghi khoảng/điều kiện và lý do đổi layout. Nếu code dùng container query, đặc tả theo container của component; nếu dùng media query, đặc tả theo viewport.

## Bộ kiểm tra tối thiểu

Chọn theo dữ liệu thiết bị của sản phẩm khi có. Nếu chưa có, dùng bộ khám phá và ghi đây là đề xuất:

- hẹp: khoảng 320–390 CSS px;
- trung gian: khoảng 768–1024 CSS px, gồm portrait/landscape hoặc split view khi liên quan;
- rộng: khoảng 1280–1440 CSS px và một màn rộng hơn để kiểm max-width;
- mọi điểm ngay trước/sau breakpoint và các khoảng giữa chúng.

Tiêu chí hoàn tất: không có scroll ngang ngoài chủ đích; nội dung và focus không bị che/cắt; hành động chính còn tìm thấy; chữ và vùng bấm đạt yêu cầu dự án; ảnh giữ được chủ thể; layout không nhảy mất trạng thái; QA ghi viewport, DPR/zoom, trình duyệt hoặc thiết bị và bằng chứng.
