# Báo cáo cá nhân — NguyenManhHung-2A202603852

## 1. Thông tin thành viên

- Họ tên: Nguyễn Mạnh Hùng
- MSSV: 2A202603852
- Email:
- GitHub: [HungLunnn](https://github.com/HungLunnn)
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- **CP3 (Nhiệm vụ C):** Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (Do người dùng, Hệ thống, Ngữ cảnh, Giới hạn hệ thống, Ngầm) dựa trên nguyên nhân gốc vào `report/team/bang_loi.md`.
- **Giữ hồ sơ (`report/team/ho_so_launch_v0.md`):** Tổng hợp kết quả các nhiệm vụ A–E vào trang hồ sơ 7 mục, gắn nhãn `Giả lập` cho các mục dùng `_simulated`, và hoàn thiện đề xuất **Go có điều kiện**.
- **Duyệt chéo (`report/team/phieu_cham.md`) & cuối buổi (`report/team/group_report.md`):** Chuẩn bị phiếu chấm hội đồng Gate 2a và viết báo cáo tổng hợp nhóm.

## 3. Đóng góp cụ thể

1. **Gắn nhãn độc lập 20 ca lỗi (`report/team/bang_loi.md`):**
   - Hoàn thành phân loại 20/20 ca ở cột `Nhãn người 2` theo nguyên nhân gốc (4 ca `Do người dùng`: 1, 6, 9, 14; 5 ca `Hệ thống`: 2, 7, 8, 15, 20; 4 ca `Ngữ cảnh`: 3, 10, 16, 18; 4 ca `Giới hạn hệ thống`: 4, 11, 13, 19; 3 ca `Ngầm`: 5, 12, 17).
   - Giữ nguyên cột `Nhãn người 1` và các cột đối chiếu để chờ Người gắn nhãn 1 hoàn thành và tính tỉ lệ đồng thuận khách quan.
2. **Hoàn thiện hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`):**
   - Tổng hợp đầy đủ 7 mục với số liệu khớp `src/lab13.py`, `bang_chi_phi.md`, `chi_so.md`, `pilot_plan.yaml`: CPS `4.472 đ` (`simulated`), 3 yếu tố nhạy nhất (làm lại `+51,8%`, xem lại `+40,7%`, lương `+23,1%`, `simulated`), phạm vi `noi_dia` + `hang_nang`, chỉ số thử nghiệm (`82,83%`, `27,12%`, `4,25%`), kế hoạch pilot `20 + 20` nhân viên (`mde = 0,06`, `n = 859`, `DE = 6,96`, power `0,64` ở mức `5 điểm`).
   - Ghi nhận trạng thái (`Giả lập` cho mục 1, 2, 3, 7; `Xong, có bằng chứng` cho mục 4, 5, 6 sau khi `bang_loi.md` có đủ 2 bộ nhãn và bảng khắc phục 5 ca) và phân công rõ một vai trò phụ trách cho từng mục.
   - Đề xuất **Go có điều kiện** kèm 4 điều kiện cụ thể (sửa lỗi ca 7 & ca 20, hoàn tất `bang_loi.md`, ký chấp nhận power `0,64` và ngưỡng an toàn `6%`, bật 10 event và giới hạn 2 lần chạy, kiểm soát xem lại `≤ 5 phút/yc`).
3. **Phiếu chấm Gate 2a (`report/team/phieu_cham.md`) và Báo cáo nhóm (`report/team/group_report.md`):**
   - Chuẩn bị mẫu phiếu chấm với thông tin hội đồng `Aliba6 (L3B)` và bộ câu hỏi kiểm tra bằng chứng Gate 2a.
   - Viết báo cáo nhóm ngắn gọn dưới 2 trang tổng hợp mục tiêu, giải pháp A–E, kết quả chính, khó khăn và hướng cải thiện.

## 4. Bằng chứng

- Các file đã cập nhật:
  - `report/team/bang_loi.md` (cột Nhãn người 2 đủ 20 ca)
  - `report/team/ho_so_launch_v0.md` (đủ 7 mục + đề xuất Go có điều kiện)
  - `report/team/phieu_cham.md` (phiếu chấm hội đồng Aliba6)
  - `report/team/group_report.md` (báo cáo nhóm)
  - `TEAM.md` (cập nhật mục đóng góp cá nhân)
  - `report/team/2A202603852_NguyenManhHung.md`

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI để đọc đối chiếu số liệu từ `src/lab13.py` và các hồ sơ nhóm (`bang_chi_phi.md`, `chi_so.md`, `pilot_plan.yaml`), phân tích nguyên nhân gốc 20 ca lỗi và soạn thảo các file báo cáo.
- Tự kiểm tra lại kết quả bằng cách chạy `cd src && python lab13.py`, kiểm tra `yaml.safe_load` trên `pilot_plan.yaml`, rà soát nhãn `simulated`/`Giả lập`, kiểm tra không có từ cấm trong `report/team/`, và đối chiếu từng con số giữa các file hồ sơ.

## 6. Tự đánh giá

- Hoàn thành đầy đủ phần việc của Thành viên 4 (Người gắn nhãn 2, kiêm giữ hồ sơ) với số liệu nhất quán giữa code và các tài liệu báo cáo.
- Điểm còn chờ phối hợp: điền điểm thực tế vào `phieu_cham.md` tại phiên duyệt chéo Gate 2a khi nhận được hồ sơ nhóm bạn.
