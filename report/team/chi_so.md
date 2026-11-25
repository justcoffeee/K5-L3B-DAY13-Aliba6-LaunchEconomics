# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Số tính bằng `src/lab13.py` (mục E1 và B). Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200); trong phạm vi noi_dia + hang_nang 92,26% (906/982) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177: 41 sửa, 7 bỏ); trong phạm vi 21,09% (27/128) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200); trong phạm vi 3,97% (39/982) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm trợ lý được nhân viên mở bằng trợ lý | Số `request_id` có `agent_suggestion_shown`, chia số `refund_request_created` có `arm = tro_ly` | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra (100 đơn/tuần) | Không cần tính |

Chỉ số chính trong đợt chạy thử là 82,83%. Không viết "trợ lý đã nâng chỉ số từ 0,70", vì đợt chạy thử không có nhóm đối chứng; con số 0,70 đo ở thời điểm khác, trên nhóm khác.

## Danh sách event

Mười event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, depot, staff_id, loai, so_tien, arm (tro_ly / doi_chung), trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status (ok / loi), trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu / sua / bo), phut_xem_lai đo thật, trace_id | Khi bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| `handoff_to_staff` | Agent | reason (het_lan_chay / thieu_du_lieu / ngoai_pham_vi), tom_tat, trace_id | Khi chuyển yêu cầu cho nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua (ok / loi), trace_id | Khi ghi lệnh hoàn vào sổ cái |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách | reopened_at, ly_do, trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính: `refund_request_created` (mẫu số, thời điểm tạo) + `ticket_closed` (đóng trong 24 giờ) + `ticket_reopened` (không mở lại trong 7 ngày).
- Bỏ qua gợi ý: `staff_review_decision` (tử số là sua + bo, mẫu số là mọi quyết định).
- Lỗi lọt đến khách: `ticket_reopened` chia `refund_request_created`.
- Mở bằng trợ lý (đề xuất): `agent_suggestion_shown` chia `refund_request_created` có `arm = tro_ly`.
- Hoàn sai tiền qua kiểm tra mẫu (đề xuất): `audit_sample_checked`.
- Chi phí mỗi việc thành công đo thật (cho luật dừng chi phí): `agent_run_completed` (token, tool) + `staff_review_decision` và `staff_rework_completed` (phút thật, thay cho cột simulated) + `ticket_closed` / `ticket_reopened` (việc thành công).
- Chống hoàn trùng (ca 20) và báo "đã hoàn" khi sổ cái lỗi (ca 7): `refund_ledger_write` theo `idempotency_key` và `ket_qua`.

Cả năm chỉ số và luật dừng chi phí đều tính được từ danh sách trên.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, chi phí mỗi việc thành công từ 4.472 đ lên 6.787 đ [simulated]; yếu tố nhạy nhất (B2) | Tỉ lệ làm lại theo tuần vượt 7% (đợt chạy thử 4,89% trong phạm vi: 48/982) | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất để tìm nguyên nhân | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ; 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated] (B4) | % yêu cầu được xem lại còn trên 50%, hoặc phút xem lại trung bình trên 5 phút (hoà vốn 5,1 phút [simulated]) ở cuối bước 0.25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ dưới 15%; không tăng lên bước 0.50 khi chưa đạt | Trưởng nhóm CSKH |
| Tỉ lệ xem lại gấp đôi | +40,7%, lên 6.292 đ [simulated] (B1) | Tỉ lệ yêu cầu được xem lại theo tuần vượt 30% (đợt chạy thử 14,75%: 177/1.200) | Tìm loại yêu cầu gây tăng, tạm dừng mở rộng loại đó | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa (4.599 đ thành 5.784 đ [simulated], A4) | Số việc thành công theo tuần dưới 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | Giám đốc vận hành |
