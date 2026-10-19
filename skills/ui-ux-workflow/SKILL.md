---
name: ui-ux-workflow
description: Điều phối quy trình UI/UX cho website và ứng dụng, từ nghiên cứu người dùng, xác định bài toán, cấu trúc nội dung và wireframe đến UI, prototype, kiểm thử, bàn giao và đo lường. Dùng cho dự án thiết kế mới, redesign hoặc một giai đoạn cụ thể; tích hợp Tavily và Figma khi có công cụ. Không áp dụng cho tác vụ ảnh đơn lẻ hoặc sửa code không liên quan đến trải nghiệm.
---

# Quy trình UI/UX

Giúp người dùng đưa ra quyết định thiết kế có căn cứ và có thể triển khai. Trả lời bằng ngôn ngữ của người dùng; mặc định dùng tiếng Việt khi chưa có yêu cầu khác.

## Bắt đầu từ yêu cầu thực tế

1. Đọc sản phẩm/tài liệu được cung cấp, tài sản thương hiệu, dữ liệu nghiên cứu, thiết kế và trạng thái hiện có. Với URL chưa truy cập được, báo đúng lỗi, dùng nguồn hiện có và ghi phần chưa xác minh; không nói đã xem trang.
2. Chốt phạm vi bằng một cập nhật ngắn: đối tượng, tác vụ ưu tiên, loại đầu ra, phần nào kiểm chứng được. Hỏi khi thiếu dữ liệu thật sự ảnh hưởng quyết định; phần độc lập vẫn làm tiếp.
3. Chọn chế độ dưới đây. Không biến yêu cầu UI đơn lẻ thành dự án nghiên cứu nhiều tuần. Không lấy thiếu nghiên cứu làm lý do ngừng dựng phương án đã được yêu cầu.
4. Dùng hồ sơ dự án hiện có. Khi cần quản lý nhiều giai đoạn, chạy [scripts/new_project.py](scripts/new_project.py) để copy [assets/project](assets/project) tới đích người dùng chọn hoặc thư mục làm việc của tác vụ. Không viết dữ liệu dự án vào skill đã cài.
5. Với thiết kế Văn Minh Việt, đọc [style-van-minh-viet.md](references/style-van-minh-viet.md) trước khi chọn font, màu và kích thước thành phần. Bộ Base/Alias đính kèm là nguồn ưu tiên cho giá trị đã có; không dùng lại giá trị khác từ phương án cũ. Với thương hiệu khác, tiếp tục dùng tài sản của thương hiệu đó.

| Chế độ | Khi dùng | Đầu ra tối thiểu |
|---|---|---|
| Toàn quy trình | Xây mới/redesign có phạm vi rộng | Brief, bằng chứng, luồng, thiết kế, test, bàn giao và kế hoạch đo; giai đoạn chưa thực hiện phải ghi rõ |
| Nghiên cứu | Research, tìm nguồn, phỏng vấn, đánh giá hiện trạng | Câu hỏi nghiên cứu, nguồn/bằng chứng, kết luận và khoảng trống |
| Phương án nhanh | Người dùng cần UI/wireframe ngay | Giả thuyết, luồng liên quan, phương án thiết kế, giới hạn và bước kiểm thử tiếp |
| Kiểm thử/review | Đánh giá prototype hay sản phẩm | Tác vụ, phát hiện có bằng chứng, mức ảnh hưởng, đề xuất và kiểm tra lại |
| Bàn giao/đo lường | Thiết kế đã có | Trạng thái, hành vi, responsive, QA hoặc định nghĩa phép đo |

## Quy tắc bằng chứng

- Gắn loại cho phát biểu quan trọng: **quan sát**, **người dùng báo cáo**, **dữ liệu định lượng**, **nguồn thứ cấp**, **giả thuyết**, hoặc **đề xuất**. Tài liệu hướng dẫn có thẩm quyền vẫn không phải bằng chứng về hành vi của khách hàng cụ thể.
- Nối kết luận với mã bằng chứng, nhóm người dùng, hoàn cảnh và ngày. Ghi ý kiến trái chiều, giới hạn mẫu và điều chưa biết. Không dựng persona, lời phỏng vấn, số liệu hay kết quả test như dữ liệu thật.
- Nghiên cứu qua web không thay thế nghiên cứu người dùng. Thẩm định chuyên gia không phải usability test. Prototype chạy được không đồng nghĩa UX đã xác nhận.
- Mẫu định tính nhỏ dùng để tìm vấn đề, không suy ra tỷ lệ của toàn bộ khách hàng hay gộp mọi nhóm tuổi thành một mẫu đại diện.
- Chỉ ghi “đã kiểm chứng” cho giả thuyết/tác vụ đã được thử, nêu phương pháp và phạm vi. Thiếu bằng chứng thì giao phương án cùng kế hoạch kiểm chứng.

## Đọc tài liệu theo giai đoạn

Chỉ đọc phần liên quan, không tải tất cả vào mỗi tác vụ.

| Việc đang làm | Đọc | Hồ sơ đầu ra |
|---|---|---|
| Mục tiêu, phạm vi, hiện trạng | [01-discovery.md](references/01-discovery.md) | `00-brief.md`, `01-research.md` |
| Chọn vấn đề, giả thuyết, ưu tiên | [02-define.md](references/02-define.md) | `02-problem.md` |
| Nội dung, luồng và wireframe | [03-structure.md](references/03-structure.md) | `03-structure.md` |
| UI, token, component và responsive | [04-ui.md](references/04-ui.md) | `04-design.md` |
| Tạo ảnh layout tham chiếu, moodboard, khóa brand | [visual-direction.md](references/visual-direction.md) | Board/ảnh tham chiếu, brand baseline và quyết định trong `04-design.md` |
| Responsive mobile, tablet/iPad, desktop | [responsive.md](references/responsive.md) | Ma trận reflow và bằng chứng QA trong `04-design.md`, `06-handoff.md` |
| Tìm, chọn, crop và bàn giao ảnh | [imagery.md](references/imagery.md) | Bảng nguồn/quyền, art direction và alt text trong `04-design.md` |
| Thiết kế theo style Văn Minh Việt | [style-van-minh-viet.md](references/style-van-minh-viet.md) | Ánh xạ token và ngoại lệ có lý do trong `04-design.md` |
| Prototype, test, sửa và thử lại | [05-test.md](references/05-test.md) | `05-test.md` |
| Bàn giao Figma, triển khai và QA | [06-handoff.md](references/06-handoff.md) | `06-handoff.md` |
| Chỉ số và cải tiến sau ra mắt | [07-measure.md](references/07-measure.md) | `07-measure.md` |
| Nghiên cứu bằng Tavily | [tavily.md](references/tavily.md) | Nhật ký nguồn trong hồ sơ nghiên cứu |
| Đọc/ghi Figma | [figma.md](references/figma.md) | Link file/node, trạng thái và hình kiểm tra |
| Tiếp cận, mobile, tiếng Việt | [quality.md](references/quality.md) | Kết quả kiểm tra, phạm vi và lỗi còn lại |
| Nguồn chuyên môn | [sources.md](references/sources.md) | Trích dẫn gần kết luận liên quan |

## Điều phối và dừng đúng lúc

Luồng tham chiếu: khám phá → xác định → cấu trúc/wireframe → UI/prototype → kiểm thử → bàn giao/QA → đo lường. Quay lại giai đoạn gây ra vấn đề, không sửa màu để chữa một luồng thao tác sai. Kiểm thử wireframe có thể diễn ra trước UI; đo lường phải được định nghĩa trước khi ra mắt.

Trong `project.json`, ghi giai đoạn hiện tại, đầu ra, trạng thái `not_started`, `in_progress`, `proposed`, `validated` hoặc `not_in_scope`. Trạng thái do người thực hiện cập nhật từ bằng chứng; script không tự đánh dấu hoàn thành. `validated` chỉ là giai đoạn đạt tiêu chí đã ghi, không chứng nhận toàn sản phẩm. Cập nhật `08-decisions.md` cho quyết định quan trọng và lý do.

Với dự án đang dở, tiếp tục từ tài liệu và dữ liệu hiện có, không bắt đầu lại. Khi có xung đột, ưu tiên yêu cầu hiện tại và bằng chứng liên quan; nêu tradeoff rõ ràng.

Kết thúc khi đầu ra trong phạm vi đã tạo và được kiểm tra phù hợp. Bàn giao ngắn: thay đổi, bằng chứng, giới hạn, link tài sản và bước tiếp theo. Không tự xuất bản, mời người tham gia, nhắn tin, cài công cụ hay thay đổi chia sẻ chỉ vì quy trình có các bước đó.
