# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Aliba6 (L3B)
- Nhóm được chấm: Nhóm 145 (L3B) — https://github.com/HieuVuong145/K5-L3B-DAY13-Nhom145-LaunchEconomics

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 5 / 10 | Bảng chi phí và pilot_plan làm rất tốt (nêu được power tụt còn 0,64 và chi phí xem lại 100% vọt lên 12.415 đ). Tuy nhiên, dòng Đề xuất cuối cùng ở ho_so_launch_v0.md vẫn bỏ trống ("- ..."), chưa chọn rõ Go / Go có điều kiện / No-go. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 / 10 | Mọi con số đều có nhãn [simulated]; thu hẹp phạm vi vào noi_dia (0,22x) và hang_nang (0,69x), loại quoc_te (1,88x, TC 27,3%) và doi_tac (0,85x) có số liệu chứng minh rõ ràng. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 / 10 | Chia theo nhân viên (20+20) để tránh spillover, tính cỡ mẫu hiệu dụng chính xác (DE=6,96, m=299), 3 luật dừng chuẩn cú pháp NẾU-TRONG-THÌ-KHÔNG THÌ có người phụ trách và thời hạn xử lý cụ thể. |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Kỹ thuật tính toán kinh tế, phân tích độ nhạy và thiết kế pilot (chia 20+20 nhân viên, MDE +6 điểm) của Nhóm 145 rất xuất sắc và có tư duy phản biện tốt. Tuy nhiên, hồ sơ tổng hợp `ho_so_launch_v0.md` chưa chốt dòng Đề xuất chính thức và điều kiện đi kèm.

**Một câu hỏi cho đội trình:**
Trong file hồ sơ `ho_so_launch_v0.md` gửi hội đồng, tại sao dòng Đề xuất cuối cùng vẫn đang để trống `...` chưa chọn giữa Go, Go có điều kiện hay No-go?

**Câu trả lời của đội trình (ghi lại tại buổi):**
Nhóm 145 đã hoàn thành tính toán các chỉ số và thống nhất đề xuất là "Go có điều kiện" (điều kiện: kiểm soát thời gian xem lại ≤ 4,8 phút và theo dõi sát trần 6% tỉ lệ mở lại), đang hoàn thiện cập nhật dòng đề xuất này lên nhánh main trước giờ chốt bài.
