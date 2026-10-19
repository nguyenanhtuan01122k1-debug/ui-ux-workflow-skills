# Tìm kiếm, chọn và bàn giao hình ảnh

Đọc tài liệu này khi layout cần ảnh chụp, minh họa, texture hoặc ảnh hero/card. Tìm thấy ảnh đẹp chưa đồng nghĩa được phép dùng.

## 1. Viết brief cho từng ô ảnh

Trước khi tìm, ghi:

- mục đích trong luồng và thông điệp cần hỗ trợ;
- chủ thể, hành động, bối cảnh, cảm xúc, ánh sáng và bảng màu;
- đối tượng cần đại diện và điều cần tránh;
- tỷ lệ ở từng layout, vùng an toàn cho chữ/CTA, điểm neo crop và độ phân giải tối thiểu;
- ảnh mang thông tin hay chỉ trang trí;
- nguồn được phép, ngân sách và yêu cầu model/property release nếu có.

Biến brief thành chuỗi tìm kiếm cụ thể theo cấu trúc `chủ thể + hành động + bối cảnh + phong cách/ánh sáng + bố cục`. Tìm bằng tiếng Việt và tiếng Anh khi giúp mở rộng nguồn; không đưa tên riêng hoặc dữ liệu nhạy cảm vào truy vấn.

## 2. Thu thập và shortlist

1. Tìm ở nguồn chính thức của thương hiệu trước, sau đó thư viện đã mua/được duyệt, stock có giấy phép rõ, cuối cùng mới dùng ảnh tham chiếu không có quyền để định hướng.
2. Lưu URL trang tài sản, tác giả, nền tảng, loại giấy phép, ngày truy cập, yêu cầu attribution, hạn chế, release và file gốc. Lưu trang nguồn thay vì chỉ URL CDN.
3. Loại ảnh không chịu được crop, không có độ phân giải đủ, sai tone/đại diện, có logo/nhân vật rủi ro hoặc không xác minh được quyền.
4. Chấm shortlist theo mức phù hợp nội dung, brand, composition, khả năng responsive, tính nhất quán bộ ảnh, quyền và hiệu năng. Không dùng độ “đẹp” làm tiêu chí duy nhất.
5. Đặt ảnh vào layout thật với chữ thật trước khi chọn. Thử crop ở mọi tỷ lệ đã định và đánh dấu focal point/safe area.

## 3. Responsive image và art direction

- Nếu cùng một bố cục chỉ cần độ phân giải khác nhau, bàn giao các kích thước nguồn để dev dùng `srcset`/`sizes` hoặc cơ chế tương đương.
- Nếu màn hẹp cần crop hay composition khác để giữ chủ thể, chuẩn bị biến thể art direction và mô tả điều kiện chọn; trên web có thể dùng `<picture>`.
- Giữ `width`/`height` hoặc aspect-ratio để dành chỗ, tránh nhảy layout. Không tải ảnh desktop rất lớn rồi chỉ thu nhỏ bằng CSS.
- Nêu format/chất lượng mong đợi, giới hạn dung lượng nếu dự án có performance budget và ảnh fallback.

## 4. Alt text và nội dung trong ảnh

Phân loại theo mục đích, không theo hình dáng. Ảnh cung cấp thông tin cần text alternative truyền cùng ý nghĩa trong ngữ cảnh; ảnh trang trí dùng alt rỗng hoặc cơ chế tương đương; ảnh là control phải có tên mô tả hành động. Tránh nhúng chữ quan trọng vào ảnh. Khi crop/art direction làm đổi thông tin nhìn thấy, kiểm lại alt text.

## 5. Bảng tài sản bàn giao

| ID/slot | Preview | URL nguồn/tác giả | License/release | Mục đích/alt | Tỷ lệ & focal point | Biến thể/kích thước | Trạng thái |
|---|---|---|---|---|---|---|---|

Trạng thái nên phân biệt `reference-only`, `candidate`, `license-checked`, `approved`, `rejected`, `missing`. Unsplash và Pexels cho phép nhiều cách dùng miễn phí theo trang giấy phép của họ nhưng vẫn có hạn chế; luôn lưu bằng chứng tại thời điểm chọn và xét thương hiệu, người nhận diện được, tác phẩm, tài sản và luật áp dụng. Skill không đưa ra kết luận pháp lý thay cho chủ sở hữu dự án.
