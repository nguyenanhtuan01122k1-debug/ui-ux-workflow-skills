# 07 · Đo lường và cải tiến

Định nghĩa phép đo từ lúc chốt vấn đề. Sau ra mắt, so với baseline bằng dữ liệu có cùng định nghĩa và bối cảnh; phân biệt tác động của thiết kế với mùa vụ, nội dung mới, nguồn truy cập hay thay đổi logging.

## Mỗi chỉ số cần có

Mục tiêu người dùng; tử số; mẫu số; event bắt đầu/kết thúc; cửa sổ thời gian; đơn vị phân tích (người/phiên/tác vụ); tiêu chí loại; phân đoạn; baseline; mục tiêu do nhóm đặt; nguồn và người phụ trách. Nếu thiếu baseline, ghi kế hoạch thu, không tạo số.

Ví dụ đề xuất M-01: tỷ lệ phiên bắt đầu chọn truyện rồi phát được bản nghe. Phải định nghĩa “phát được” (ví dụ event phát thành công từ player), không coi một click là nghe thành công. Ngưỡng thời gian, cách loại lỗi và cửa sổ đo do dự án xác định.

## Chọn chỉ số phản ánh giá trị

- Hoàn thành tác vụ, số lỗi, nhu cầu trợ giúp và tìm đúng nội dung có thể hữu ích hơn tổng lượt click.
- Với sản phẩm trẻ em, không mặc định tăng thời gian màn hình là thành công. Đề xuất đo tìm nội dung phù hợp, độ rõ trạng thái, khả năng dừng/nghỉ và mức an tâm của phụ huynh.
- Không gửi tên trẻ, năm sinh chính xác, nội dung riêng hay bản ghi nghiên cứu vào event analytics chỉ để có phân đoạn. Thiết kế phép đo tối thiểu theo nhu cầu và quy tắc dữ liệu của dự án.
- Chỉ dùng A/B test khi có đủ lưu lượng, thiết kế thử nghiệm và phép đo phù hợp; không chọn người thắng từ vài lượt bấm hoặc peek liên tục.

Đầu ra `07-measure.md`: định nghĩa event/chỉ số, baseline, kết quả thực tế khi có, yếu tố nhiễu, quyết định giữ/sửa/thử tiếp. Không ghi kế hoạch đo là bằng chứng sản phẩm đã cải thiện.
