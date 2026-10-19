# Ví dụ áp dụng · Làng Hoạt Hình Việt

Đây là **brief và kế hoạch mẫu**, không phải báo cáo nghiên cứu. Không có transcript, analytics hay kết quả thử với trẻ/phụ huynh đi kèm repo.

## Bối cảnh có sẵn trong cuộc trao đổi

Trang Hoạt hình của Văn Minh Việt có bộ lọc tuổi Mầm 3–5, Chồi 6–8, Lá 9–12; phim đang vẽ/sắp có; truyện kể; học chữ Hán Nôm; tô màu; trò chơi; đồng dao; Hộ chiếu nhí và góc phụ huynh. Cần xem lại trang hiện tại khi bắt đầu dự án vì nội dung có thể thay đổi.

Style cập nhật theo [Base/Alias](../skills/ui-ux-workflow/references/style-van-minh-viet.md): đỏ chính #A11414, đồng #A87437; Be Vietnam Pro cho cả tiêu đề và thân. Bố cục giữ tinh thần giấy kem và nét đồng tiết chế. Hai phương án Figma trước là ý tưởng thị giác, không là bằng chứng UX; font/màu ở đó không được ưu tiên hơn export mới.

## Phạm vi đề xuất

- Ưu tiên: tìm bản kể chuyện phù hợp tuổi; nhận biết phim chưa xuất bản; phụ huynh tìm quản lý hồ sơ và hẹn giờ.
- Ngoài phạm vi ban đầu: sản xuất phim, thiết kế toàn nền tảng, triển khai backend, tuyển người tham gia tự động.
- Người dùng: các nhóm tuổi nêu trên và phụ huynh; cần nghiên cứu để biết khác biệt hành vi, chưa tạo persona khẳng định.

## Chuỗi giả thuyết → thử nghiệm

| Mã | Giả thuyết chưa kiểm chứng | Thử bằng tác vụ | Quan sát cần ghi |
|---|---|---|---|
| H-01 | Lựa chọn tuổi rõ hơn có thể giúp tìm truyện phù hợp | “Tìm truyện để nghe cùng bé 5 tuổi” | Chọn tuổi, nội dung tìm được, nhầm lẫn, trợ giúp |
| H-02 | Phân biệt phim đang sản xuất và bản nghe có sẵn có thể giảm bấm nhầm | “Bạn muốn xem một phim đã có; nếu chưa có thì tìm cách nghe truyện” | Hiểu trạng thái và tìm được hành động khả dụng |
| H-03 | Góc phụ huynh có tên rõ có thể giúp tìm công cụ quản lý | “Bạn muốn giới hạn một lần xem của bé trong 15 phút” | Tìm đúng nơi, hiểu trạng thái hẹn giờ và cách tắt |

Các nhãn trên là đề xuất thử, không là mô tả hành vi đã quan sát. Với phiên thử trẻ, điều chỉnh lời giao tác vụ theo độ tuổi; không dùng kịch bản của phụ huynh nguyên xi cho trẻ 3 tuổi.

## Cách triển khai

1. Tạo hồ sơ bằng `new_project.py`, điền brief và kiểm kê nội dung thật.
2. Dùng Tavily để đối chiếu phương pháp với nguồn gốc. Không tìm web để thay thế bằng chứng về người dùng trang này.
3. Nghiên cứu định tính phù hợp; nếu chưa tổ chức được, giao wireframe như phương án giả thuyết.
4. Dựng luồng nghe và luồng phụ huynh. Dùng style skill Văn Minh Việt nếu có; kiểm tra file phụ trước khi nói đã dùng.
5. Tạo UI editable trong Figma, thử mobile 375px và desktop, chữ dài và trạng thái phim.
6. Test, sửa, thử lại theo phạm vi. Sau đó bàn giao và định nghĩa event không chứa dữ liệu riêng của trẻ.

Chỉ số đề xuất: hoàn thành tìm/phát truyện; hiểu đúng trạng thái phim; hoàn thành đặt/tắt hẹn giờ. Baseline, ngưỡng và kết quả hiện **chưa có**.
