# Báo cáo cá nhân — LeThanhTung-2A202603819

## 1. Thông tin thành viên

- Họ tên: Lê Thanh Tùng
- MSSV: 2A202603819
- Email: lethanhtung6803@gmail.com
- GitHub: [griin-03](https://github.com/griin-03)
- Vai trong nhóm: Người kiểm số và `bang_chi_phi.md` (trước giải lao) → người viết code D1 và hoàn thiện `pilot_plan.yaml` (sau giải lao)

## 2. Phần việc phụ trách

- **Trước giải lao:** Kiểm tra, đối chiếu tính toán toàn bộ số liệu tài chính từ Nhiệm vụ A (A1, A2, A3, A4) và B (B1, B2, B3, B4); hoàn thiện bảng chi phí `report/team/bang_chi_phi.md` với đầy đủ nhãn `[simulated]` và độ dài mỗi câu trả lời $\le 3$ dòng có số liệu chứng minh.
- **Sau giải lao:** Viết code tính cỡ mẫu Nhiệm vụ D1 (`co_mau`, tính toán kích thước mẫu cho các kịch bản a, b, c, d, e) trong `src/lab13.py`; cùng nhóm rà soát thiết kế pilot, phân tích tính khả thi của các cách chia (yêu cầu vs. cụm nhân viên/depot) và hoàn thiện `report/team/pilot_plan.yaml`.

## 3. Đóng góp cụ thể

1. **Kiểm số và hoàn thiện `report/team/bang_chi_phi.md`:**
   - **A1:** Xác thực 3 phép thử đáp án biết trước ($1,20$; $1,25$; $1,25$).
   - **A2:** Kiểm số tổng chi phí $4.373.585$ đ [simulated], chi phí mỗi việc thành công $4.472$ đ [simulated] (gấp $16,3$ lần hóa đơn token+tool mỗi yêu cầu $274,7$ đ), tỉ trọng giờ nhân viên chiếm $92,5\%$ (làm lại $51,8\%$, xem lại $40,7\%$).
   - **A3:** Xác thực phạm vi triển khai `noi_dia` ($2.696$ đ [simulated], $0,22\times$) và `hang_nang` ($8.221$ đ [simulated], $0,69\times$); loại bỏ `quoc_te` ($22.515$ đ [simulated], $1,88\times$) và `doi_tac` ($10.215$ đ [simulated], $0,85\times$).
   - **A4:** Xác thực chi phí cố định không làm đổi kết luận ở quy mô đầy đủ ($4.599$ đ [simulated], $0,38\times$) và nửa khối lượng ($5.784$ đ [simulated], $0,48\times$).
   - **B1 & B2:** Đo lường 9 kịch bản độ nhạy; kịch bản token $\times 2$ cùng xem lại $\times 2$ là $6.543$ đ [simulated] ($+46,3\%$). Xếp hạng 3 yếu tố nhạy nhất: Làm lại $\to$ Xem lại $\to$ Lương nhân viên.
   - **B3:** Xác định giới hạn chạy lại rẻ nhất cho toàn hệ thống là **2 lần** ($6.901.220$ đ [simulated]), không trùng với giới hạn CPS thấp nhất là 1 lần ($4.111$ đ [simulated]). Cột chi phí cả hệ thống và câu trả lời đều được gắn nhãn `[simulated]`.
   - **B4:** Đánh giá rủi ro xem lại 100% phạm vi pilot làm chi phí đội lên $11.743$ đ ($0,98\times$) đến $12.415$ đ ($1,03\times$), tính toán và chỉ ra điểm hoà vốn thời gian xem lại là $\le 5,1$ phút/yêu cầu (với 9 phút làm lại) và $\le 4,8$ phút/yêu cầu (với 15,3 phút làm lại).

2. **Lập trình Nhiệm vụ D1 trong `src/lab13.py`:**
   - Viết hàm `co_mau()` tính cỡ mẫu hai mẫu tỉ lệ độc lập bằng phân phối chuẩn `NormalDist`.
   - Tính toán và in kết quả kiểm tra cho cả 5 kịch bản a–e: chia theo yêu cầu ($1.251$), theo nhân viên $m=75$ ($\text{DE}=2,48 \to 3.103$ yêu cầu, cần $42$ NV/nhóm $\to 84 > 40$: không đủ), 20 NV/nhóm ($n_{\text{eff}} \le 1.000 < 1.251$), 6 depot/nhóm ($n_{\text{eff}} \le 300 < 1.251$), và mức chênh 6 điểm với 20 NV/nhóm ($m \ge 299$ yêu cầu/nhân viên, $\text{DE}=6,96$).

3. **Đóng góp kế hoạch pilot (`report/team/pilot_plan.yaml`):**
   - Phân tích đánh đổi giữa chia theo yêu cầu và chia theo cụm: nhóm thống nhất chuyển sang **chia theo nhân viên ($20 + 20$, `unit: staff`)** để đảm bảo tính tách biệt tác động (tránh can thiệp chéo spillover), chấp nhận MDE $0,06$ với $m \ge 299$ yêu cầu/nhân viên (nếu tác động thật là 5 điểm thì power còn khoảng $0,64$).
   - Xác định 4 luật dừng an toàn chuẩn cú pháp `NẾU – TRONG – THÌ – KHÔNG THÌ`, bao gồm việc kiểm soát tỉ lệ mở lại 7 ngày so với đối chứng (chênh $\ge 2$ điểm, trần tuyệt đối $6\%$), trần chi phí mỗi việc thành công $8.000$ đ, tỉ lệ bỏ qua gợi ý $\le 40\%$, và kiểm soát thời gian xem lại $\le 5$ phút (ngưỡng hoà vốn $5,1$ phút [simulated]).

## 4. Bằng chứng

- **Files chỉnh sửa & đóng góp:**
  - `src/lab13.py`: Viết code tính cỡ mẫu D1 (`co_mau`, kịch bản a–e).
  - `report/team/bang_chi_phi.md`: Điền toàn bộ các bảng và câu trả lời A1–A4, B1–B4 (chuẩn nhãn `[simulated]` tại B3, mức hoà vốn B4 $\le 5,1$ và $\le 4,8$ phút).
  - `report/team/pilot_plan.yaml`: Điền và cập nhật kế hoạch pilot theo cụm nhân viên ($20 + 20$).
  - `TEAM.md`: Cập nhật mục phân công và đóng góp cá nhân.
- **Git Commits:**
  - `e729b74`: feat(tung): complete bang_chi_phi.md, pilot_plan.yaml, D1 code and personal report
  - Commit cập nhật B3/B4 `bang_chi_phi.md`, điều chỉnh báo cáo cá nhân và `TEAM.md` under author `Lê Thanh Tùng <lethanhtung6803@gmail.com>`.

## 5. Công cụ AI đã dùng

- Dùng AI hỗ trợ giải nhanh công thức cỡ mẫu hai mẫu tỉ lệ độc lập với hệ số hiệu ứng thiết kế ($\text{DE} = 1 + (m-1)\rho$) và tính mức hoà vốn.
- Tự tay kiểm chứng toàn bộ công thức và số liệu bằng script Python trên tập dữ liệu mô phỏng, đảm bảo tính chuẩn xác và nhất quán $100\%$.

## 6. Tự đánh giá

- Hoàn thành đầy đủ, chính xác và kịp thời các nhiệm vụ được giao theo đúng phân vai của nhóm.
- Tuân thủ chặt chẽ các nguyên tắc: không dùng từ cấm, gắn nhãn `[simulated]` nghiêm ngặt, câu trả lời súc tích dưới 3 dòng có kèm số liệu chứng minh.
