# UI/UX Workflow Skills

Repo skill tiếng Việt để điều phối một dự án UI/UX từ nghiên cứu đến đo lường sau ra mắt. Dùng cho website, ứng dụng và thiết kế lại sản phẩm; có nhánh làm việc trực tiếp trong Figma và nghiên cứu qua Tavily khi các công cụ đó được kết nối.

Skill chính: **`ui-ux-workflow`**. Không yêu cầu Tavily hoặc Figma để đọc hướng dẫn, tạo hồ sơ dự án hoặc phác thảo phương án. Muốn đọc dữ liệu bên ngoài hay chỉnh Figma cần công cụ và quyền tương ứng.

Đã kèm [quy định style Văn Minh Việt](skills/ui-ux-workflow/references/style-van-minh-viet.md) và hai bộ token Base/Alias người dùng cung cấp. Với dự án Văn Minh Việt, các token này ưu tiên hơn màu/font trong ví dụ cũ: đỏ #A11414, đồng #A87437, Be Vietnam Pro cho tiêu đề và thân. Giữ file export nguyên bản và mô tả rõ phần mapping được đề xuất thêm.

## Cài đặt

Copy thư mục `skills/ui-ux-workflow` vào thư mục skills của môi trường đang dùng. Với Codex, đặt tại `$CODEX_HOME/skills/ui-ux-workflow`; nếu không cấu hình `CODEX_HOME`, dùng `~/.codex/skills/ui-ux-workflow`. Mở phiên mới nếu skill chưa xuất hiện. Repo này chưa tự cài vào tài khoản và chưa được đẩy lên GitHub.

Ví dụ PowerShell, chạy ở thư mục repo, đích cài phải chưa tồn tại:

```powershell
$skillRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $env:USERPROFILE '.codex/skills' }
$skillTarget = Join-Path $skillRoot 'ui-ux-workflow'
if (Test-Path -LiteralPath $skillTarget) { throw 'Skill đã tồn tại; hãy so sánh trước khi cập nhật.' }
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath './skills/ui-ux-workflow' -Destination $skillTarget -Recurse
```

## Gọi skill

```text
Dùng $ui-ux-workflow để thiết kế lại trang của tôi.
Đọc dữ liệu hiện có, chọn phạm vi phù hợp và ghi riêng bằng chứng với giả thuyết.
Nếu có Tavily, nghiên cứu nguồn gốc; nếu có Figma, tạo các lớp chỉnh sửa được.
```

Các yêu cầu hẹp cũng được hỗ trợ:

- “Dùng $ui-ux-workflow lập kế hoạch nghiên cứu và kịch bản phỏng vấn.”
- “Dùng $ui-ux-workflow kiểm thử luồng chọn truyện và hẹn giờ xem.”
- “Dùng $ui-ux-workflow chuẩn bị bàn giao bộ màn hình hiện tại.”
- “Dùng $ui-ux-workflow thiết kế UI theo style Văn Minh Việt; chưa có dữ liệu người dùng.”

Trong trường hợp cuối, đầu ra được ghi là **phương án đề xuất**, không phải UX đã kiểm chứng. Skill không bắt buộc làm toàn bộ quy trình cho một chỉnh sửa nhỏ.

## Nội dung repo

```text
skills/ui-ux-workflow/
  SKILL.md                 Điều phối, chọn chế độ, quy tắc bằng chứng
  agents/openai.yaml       Metadata để tìm và gọi skill
  references/              Hướng dẫn từng giai đoạn, layout/brand, responsive, hình ảnh, Tavily, Figma, tiếp cận
  assets/project/          Mẫu hồ sơ dự án từ brief đến kết quả đo lường
  assets/tokens/           Hai bộ token gốc Base và Alias Văn Minh Việt
  scripts/new_project.py   Tạo hồ sơ dự án, từ chối ghi đè
  scripts/check_tokens.py  Kiểm tra dữ liệu, target alias và giá trị resolve
examples/van-minh-viet.md   Bài toán mẫu; chưa có nghiên cứu người dùng
scripts/check_repo.py      Kiểm tra cấu trúc, liên kết nội bộ và metadata
tests/test_new_project.py  Kiểm tra công cụ tạo hồ sơ
```

## Khởi tạo một dự án

Cần Python 3.10 trở lên, chỉ dùng thư viện chuẩn:

```powershell
python skills/ui-ux-workflow/scripts/new_project.py --name "Làng Hoạt Hình Việt" --output ./projects/lang-hoat-hinh
```

Kết quả có 9 tài liệu làm việc và `project.json`. Các mục chưa thực hiện để trống hoặc đánh dấu chưa có dữ liệu; không tự sinh “insight”, người tham gia hay kết quả kiểm thử. Dự án nằm ngoài thư mục skill để không làm thay đổi mẫu gốc.

## Kiểm tra repo

```powershell
python scripts/check_repo.py
python skills/ui-ux-workflow/scripts/check_tokens.py
python -m unittest discover -s tests -v
```

Nếu có skill-creator trong môi trường, chạy thêm `quick_validate.py` của môi trường đó với `skills/ui-ux-workflow`. Kiểm tra tự động chỉ xác nhận cấu trúc và hành vi công cụ; không chứng minh chất lượng UX hay tuân thủ WCAG của một sản phẩm.

Tài liệu gốc và giới hạn diễn giải ở [references/sources.md](skills/ui-ux-workflow/references/sources.md). Tài liệu trong repo là phần tổng hợp thực hành, không phải bản sao toàn văn của các nguồn.

Kết quả kiểm tra bản bàn giao và giới hạn môi trường: [VALIDATION.md](VALIDATION.md).
