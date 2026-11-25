# Báo cáo cá nhân — CanXuanNghia-2A202603805

## 1. Thông tin thành viên

- Họ tên: Cấn Xuân Nghĩa
- MSSV: 2A202603805
- Email: Chưa bổ sung
- GitHub: [xuannghia2](https://github.com/xuannghia2)
- Nhóm / Lớp: Aliba6 / L3B
- Vai trong nhóm: Người gắn nhãn 1, phụ trách tổng hợp bảng lỗi và cách khắc phục ở CP3.

## 2. Phần việc phụ trách

- Phân loại 20 ca lỗi trong đề bài theo năm loại Google PAIR, dựa trên nguyên nhân gốc.
- Hoàn thiện cột `Nhãn người 1`, căn cứ phân loại và quy tắc phân biệt trong `report/team/bang_loi.md`.
- Đối chiếu với bộ nhãn người 2 của Nguyễn Mạnh Hùng và tính tỉ lệ nhãn trùng.
- Soạn bảng khắc phục cho 5 ca đại diện đủ năm loại, có cách phát hiện đo được và một vai trò phụ trách cho mỗi ca.
- Cập nhật phần đóng góp cá nhân trong `TEAM.md`.

## 3. Đóng góp cụ thể

### Phân loại và giải thích 20 ca lỗi

Tôi sử dụng Codex hỗ trợ đọc mô tả đề bài, soạn 20 nhãn người 1 và căn cứ phân loại từng ca. Phân bố nhãn trong bảng hiện tại:

| Loại lỗi | Các ca | Số ca |
| --- | --- | ---: |
| Do người dùng | 1, 6, 9, 14 | 4 |
| Hệ thống | 2, 7, 8, 15, 20 | 5 |
| Ngữ cảnh | 3, 10, 16, 18 | 4 |
| Giới hạn hệ thống | 4, 11, 13, 19 | 4 |
| Ngầm | 5, 12, 17 | 3 |
| **Tổng** | | **20** |

Phần giải thích làm rõ các ca dễ nhầm: ca 20 thuộc Hệ thống vì thiếu khoá chống trùng; ca 3 thuộc Ngữ cảnh vì tiền về ví đúng thiết kế nhưng khác kỳ vọng của khách; ca 17 thuộc Ngầm vì bảng giá cũ gây sai tiền mà không ai mở lại yêu cầu. Tôi bổ sung các quy tắc phân biệt Hệ thống / Ngầm, Ngữ cảnh / Hệ thống, Giới hạn hệ thống / Hệ thống và Do người dùng / Hệ thống.

### Đối chiếu hai cột nhãn

Bộ nhãn người 2 được giữ nguyên từ commit `e9ba35e`. Hai cột hiện trùng **20/20 ca**, tính bằng `20 ÷ 20 × 100 = 100%`. Bản `bang_loi.md` hiện tại của nhóm ghi đã rà soát, thống nhất và ghi nhận tỉ lệ đồng thuận 100%.

Về quá trình tạo phần của tôi, Codex đã thấy bộ nhãn người 2 trước khi soạn cột người 1. Vì vậy, tôi không coi con số 100% là bằng chứng cho hai lượt gắn nhãn độc lập trong 8 phút. Đây là giới hạn của quá trình thực hiện, dù hai cột nhãn trong hồ sơ hiện khớp nhau.

### Bảng khắc phục năm loại lỗi

Tôi dùng Codex hỗ trợ soạn 5 phương án cho các ca **1, 20, 3, 19, 17**, tương ứng năm loại lỗi:

- **Ca 1 — Do người dùng:** kiểm tra tài khoản trước khi hoàn, chặn đầu vào không hợp lệ và hướng dẫn nhập lại.
- **Ca 20 — Hệ thống:** dùng `idempotency_key`, ràng buộc duy nhất tại sổ cái và đối soát bút toán để ngăn hoàn hai lần.
- **Ca 3 — Ngữ cảnh:** xác nhận rõ nơi nhận là ví LogiX trước khi gửi lệnh, theo dõi yêu cầu mở lại vì nhầm nơi nhận tiền.
- **Ca 19 — Giới hạn hệ thống:** phát hiện đơn ngoài cửa sổ dữ liệu 12 tháng, thông báo giới hạn và chuyển nhân viên kèm tóm tắt.
- **Ca 17 — Ngầm:** kiểm tra phiên bản bảng giá, vô hiệu cache cũ và kiểm tra mẫu 100 đơn/tuần; điều tra ngay khi có đơn lệch tiền.

Mỗi dòng trong bảng chi tiết có event/thuộc tính cần ghi, ngưỡng cảnh báo, tần suất kiểm tra, hành động và vai trò phụ trách. Những event, ngưỡng và biện pháp này là **đề xuất cho pilot**, chưa phải chức năng đã triển khai hoặc kết quả đã đo.

## 4. Bằng chứng

- Commit đóng góp CP3: [`5a828ab`](https://github.com/justcoffeee/K5-L3B-DAY13-Aliba6-LaunchEconomics/commit/5a828ab5e9eebc4c355e334acc70fa3e9c5e92f2) — thêm nhãn đề xuất, căn cứ phân loại, bảng khắc phục và mục đóng góp trong `TEAM.md`.
- Sản phẩm: [bang_loi.md](bang_loi.md), gồm 20 ca, căn cứ phân loại từng ca, quy tắc phân biệt và 5 phương án khắc phục.
- Đóng góp cá nhân được tổng hợp tại [TEAM.md](../../TEAM.md), mục `CanXuanNghia-2A202603805`.
- Nguồn tình huống: mục “Hai mươi ca lỗi” trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Các con số như 212 đơn trong 9 ngày là dữ kiện của ca mẫu, không phải kết quả vận hành do tôi đo.

## 5. Công cụ AI đã dùng

- **Codex:** đọc đề, đề xuất nhãn và lý do cho 20 ca, soạn phương án khắc phục, cập nhật Markdown và hỗ trợ thao tác Git.
- **Kiểm tra đã thực hiện bằng công cụ:** kiểm đếm đủ 20 dòng nhãn; so sánh cột người 2 với bản trước để bảo đảm không bị thay đổi; tính được 20 dòng trùng; kiểm tra bảng khắc phục đủ 5 loại; chạy `git diff --check` để kiểm tra lỗi khoảng trắng.
- Các kiểm tra trên xác nhận cấu trúc và sự nhất quán của bảng. Việc đánh giá nhãn vẫn cần dựa vào mô tả ca và định nghĩa từng loại; không dùng phép đếm này thay cho lượt gắn nhãn độc lập của con người.

## 6. Tự đánh giá

Tôi đã đóng góp phần nội dung CP3: cột nhãn người 1 cho 20 ca, căn cứ và quy tắc phân biệt, 5 phương án khắc phục và mục đóng góp trong `TEAM.md`, với Codex hỗ trợ. Báo cáo này mô tả phần việc đó và kết quả đang ghi trong hồ sơ nhóm.

Điểm cần cải thiện là thực hiện lượt phân loại cá nhân trước khi xem nhãn của người còn lại, lưu lại bộ nhãn ban đầu rồi mới đối chiếu. Tôi cũng cần tự giải thích được các ca dễ nhầm và rà tính khả thi của event, ngưỡng cùng người phụ trách trước khi áp dụng các đề xuất vào pilot.
