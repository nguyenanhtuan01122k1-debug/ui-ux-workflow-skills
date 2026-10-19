# Dùng skill với Google Antigravity + Figma

Antigravity đọc MCP server và skill toàn cục từ `~/.gemini/config/`. Hai việc cần làm: nối Figma MCP và cài skill `ui-ux-workflow`.

## 1. Nối Figma MCP

Cách nhanh: trong Antigravity mở bảng agent → **… (Additional Options) → MCP Servers**, tìm Figma và cài.

Cách thủ công: chép [mcp_config.json](mcp_config.json) vào `~/.gemini/config/mcp_config.json` (Windows: `%USERPROFILE%\.gemini\config\mcp_config.json`). Nếu file đã có server khác, chỉ thêm khóa `figma` vào `mcpServers`, không ghi đè.

```json
{
  "mcpServers": {
    "figma": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "mcp-remote", "https://mcp.figma.com/mcp"]
    }
  }
}
```

- Cần Node.js (có `npx`). Trên macOS/Linux bỏ `cmd /c`: `"command": "npx", "args": ["-y", "mcp-remote", "https://mcp.figma.com/mcp"]`.
- `mcp-remote` làm cầu nối stdio và mở trình duyệt để đăng nhập Figma (OAuth) ở lần chạy đầu. Chọn **Allow access** bằng tài khoản Figma của bạn.
- Phương án thay thế không cần OAuth: bật **Dev Mode MCP server** trong Figma desktop (Preferences), rồi đổi URL thành `http://127.0.0.1:3845/mcp`. Cách này chỉ đọc được file đang mở trong app desktop và cần ghế Dev/Full.

Khởi động lại Antigravity, mở lại **MCP Servers** và kiểm tra Figma hiển thị các tool như `get_design_context`, `get_screenshot`, `use_figma`. Nếu báo lỗi, gỡ và cài lại server, hoặc xoá cache OAuth tại `~/.mcp-auth` rồi thử lại.

## 2. Cài skill

Toàn cục (mọi workspace), PowerShell ở thư mục repo:

```powershell
$target = Join-Path $env:USERPROFILE '.gemini/config/skills/ui-ux-workflow'
if (Test-Path -LiteralPath $target) { throw 'Skill đã tồn tại; hãy so sánh trước khi cập nhật.' }
New-Item -ItemType Directory -Path (Split-Path $target) -Force | Out-Null
Copy-Item -LiteralPath './skills/ui-ux-workflow' -Destination $target -Recurse
```

Hoặc chỉ cho một dự án: copy vào `<dự án>/.agents/skills/ui-ux-workflow`.

## 3. Luồng làm việc gợi ý

| Bước | Prompt trong Antigravity | Tool Figma chính |
| --- | --- | --- |
| Đọc thiết kế | “Dùng ui-ux-workflow, đọc frame này: `<link Figma>` và tóm tắt cấu trúc, token, component.” | `get_metadata`, `get_variable_defs`, `get_screenshot` |
| Thiết kế mới | “Dùng ui-ux-workflow dựng phương án UI theo style Văn Minh Việt vào file `<link>`, dùng layer chỉnh sửa được.” | `search_design_system`, `use_figma` |
| Đẩy trang code lên Figma | “Đưa trang đang chạy ở localhost lên Figma để review.” | `generate_figma_design`, `use_figma` |
| Code từ Figma | “Triển khai frame `<link>` thành code, dùng token sẵn có của dự án.” | `get_design_context` |
| Bàn giao | “Dùng ui-ux-workflow chuẩn bị bàn giao, ghi link node vào `06-handoff.md`.” | `get_code_connect_map`, `get_screenshot` |

Quy tắc ghi vào Figma (không đè bản cũ, layer thật, font tiếng Việt, kiểm tra screenshot) vẫn theo [references/figma.md](../../skills/ui-ux-workflow/references/figma.md).
