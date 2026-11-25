# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Aliba6
- Lớp: L3B
- Thành viên: xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Nhóm thực hiện đánh giá kinh tế triển khai (Launch Economics) và lập kế hoạch pilot Gate 2a cho trợ lý hoàn phí LogiX-VN trên tập dữ liệu giả lập gồm `1.200` yêu cầu (`logix_requests.csv`) và `1.624` lần chạy (`logix_runs.csv`). Cách tiếp cận gồm 5 bước: (1) xây dựng mô hình chi phí mỗi việc thành công từ trace; (2) phân tích độ nhạy và giới hạn chạy lại; (3) phân loại 20 ca lỗi theo Google PAIR; (4) tính cỡ mẫu cụm và thiết kế `pilot_plan.yaml`; (5) đặc tả chỉ số, event, rủi ro kinh tế và tổng hợp hồ sơ `ho_so_launch_v0.md`.

## 3. Giải pháp

- **Nhiệm vụ A & B ([`src/lab13.py`](../../src/lab13.py), [`bang_chi_phi.md`](bang_chi_phi.md)):** Hoàn thành 3 phép thử A1 đạt (`1,20 · 1,25 · 1,25`), viết hàm `mo_hinh` tính đủ token, tool và thời gian nhân viên (xem lại, làm lại), tách theo 4 loại yêu cầu (`noi_dia`, `hang_nang`, `quoc_te`, `doi_tac`), cộng chi phí cố định 40 triệu đ/tháng, và chạy 9 kịch bản độ nhạy B1–B4.
- **Nhiệm vụ C ([`bang_loi.md`](bang_loi.md)):** Hoàn thành và chốt hai bộ nhãn 20/20 ca theo 5 loại Google PAIR (đồng thuận `20/20 = 100%`), kèm căn cứ phân loại 20 ca và bảng khắc phục 5 ca (`1, 20, 3, 19, 17`) có cách phát hiện đo được và vai trò phụ trách.
- **Nhiệm vụ D ([`pilot_plan.yaml`](pilot_plan.yaml)):** Tính 5 câu D1 bằng `NormalDist`, phân tích đánh đổi và chọn chia cụm theo nhân viên `20 + 20` (`unit: staff`), phạm vi `noi_dia` + `hang_nang`, thiết lập 4 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`.
- **Nhiệm vụ E ([`chi_so.md`](chi_so.md), [`ho_so_launch_v0.md`](ho_so_launch_v0.md)):** Tính thử 3 chỉ số trên dữ liệu chạy thử, đề xuất 2 chỉ số mới, thiết kế 10 event có `trace_id`, lập 4 dòng rủi ro kinh tế và tổng hợp thành hồ sơ 1 trang để trình duyệt chéo Gate 2a ([`phieu_cham.md`](phieu_cham.md)).

## 4. Kết quả

- **Chi phí mỗi việc thành công:** `4.472 đ` toàn mẫu (`simulated`), gấp `16,3×` hoá đơn token + tool chia cho số yêu cầu (`274,7 đ`), do chi phí thời gian nhân viên chiếm `92,5%` (`simulated`). Trong phạm vi `noi_dia` + `hang_nang`: `3.414 đ` (`simulated`); cộng chi phí cố định 40 triệu đ/tháng là `4.599 đ` (`0,38×` so với mốc tự làm `12.000 đ`) ở 45.000 yc/tháng và `5.784 đ` (`0,48×`) ở nửa khối lượng (`simulated`).
- **Phạm vi và giới hạn chạy lại:** Giữ `noi_dia` (`2.696 đ`, `0,22×`, `simulated`) và `hang_nang` (`8.221 đ`, `0,69×`, `simulated`); loại `quoc_te` (`22.515 đ`, `1,88×`, `simulated`) và `doi_tac` (`10.215 đ`, `0,85×`, `simulated`). Ba yếu tố nhạy nhất: số ca làm lại (`+51,8%`), tỉ lệ xem lại (`+40,7%`), lương nhân viên (`+23,1%`) (`simulated`). Giới hạn `2 lần` chạy cho tổng chi phí cả hệ thống thấp nhất (`6.901.220 đ`, `simulated`). Nếu xem lại 100%, chi phí lên `11.743 đ` (`0,98×`, hoà vốn ≤ `5,1 phút` xem/yc) hoặc `12.415 đ` (`1,03×`) nếu làm lại `15,3 phút` (`simulated`).
- **Chỉ số và thiết kế pilot:** Đợt chạy thử (không đối chứng) ghi nhận chỉ số chính `82,83%` (phạm vi `92,26%`), bỏ qua gợi ý `27,12%` (phạm vi `21,09%`), lỗi lọt đến khách `4,25%` (phạm vi `3,97%`). Pilot chia `20 + 20` nhân viên chỉ phát hiện được mức chênh `6 điểm` (`n = 859/nhóm`, `m ≥ 299`, `DE = 6,96`; power còn `0,64` ở mức `5 điểm`).
- **Đề xuất cuối tại [`ho_so_launch_v0.md`](ho_so_launch_v0.md):** **Go có điều kiện** với 4 điều kiện có người phụ trách và ngày kiểm tra rõ ràng.
- **Kết quả duyệt chéo:** Chưa có kết quả từ hội đồng (chờ phiên trình bày Gate 2a và hoàn thiện [`phieu_cham.md`](phieu_cham.md)).

## 5. Khó khăn và cách xử lý

- **Hạn chế cỡ mẫu cụm (40 nhân viên, 12 depot):** Không cách chia theo cụm nào đủ mẫu cho mức chênh `5 điểm` (`20 / 0,02 = 1.000 < 1.251`). Nhóm xử lý bằng cách chọn chia theo nhân viên `20 + 20` để tách được tác động, chấp nhận `mde = 0,06` và nêu rõ power `0,64` ở mức `5 điểm` trong hồ sơ.
- **Ngưỡng an toàn thực tế:** Tỉ lệ mở lại hiện tại là `4,25%`, nên đặt trần `3%` sẽ khiến pilot dừng ngay tuần đầu; nhóm chuyển sang so sánh với nhóm đối chứng (`≥ 2 điểm`) kèm trần tuyệt đối `6%`.
- **Khắc phục lỗi hệ thống:** Bảng lỗi đã chốt 100% nhưng vẫn còn lỗi nghiêm trọng như hoàn trùng (ca 20) và báo thành công khi sổ cái lỗi 503 (ca 7); nhóm đưa việc sửa hai lỗi này vào điều kiện bắt buộc trước ngày mở pilot.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong [TEAM.md](../../TEAM.md).

## 7. Hạn chế và hướng cải thiện

- Thời gian xem lại và làm lại hiện dùng cột `_simulated`; cần bật đủ `10 event` có `trace_id` để đo thật ngay từ tuần 1 của pilot.
- Cần hoàn thiện đối chiếu hai bộ nhãn và bảng khắc phục 5 ca trong `bang_loi.md`, đồng thời triển khai khoá chống hoàn trùng (`idempotency_key`) trước khi chạy thử nghiệm có kiểm soát.

## 8. Tài liệu tham khảo

- Đề bài và hướng dẫn buổi lab: [`docs/Ngay13_Lab13_De_bai_hoc_vien.docx`](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx), [`docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)
- Tiêu chí chấm và quy định nộp bài: [`RUBRIC.md`](../../RUBRIC.md), [`SUBMISSION.md`](../../SUBMISSION.md), [`CHECKPOINTS.md`](../../CHECKPOINTS.md)
