# Báo cáo cá nhân — LeThanhTung-2A202603819

## 1. Thông tin thành viên

- Họ tên: Lê Thanh Tùng
- MSSV: 2A202603819
- Email: lethanhtung6803@gmail.com
- GitHub: griin-03
- Vai trong nhóm: Kiểm số và `bang_chi_phi.md`, sau giải lao viết code D1 và `pilot_plan.yaml`

## 2. Phần việc phụ trách

- **Trước giải lao:** Kiểm tra, xác minh toàn bộ các con số tài chính từ Nhiệm vụ A (A1, A2, A3, A4) và B (B1, B2, B3, B4); hoàn thiện bảng chi phí `report/team/bang_chi_phi.md` với đầy đủ nhãn `[simulated]` và độ dài mỗi câu trả lời $\le 3$ dòng có số liệu cụ thể.
- **Sau giải lao:** Viết code cho Nhiệm vụ D1 (`co_mau`, tính toán kích thước mẫu cho các kịch bản a, b, c, d, e) trong `src/lab13.py`; hoàn thiện kế hoạch pilot chuẩn trong `report/team/pilot_plan.yaml`.

## 3. Đóng góp cụ thể

1. **Kiểm số và hoàn thiện `report/team/bang_chi_phi.md`:**
   - **A1:** Xác thực 3 phép thử đáp án biết trước ($1,20$; $1,25$; $1,25$).
   - **A2:** Kiểm số tổng chi phí $4.373.585$ đ [simulated], chi phí mỗi việc thành công $4.472$ đ [simulated] (gấp $16,3$ lần hóa đơn token+tool mỗi yêu cầu $274,7$ đ), tỉ trọng giờ nhân viên chiếm $92,5\%$ (làm lại $51,8\%$, xem lại $40,7\%$).
   - **A3:** Xác thực phạm vi triển khai `noi_dia` ($2.696$ đ [simulated], $0,22\times$) và `hang_nang` ($8.221$ đ [simulated], $0,69\times$); loại bỏ `quoc_te` ($22.515$ đ [simulated], $1,88\times$) và `doi_tac` ($10.215$ đ [simulated], $0,85\times$).
   - **A4:** Xác thực chi phí cố định không làm đổi kết luận ở quy mô đầy đủ ($4.599$ đ [simulated], $0,38\times$) và nửa khối lượng ($5.784$ đ [simulated], $0,48\times$).
   - **B1 & B2:** Đo lường 9 kịch bản độ nhạy; kịch bản token $\times 2$ cùng xem lại $\times 2$ là $6.543$ đ [simulated] ($+46,3\%$). Xếp hạng 3 yếu tố nhạy nhất: Làm lại $\to$ Xem lại $\to$ Lương nhân viên.
   - **B3:** Xác định giới hạn chạy lại rẻ nhất cho toàn hệ thống là **2 lần** ($6.901.220$ đ), không trùng với giới hạn CPS thấp nhất là 1 lần ($4.111$ đ [simulated]).
   - **B4:** Đánh giá rủi ro xem lại 100% phạm vi pilot làm chi phí đội lên $11.743$ đ ($0,98\times$) đến $12.415$ đ ($1,03\times$), khẳng định tầm quan trọng của bộ lọc rủi ro.
2. **Lập trình `src/lab13.py`:**
   - Viết hàm `co_mau()` tính toán cỡ mẫu cho Nhiệm vụ D1 bằng phân phối chuẩn `NormalDist` và in ra kết quả cho các kịch bản a, b, c, d, e.
   - Chạy kiểm tra code và đảm bảo script in kết quả thông suốt, không có lỗi.
3. **Hoàn thiện `report/team/pilot_plan.yaml`:**
   - Tính toán và điền cỡ mẫu $1.251$ yêu cầu/nhóm cho MDE $+5\%$ ($\alpha=0,05, \text{power}=0,8$).
   - Trình bày 5 câu kiểm tra tính tách biệt tác động, nêu rõ đánh đổi chọn đơn vị yêu cầu (`unit: request`) thay vì cụm để đảm bảo đủ công suất.
   - Thiết lập 3 luật dừng chuẩn cú pháp `NẾU – TRONG – THÌ – KHÔNG THÌ` và kịch bản rollback trong 5 phút.

## 4. Bằng chứng

- **Files chỉnh sửa & đóng góp:**
  - `src/lab13.py`: Thêm code D1 (`co_mau`, tính toán kích thước mẫu a–e).
  - `report/team/bang_chi_phi.md`: Điền toàn bộ các bảng và câu trả lời A1–A4, B1–B4.
  - `report/team/pilot_plan.yaml`: Điền toàn bộ cấu hình pilot, kiểm tra cú pháp YAML hợp lệ, không còn dấu `?`.
- **Git Commits:**
  - Commit bổ sung `bang_chi_phi.md`, `pilot_plan.yaml` và code `lab13.py` under author `Lê Thanh Tùng <lethanhtung6803@gmail.com>`.

## 5. Công cụ AI đã dùng

- Dùng AI hỗ trợ giải nhanh công thức cỡ mẫu hai mẫu tỉ lệ độc lập và thiết kế kịch bản nhạy cảm.
- Kiểm tra lại toàn bộ bằng cách chạy trực tiếp trên file dữ liệu giả lập `logix_runs.csv` và `logix_requests.csv` qua Python để đảm bảo số liệu khớp $100\%$ không sai lệch.

## 6. Tự đánh giá

- Hoàn thành đầy đủ, chính xác và kịp thời các nhiệm vụ được giao theo bảng phân công nhóm.
- Tuân thủ chặt chẽ các nguyên tắc: không dùng từ cấm, nhãn `[simulated]` đầy đủ, câu trả lời súc tích dưới 3 dòng có kèm số liệu chứng minh.
