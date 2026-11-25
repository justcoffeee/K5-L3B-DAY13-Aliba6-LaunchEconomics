# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | [simulated] |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | [simulated] |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | |

- Chi phí mỗi việc thành công (4.472 đ [simulated]) gấp 16,3 lần hoá đơn chia cho số yêu cầu (274,7 đ).
- Khoản chiếm tỉ trọng lớn nhất là làm lại (2.264.000 đ, chiếm 51,8% [simulated]), kế đến là xem lại (1.780.000 đ, chiếm 40,7% [simulated]); tổng chi phí thời gian nhân viên chiếm tới 92,5% [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22x |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69x |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88x |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85x |

- Loại không đáng để trợ lý xử lý là `quoc_te` (chi phí mỗi việc thành công 22.515 đ [simulated], gấp 1,88 lần tự làm 12.000 đ) và `doi_tac` (chỉ tiết kiệm 15% nhưng tỉ lệ thành công thấp 54,4%).
- Với `quoc_te`, chạy lại tới 3 lần hầu như không giúp vì tỉ lệ đạt yêu cầu giảm mạnh qua từng lần thử (lần 1: 30,0%, lần 2: 11,4%, lần 3: 2,2%).

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38x |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48x |

- Chi phí cố định 40.000.000 đ/tháng không làm đổi kết luận ở cả hai mức khối lượng, vì tổng chi phí mỗi việc thành công là 4.599 đ [simulated] (0,38x) và 5.784 đ [simulated] (0,48x), vẫn rẻ hơn nhiều so với mốc 12.000 đ.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | -2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | -20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | -25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | -5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | -8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: chi phí mỗi việc thành công tăng lên 6.543 đ [simulated], tương ứng tăng 46,3% so với gốc 4.472 đ [simulated].
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (+51,8% khi x2) · 2. Tỉ lệ xem lại (+40,7% khi x2) · 3. Lương nhân viên (+23,1% khi tăng 25%).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ [simulated] | 319 | 7.449.781 đ [simulated] | 4.111 đ [simulated] |
| 2 lần | 4.093.220 đ [simulated] | 234 | 6.901.220 đ [simulated] | 4.237 đ [simulated] |
| 3 lần | 4.373.585 đ [simulated] | 222 | 7.037.585 đ [simulated] | 4.472 đ [simulated] |

- Giới hạn rẻ nhất cho công ty là 2 lần (chi phí cả hệ thống 6.901.220 đ [simulated], thấp hơn mức 7.449.781 đ [simulated] của 1 lần và 7.037.585 đ [simulated] của 3 lần).
- Giới hạn rẻ nhất toàn hệ thống (2 lần) không trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần: 4.111 đ [simulated]), do khi chỉ chạy 1 lần thì có tới 319 yêu cầu hỏng bị đẩy sang nhân viên làm thủ công (319 × 12.000 đ = 3.828.000 đ).

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% trong phạm vi `noi_dia` + `hang_nang` là 11.743 đ [simulated] (0,98x so với 12.000 đ) nếu thời gian làm lại là 9 phút, và lên tới 12.415 đ [simulated] (1,03x) nếu làm lại mất 15,3 phút.
- Kết quả này chỉ ra pilot bắt buộc phải kiểm soát thời gian xem lại dưới mức hoà vốn 5,1 phút/yêu cầu (với 9 phút làm lại) và 4,8 phút/yêu cầu (với 15,3 phút làm lại), tránh xem lại kéo dài làm chi phí vượt mốc tự làm 12.000 đ.
