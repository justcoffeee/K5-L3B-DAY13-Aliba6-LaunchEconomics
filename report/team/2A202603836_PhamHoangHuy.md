# Báo cáo cá nhân — PhamHoangHuy-2A202603836

## 1. Thông tin thành viên

- Họ tên: Phạm Hoàng Huy
- MSSV: 2A202603836
- Email: huyclaynun@gmail.com
- GitHub: justcoffeee
- Vai trong nhóm: Nhóm trưởng; người viết code (trước giải lao); sau giải lao phụ trách chỉ số, event, rủi ro

## 2. Phần việc phụ trách

- Tạo repo nhóm (fork, đặt tên `K5-L3B-DAY13-Aliba6-LaunchEconomics`), mời thành viên, điền `TEAM.md`, chia vai.
- Viết `src/lab13.py` cho CP1–CP2: A1, A2, A3, A4, B1–B4.
- Sau giải lao: `report/team/chi_so.md` (E1, E2) và phần tính ba chỉ số E1 trong `src/lab13.py`.
- Hỗ trợ CP4: soát và sửa `report/team/pilot_plan.yaml`.

## 3. Đóng góp cụ thể

- **A1:** ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử đạt 1,20 · 1,25 · 1,25.
- **A2:** hàm `mo_hinh` tính chi phí mỗi việc thành công từ trace: tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm 978 việc thành công. Kết quả 4.472 đ [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ). Hàm nhận sẵn tham số giá, hệ số và `max_lan_chay` để nhiệm vụ B gọi lại.
- **A3:** tách theo loại; `quoc_te` 22.515 đ = 1,88× [simulated], tỉ lệ ok theo lần thử 30% → 11,4% → 2,2%, nên chạy lại không giúp. Đề xuất phạm vi pilot `noi_dia` + `hang_nang`.
- **A4:** cộng chi phí cố định 40 triệu đ/tháng: 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng, 5.784 đ = 0,48× nếu còn một nửa [simulated].
- **B1–B4:** chín kịch bản độ nhạy; xếp hạng số ca làm lại (+51,8%) · tỉ lệ xem lại (+40,7%) · lương (+23,1%) [simulated]; giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ); xem lại 100% thì 11.743 đ = 0,98×, hoà vốn ≤ 5,1 phút xem mỗi yêu cầu [simulated].
- **D1 (bổ sung vào code của Tùng):** in power 0,64 khi chọn mức chênh 6 điểm mà tác động thật chỉ 5 điểm, và tỉ lệ mở lại 7 ngày hiện tại 4,25% (51/1.200).
- **D3:** sửa `pilot_plan.yaml` sau khi nhóm chọn chia theo nhân viên 20 + 20: mde 0,06, n 859, DE 6,96; sửa tỉ lệ mở lại; viết lại bốn luật dừng đủ bốn vế (an toàn, chi phí, sử dụng, xem lại).
- **E1, E2:** ba chỉ số 82,83% · 27,12% · 4,25% tính bằng code; hai chỉ số tự đề xuất; mười event có `trace_id` kèm kiểm tra chéo chỉ số ↔ event; bốn dòng rủi ro kinh tế lấy số từ bảng độ nhạy.

## 4. Bằng chứng

Commit trên nhánh `main`:

| Commit | Nội dung |
| --- | --- |
| `955e6d0` | Điền thông tin nhóm, tạo báo cáo cá nhân cho 4 thành viên |
| `95eeb1e` | CP1 · A1 |
| `bfa61a1` | CP1 · A2 |
| `96f50c5` | CP1 · A3 |
| `6ec17cf` | CP1 · A4 |
| `6f197c7` | CP2 · B1 |
| `7042493` | CP2 · B2 |
| `8df23e3` | CP2 · B3 |
| `b4af985` | CP2 · B4 |
| `8ce01ee` | CP4 · D1: in power và tỉ lệ mở lại |
| `133215d` | CP4 · D3: sửa `pilot_plan.yaml` |
| `816cc16` | CP5 · E1, E2: `chi_so.md` và ba chỉ số trong `lab13.py` |

File: `src/lab13.py`, `report/team/chi_so.md`, `report/team/pilot_plan.yaml`, `TEAM.md`.

## 5. Công cụ AI đã dùng

- **Claude (Claude Code):** đọc đề, gợi ý cách chia việc, viết code `lab13.py` từ A1 đến B4, phần E1, và soạn nháp `chi_so.md`, `pilot_plan.yaml`.
- **Cách tự kiểm tra:**
  - Chạy `python lab13.py` sau mỗi phần; ba phép thử A1 phải in ĐẠT trước khi làm tiếp.
  - Đối chiếu từng con số A2, A3, A4, B1–B4, D1, E1 với bảng số trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; tất cả nằm trong sai số 2%.
  - Tự kiểm tra của CP2: mỗi kịch bản "giảm một nửa" thay đổi đúng bằng nửa kịch bản "gấp đôi".
  - Kiểm tra `pilot_plan.yaml` bằng `yaml.safe_load`, không còn dấu `?` ngoài chú thích, không có từ cấm.
- Không dùng AI để bịa số: mọi con số trong hồ sơ do `lab13.py` tính ra.

## 6. Tự đánh giá

- Hoàn thành phần code A–B và `chi_so.md` đúng hạn, số khớp đáp án.
- Tự giải thích được: vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công; vì sao chia theo nhân viên chỉ đạt tối đa 1.000 mẫu hiệu dụng (20 / ICC) nên phải chấp nhận mức chênh 6 điểm.
- Cần cải thiện: phụ thuộc nhiều vào AI khi viết code; lần sau tự viết hàm trước rồi mới nhờ soát.
