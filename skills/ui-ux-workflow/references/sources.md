# Nguồn và phạm vi diễn giải

Các nguồn dưới được tra cứu qua Tavily trong cuộc trao đổi xây dựng repo ngày 19/10/2026. Lần tra cứu chủ yếu dùng nội dung kết quả tìm kiếm; không khẳng định đã đọc toàn bộ mọi tài liệu. Hướng dẫn repo là tổng hợp thực hành, không phải quy trình chính thức chung của các tổ chức này. Khi dùng cho quyết định mới, kiểm tra lại nội dung/phiên bản liên quan.

| Nguồn gốc | Nhận định được sử dụng | Giới hạn |
|---|---|---|
| [Design Council — Double Diamond](https://www.designcouncil.org.uk/resources/the-double-diamond) | Discover, Define, Develop, Deliver; khám phá rộng và thu hẹp quyết định | Không quy định mọi dự án phải có đúng 8 tài liệu hay cùng thời lượng |
| [Design Council — Framework for Innovation](https://www.designcouncil.org.uk/resources/framework-for-innovation) | Lấy người bị ảnh hưởng làm trung tâm, thử và cải thiện giải pháp | Không phải bằng chứng người dùng của dự án |
| [NN/g — Usability Testing 101](https://www.nngroup.com/articles/usability-testing-101/) | Quan sát tác vụ thực tế; khuyến nghị 5 người cho vòng định tính điển hình một nhóm | Không dùng làm cỡ mẫu định lượng hay kết luận đại diện nhiều nhóm |
| [GOV.UK — Alpha](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works) | Kiểm tra giả định rủi ro và cân nhắc trước khi triển khai tiếp | Quy trình dịch vụ công UK, không áp nguyên ngân sách/thời lượng cho website nhỏ |
| [GOV.UK — Measuring completion rate](https://www.gov.uk/service-manual/measuring-success/measuring-completion-rate) | Định nghĩa lượt bắt đầu/kết thúc và đo hoàn thành | “Hoàn thành” của từng sản phẩm cần được định nghĩa riêng |
| [GOV.UK — Measuring service benefits](https://www.gov.uk/service-manual/measuring-success/measuring-service-benefits) | Có baseline để đánh giá cải thiện | Kết quả so sánh có thể chịu yếu tố nhiễu |
| [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Tiêu chí tiếp cận, gồm vùng bấm tối thiểu và focus không bị che | Đọc mức/định nghĩa/ngoại lệ đầy đủ; checklist repo không là audit |
| [W3C — Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) | Tra tiêu chí và kỹ thuật đáp ứng | Kỹ thuật là cách hỗ trợ, không thay tiêu chí chuẩn |
| [Figma — Ready for dev view](https://help.figma.com/hc/en-us/articles/23918228264855-Dev-Mode-ready-for-dev-view) | Tín hiệu thiết kế sẵn sàng cho phát triển | Phụ thuộc quyền/tính năng; không chứng minh code hoặc UX hoàn tất |
| [Figma — How to make a mood board](https://www.figma.com/resource-library/how-to-make-a-mood-board) | Xác định mục tiêu, tập hợp và chú thích tham chiếu, cộng tác sớm để thống nhất hướng | Moodboard giúp căn chỉnh hướng; không tự chứng minh hướng đó phù hợp người dùng |
| [Figma — Design system governance](https://www.figma.com/resource-library/design-system-governance) | Ghi rõ ai sở hữu, ai duyệt và cách truyền đạt thay đổi của design system | Repo áp dụng thành brand lock theo phạm vi; không gán một mô hình quản trị duy nhất cho mọi đội |
| [MDN — Media query fundamentals](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Media_queries) | Đặt breakpoint khi nội dung/layout cần đổi thay vì nhắm từng model thiết bị; kiểm bằng resize | Khoảng kiểm tra trong repo là đề xuất, không phải breakpoint chuẩn của MDN |
| [MDN — Responsive design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design) | Grid/ảnh linh hoạt và media query; ảnh quá lớn thu nhỏ gây tốn băng thông | Cần phối hợp với yêu cầu sản phẩm và hiệu năng thực tế |
| [Apple HIG — Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | Với app Apple, quyết định layout theo không gian/size class thay vì loại thiết bị hoặc orientation | Chi tiết nền tảng Apple; nguyên tắc không gian khả dụng được repo dùng làm tham chiếu, không áp API Apple cho web |
| [MDN — Responsive images](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images) | Phân biệt resolution switching và art direction; dùng nguồn phù hợp thay vì tải ảnh desktop cho mobile | Cách triển khai cụ thể phụ thuộc stack và pipeline ảnh |
| [W3C WAI — Alt decision tree](https://www.w3.org/WAI/tutorials/images/decision-tree/) | Chọn text alternative theo mục đích/ngữ cảnh của ảnh | Cần đọc tutorial liên quan cho ảnh phức tạp; bảng tài sản không thay audit |
| [Unsplash License](https://unsplash.com/license) | Cho phép nhiều cách dùng miễn phí, kể cả thương mại, với các hạn chế được nêu | Không suy ra mọi quyền về người, nhãn hiệu, tác phẩm hay tài sản trong ảnh |
| [Pexels License](https://www.pexels.com/license/) | Cho phép tải, sửa và dùng ảnh/video miễn phí; có các hạn chế về bán bản không sửa, endorsement và phân phối lại | Luôn kiểm trang giấy phép và asset tại thời điểm chọn; không là tư vấn pháp lý |

Các đề xuất như hồ sơ E/P/H/T/M, chia 8 giai đoạn, cách bố trí tài liệu, lựa chọn kích thước viewport và áp dụng cho Văn Minh Việt là **tổng hợp của repo**. Không gán chúng cho nguồn nếu nguồn không nói vậy.

Repo không kèm nội dung sao chép toàn văn, font, hình thương hiệu hoặc skill bên thứ ba. Khi thêm tài sản vào một dự án, quản lý nguồn và quyền sử dụng riêng.
