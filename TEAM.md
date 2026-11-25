# Team

## Thông tin nhóm

- Tên nhóm: Aliba6
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Aliba6-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/justcoffeee/K5-L3B-DAY13-Aliba6-LaunchEconomics · `main` · [`91175e9`](https://github.com/justcoffeee/K5-L3B-DAY13-Aliba6-LaunchEconomics/commit/91175e95c53f3bbf75a8134fb5ef8877e80bd26d) (commit chốt nội dung; commit sau chỉ ghi mã này)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Phạm Hoàng Huy (nhóm trưởng) | 2A202603836 | huyclaynun@gmail.com | [justcoffeee](https://github.com/justcoffeee) | Người viết code (trước giải lao) → chỉ số, event, rủi ro |
|   2 | Lê Thanh Tùng | 2A202603819 | lethanhtung6803@gmail.com | [griin-03](https://github.com/griin-03) | Người kiểm số → người viết code (sau giải lao) |
|   3 | Cấn Xuân Nghĩa | 2A202603805 | | [xuannghia2](https://github.com/xuannghia2) | Người gắn nhãn 1 |
|   4 | Nguyễn Mạnh Hùng | 2A202603852 | | [HungLunnn](https://github.com/HungLunnn) | Người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Mỗi người một mục dưới đây (phân công dự kiến, cập nhật khi xong).

## PhamHoangHuy-2A202603836

### Phần việc phụ trách

- Viết `src/lab13.py` cho CP1–CP2: ba hàm A1, `mo_hinh`, A3, A4, các kịch bản B1–B4
- Sau giải lao: `report/team/chi_so.md` (E1 chỉ số, danh sách event, E2 rủi ro kinh tế)

### Đóng góp cụ thể

- Tạo repo nhóm, mời thành viên, chia vai, điền `TEAM.md`.
- `src/lab13.py`: A1 (ba phép thử ĐẠT), `mo_hinh` (4.472 đ/việc [simulated]), A3, A4, B1–B4; bổ sung in power 0,64 và tỉ lệ mở lại 4,25% vào phần D1; tính ba chỉ số E1.
- `report/team/chi_so.md`: ba chỉ số (82,83% · 27,12% · 4,25%), hai chỉ số đề xuất, mười event có `trace_id`, bốn dòng rủi ro kinh tế.
- Sửa `report/team/pilot_plan.yaml` theo cách chia nhân viên 20 + 20 và bốn luật dừng.

### Bằng chứng

- Commit `95eeb1e`, `bfa61a1`, `96f50c5`, `6ec17cf` (CP1); `6f197c7`, `7042493`, `8df23e3`, `b4af985` (CP2); `8ce01ee`, `133215d` (CP4); `816cc16` (CP5).
- Báo cáo cá nhân: `report/team/2A202603836_PhamHoangHuy.md`.

## LeThanhTung-2A202603819

### Phần việc phụ trách

- CP1–CP2: tính tay đối chiếu, điền `report/team/bang_chi_phi.md`
- Sau giải lao: viết phần D1 trong `src/lab13.py`, hoàn thiện `report/team/pilot_plan.yaml`

### Đóng góp cụ thể

- Hoàn thiện toàn bộ bảng chi phí A1–A4, B1–B4 trong `report/team/bang_chi_phi.md`, đảm bảo nhãn `[simulated]` tại A2, A3, A4, B1, B2, B3, B4 và câu trả lời $\le 3$ dòng có số liệu.
- Viết code D1 trong `src/lab13.py` tính cỡ mẫu 5 kịch bản a–e bằng `NormalDist`.
- Tham gia rà soát và hoàn thiện `report/team/pilot_plan.yaml` theo cách chia cụm nhân viên $20 + 20$ (`unit: staff`), xác định MDE $0,06$ và 4 luật dừng chuẩn.
- Cập nhật báo cáo cá nhân `report/team/2A202603819_LeThanhTung.md`.

### Bằng chứng

- Commit `e729b74` và commit cập nhật B3/B4, `TEAM.md`
- Các file: `report/team/bang_chi_phi.md`, `src/lab13.py`, `report/team/pilot_plan.yaml`, `report/team/2A202603819_LeThanhTung.md`

## CanXuanNghia-2A202603805

### Phần việc phụ trách

- CP3: phân loại 20 ca lỗi ở cột người 1, tổng hợp căn cứ và quy tắc phân biệt trong `report/team/bang_loi.md`.
- Đối chiếu hai cột nhãn và soạn bảng khắc phục cho 5 ca đại diện đủ năm loại.
- Cập nhật đóng góp và báo cáo cá nhân.

### Đóng góp cụ thể

- Hoàn thiện nội dung cột người 1 cho 20/20 ca với Codex hỗ trợ: 4 ca Do người dùng, 5 ca Hệ thống, 4 ca Ngữ cảnh, 4 ca Giới hạn hệ thống và 3 ca Ngầm; kèm căn cứ từng ca và bốn quy tắc phân biệt các loại dễ nhầm.
- Đối chiếu với bộ nhãn người 2 của Hùng từ commit `e9ba35e`: trùng 20/20 ca (100%). `bang_loi.md` hiện ghi đã rà soát, thống nhất; quá trình soạn bằng Codex đã thấy nhãn người 2, nên không dùng kết quả này để khẳng định hai lượt gắn nhãn độc lập trong 8 phút.
- Soạn 5 phương án khắc phục cho ca 1, 20, 3, 19, 17, đủ năm loại; mỗi dòng có cách phát hiện đo được, ngưỡng, tần suất và vai trò phụ trách. Đây là đề xuất giám sát cho pilot, chưa phải biện pháp đã triển khai.
- Điền báo cáo cá nhân `report/team/2A202603805_CanXuanNghia.md`, nêu sản phẩm, bằng chứng, công cụ AI và giới hạn của quá trình thực hiện.

### Bằng chứng

- Commit [`5a828ab`](https://github.com/justcoffeee/K5-L3B-DAY13-Aliba6-LaunchEconomics/commit/5a828ab5e9eebc4c355e334acc70fa3e9c5e92f2): phần nhãn người 1, căn cứ phân loại, bảng khắc phục và đóng góp CP3.
- File: `report/team/bang_loi.md`; báo cáo cá nhân: `report/team/2A202603805_CanXuanNghia.md`.
- Nguồn ca lỗi: mục “Hai mươi ca lỗi” trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`; công cụ hỗ trợ: Codex.

## NguyenManhHung-2A202603852

### Phần việc phụ trách

- Điền `report/team/ho_so_launch_v0.md` từ đầu buổi
- CP3: gắn nhãn 20 ca độc lập (Người gắn nhãn 2)
- Duyệt chéo: `report/team/phieu_cham.md`; cuối buổi: `report/team/group_report.md`

### Đóng góp cụ thể

- `report/team/bang_loi.md`: Hoàn thành gắn nhãn độc lập 20/20 ca lỗi (cột Nhãn người 2) theo 5 loại Google PAIR dựa trên nguyên nhân gốc.
- `report/team/ho_so_launch_v0.md`: Tổng hợp đầy đủ 7 mục hồ sơ Gate 2a (gắn nhãn `simulated` cho các mục 1, 2, 3, 7; nêu rõ con số bất lợi power `0,64` và mức hoà vốn xem lại `5,1 phút`) và chốt đề xuất **Go có điều kiện** với 4 điều kiện có người phụ trách và ngày kiểm tra.
- `report/team/phieu_cham.md`: Chuẩn bị phiếu chấm hội đồng Gate 2a cho nhóm Aliba6 (L3B), sẵn sàng điền điểm và câu hỏi kiểm tra chéo khi nhận hồ sơ nhóm bạn.
- `report/team/group_report.md`: Viết báo cáo tổng hợp nhóm (tối đa 2 trang), liên kết các hồ sơ A–E và tóm tắt kết quả, khó khăn, hướng cải thiện.
- Cập nhật báo cáo cá nhân `report/team/2A202603852_NguyenManhHung.md`.

### Bằng chứng

- Các file: `report/team/bang_loi.md`, `report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md`, `report/team/group_report.md`, `report/team/2A202603852_NguyenManhHung.md`, `TEAM.md`.
