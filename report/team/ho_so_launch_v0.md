# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Aliba6 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | `4.472 đ` toàn mẫu (`16,3×` hoá đơn token + tool `274,7 đ`); trong phạm vi `noi_dia` + `hang_nang`: `3.414 đ`, cộng cố định 40 triệu/tháng còn `4.599 đ` ở 45.000 yc/tháng hoặc `5.784 đ` ở nửa khối lượng (`simulated`) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (`+51,8%` khi ×2 → `6.787 đ`) · 2. Tỉ lệ xem lại (`+40,7%` khi ×2 → `6.292 đ`) · 3. Lương nhân viên (`+23,1%` khi +25% → `5.506 đ`) (`simulated`) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Tự làm `12.000 đ` (6 phút). `noi_dia` `2.696 đ` (`0,22×`), `hang_nang` `8.221 đ` (`0,69×`), `doi_tac` `10.215 đ` (`0,85×`), `quoc_te` `22.515 đ` (`1,88×`). Giới hạn 2 lần chạy rẻ nhất toàn hệ thống (`6.901.220 đ`). Xem lại 100% trong phạm vi hết `11.743 đ` (`0,98×`, hoà vốn ≤ `5,1 phút` xem/yc) hoặc `12.415 đ` (`1,03×`) nếu làm lại `15,3 phút` (`simulated`) | Giả lập | Kế toán trưởng |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử (không đối chứng): chính `82,83%` (`994/1.200`; phạm vi `92,26%`), bỏ qua gợi ý `27,12%` (`48/177`; phạm vi `21,09%`), lỗi lọt đến khách `4,25%` (`51/1.200`; phạm vi `3,97%`). Đủ 10 event có `trace_id` + 2 chỉ số tự đề xuất | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | `20/20` ca đã chốt đồng thuận (`20/20 = 100%`, đạt ≥ `80%`); đủ bảng khắc phục `5 ca` theo 5 loại Google PAIR (`ca 1, 20, 3, 19, 17`) có event, ngưỡng và vai trò phụ trách | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia cụm theo nhân viên `20 + 20` (`unit: staff`), phạm vi `noi_dia` + `hang_nang`, `mde = 0,06` (`n = 859/nhóm`, `m ≥ 299` yc/NV, `DE = 6,96`; con số bất lợi: power còn `0,64` nếu tác động thật `5 điểm`), rollout `[0.10, 0.25, 0.50]`, 4 luật dừng đủ 4 vế, ngày quyết định `2027-01-11` | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | 4 dòng rủi ro từ bảng độ nhạy: làm lại ×2 (`+51,8%`), xem lại 100% kéo dài (`11.743–12.415 đ`), xem lại ×2 (`+40,7%`), khối lượng giảm 50% (`+2.370 đ/việc` cố định, tổng `5.784 đ`) (`simulated`) | Giả lập | Giám đốc vận hành LogiX-VN |

**Đề xuất:** **Go có điều kiện** cho pilot phạm vi `noi_dia` + `hang_nang` (loại `quoc_te` vì `1,88×` và thành công `27,3%`, loại `doi_tac` vì điều khoản riêng và thành công `54,4%`), kèm bốn điều kiện bắt buộc:

- **Điều kiện 1 (sửa lỗi hệ thống nghiêm trọng):** Sửa khoá chống hoàn trùng (`idempotency_key`, ca 20) và đối soát ghi sổ cái khi lỗi 503 (ca 7) trước khi mở pilot. — *Phụ trách:* Kỹ sư trưởng agent · *Ngày kiểm tra:* `2026-12-04`.
- **Điều kiện 2 (ký chấp nhận đánh đổi cỡ mẫu và ngưỡng an toàn):** Giám đốc vận hành ký chấp nhận `mde = 0,06` (power còn `0,64` nếu tác động thật chỉ `5 điểm`) và luật dừng an toàn theo chênh lệch với đối chứng `≥ 2 điểm` kèm trần tuyệt đối `6%` (do nền mở lại hiện tại là `4,25%`, phạm vi `3,97%`). — *Phụ trách:* Giám đốc vận hành LogiX-VN · *Ngày kiểm tra:* `2026-12-04`.
- **Điều kiện 3 (bật đo thật và giới hạn chạy lại):** Bật đủ `10 event` có `trace_id`, đặt giới hạn tối đa `2 lần` chạy lại (chi phí hệ thống thấp nhất `6.901.220 đ`, `simulated`), và thay toàn bộ số phút `_simulated` bằng thời gian xem lại/làm lại đo thật sau tuần đầu. — *Phụ trách:* PM trợ lý hoàn phí · *Ngày kiểm tra:* `2026-12-14` (cuối bước `0.10`).
- **Điều kiện 4 (kiểm soát thời gian xem lại):** Áp dụng lộ trình giảm xem lại theo bậc và giữ thời gian xem lại trung bình `≤ 5 phút/yêu cầu` (dưới ngưỡng hoà vốn `5,1 phút`, `simulated`), vì xem lại 100% kéo dài sẽ mất lợi thế chi phí (`0,98×–1,03×`). — *Phụ trách:* Trưởng nhóm CSKH · *Ngày kiểm tra:* `2026-12-21` (cuối bước `0.25`).
