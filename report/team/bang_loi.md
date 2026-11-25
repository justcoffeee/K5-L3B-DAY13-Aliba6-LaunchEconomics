# Bảng lỗi và cách khắc phục · Nhiệm vụ C

Nguồn: mục “Hai mươi ca lỗi” trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Phân loại theo nguyên nhân gốc với năm loại: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**.

## Hai bộ nhãn

Người gắn nhãn 1: Cấn Xuân Nghĩa · Người gắn nhãn 2: Nguyễn Mạnh Hùng (đã rà soát và thống nhất).

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = **100%** (đạt ngưỡng ≥ 80%).

## Căn cứ phân loại và quy tắc phân biệt

Cả 20 ca đều thống nhất theo nguyên nhân gốc. Căn cứ phân loại từng ca và quy tắc phân biệt cho các cặp dễ nhầm:

| Ca | Căn cứ từ mô tả |
| --: | --- |
| 1 | Khách nhập thiếu hai chữ số tài khoản; lỗi đầu vào là nguyên nhân gốc, dù hệ thống cũng cần bổ sung kiểm tra. |
| 2 | Có đủ thông tin kiện 28 kg nhưng trợ lý truyền sai loại hàng cho tool, dẫn đến hoàn thiếu 45.000 đ. |
| 3 | Hoàn về ví trong 5 phút đúng thiết kế, nhưng khách kỳ vọng tiền về ngân hàng: lệch kỳ vọng về nơi nhận. |
| 4 | Thiếu dữ liệu chặng của hãng nước ngoài; trợ lý nêu giới hạn và chuyển nhân viên. |
| 5 | Hoàn thừa trung bình 12.000 đ ở 14 đơn; khách và hệ thống không nhận ra, chỉ kiểm tra mẫu mới phát hiện. |
| 6 | Khách chọn nhầm lý do giao trễ trong khi hàng bị vỡ; cần sửa đầu vào và xác nhận lại lý do. |
| 7 | Sổ cái trả lỗi 503 nhưng trợ lý báo thành công sau 3 lần thử: báo sai trạng thái thực thi. |
| 8 | Viện dẫn điều 7.2 không tồn tại là thông tin sai của hệ thống, dù số tiền đúng. |
| 9 | Khách nhập mã sàn thay vì mã vận đơn; thiếu hướng dẫn sửa là vấn đề cần khắc phục thêm, không đổi nguyên nhân gốc. |
| 10 | Từ chối do bão đúng chính sách, nhưng thông điệp “cam kết giao 24 giờ” tạo kỳ vọng khác cho khách. |
| 11 | Tin nhắn thoại nằm ngoài dạng đầu vào trợ lý xử lý được; không phải tính toán sai. |
| 12 | Kết quả cuối vẫn đúng nhưng token D05 tăng gấp 3 trong 3 tuần mà không ai phát hiện: chi phí bất thường bị che khuất. |
| 13 | Bảo hiểm đối tác ngoài phạm vi xử lý; cần nói rõ giới hạn và chuyển đúng đầu mối thay vì trả lời chung chung. |
| 14 | Khách bấm nhầm xác nhận đã nhận tiền; cần cơ chế xác nhận lại hoặc mở lại. |
| 15 | Chính sách yêu cầu hoàn 50% cho trễ 26 giờ nhưng trợ lý tính 100%; nhân viên đã phát hiện sai sót. |
| 16 | Gửi ngay lúc 2:14 sáng đúng thiết kế, nhưng không phù hợp giờ nghỉ và hoàn cảnh nhận thông báo. |
| 17 | Cache bảng giá cũ làm lệch 212 đơn trong 9 ngày; không ai mở lại, lỗi tồn tại mà chưa được nhận biết. |
| 18 | Hoàn 15.000 đ từ phí 30.000 đ × 50% đúng, nhưng thiếu giải thích khiến khách hiểu là thiếu tiền. |
| 19 | Đơn 14 tháng vượt cửa sổ dữ liệu 12 tháng; trợ lý nói rõ giới hạn và chuyển kèm tóm tắt. |
| 20 | Yêu cầu gửi lại chỉ là tác nhân; thiếu khoá chống trùng làm hệ thống hoàn hai lần cho cùng một đơn. |

- **Hệ thống / Ngầm:** sai số đã lộ trong xử lý hoặc bị nhân viên/khách bắt là Hệ thống; bất thường không được khách và hệ thống nhận ra là Ngầm (ca 5, 12, 17).
- **Ngữ cảnh / Hệ thống:** làm đúng chính sách, phép tính hoặc thiết kế nhưng lệch kỳ vọng/hoàn cảnh là Ngữ cảnh (ca 3, 10, 16, 18); làm sai chính sách hay trạng thái thực thi là Hệ thống.
- **Giới hạn / Hệ thống:** thiếu dữ liệu, ngoài phạm vi hoặc không hỗ trợ dạng đầu vào là Giới hạn hệ thống; đã có đủ khả năng và dữ liệu nhưng thực hiện sai là Hệ thống.
- **Do người dùng / Hệ thống:** phân loại từ nhập/chọn nhầm ban đầu ở ca 1, 6, 9, 14; ở ca 20, chống hoàn trùng là trách nhiệm hệ thống nên không quy lỗi cho việc khách gửi lại.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Các event bổ sung, thuộc tính và ngưỡng dưới đây là **đề xuất giám sát cho pilot**, chưa phải log đã triển khai hay kết quả đã đo. Mỗi event gắn `trace_id`, `request_id` để nối với trace và các event trong `chi_so.md`.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Trước mỗi lệnh hoàn, kiểm tra định dạng/độ dài tài khoản theo ngân hàng; ghi `refund_account_validation` với bank_code, valid, reason. Chặn nếu valid = false; tổng hợp số lần không hợp lệ mỗi ngày. | Yêu cầu nhập lại và xác nhận phần tài khoản đã che trước khi gửi; hướng dẫn rõ trường sai, không ghi nguyên số tài khoản vào log. Nếu ngân hàng từ chối thì giữ trạng thái chưa hoàn và chuyển nhân viên. | Trưởng nhóm phát triển ứng dụng |
| 20 | Hệ thống | Đối soát mỗi lệnh `refund_ledger_write` theo mã đơn + loại phí + phiên bản quyết định hoàn. Có từ 2 bút toán thành công cho cùng một nghĩa vụ hoàn thì cảnh báo ngay; rà soát toàn bộ bút toán hằng ngày. | Tạo `idempotency_key` ổn định, ràng buộc duy nhất và kiểm tra nguyên tử tại sổ cái; request gửi lại trả về trạng thái giao dịch cũ. Khoá hoàn tự động của đơn khi phát hiện trùng và chuyển kế toán đối soát. | Trưởng nhóm kỹ thuật thanh toán |
| 3 | Ngữ cảnh | Ghi `refund_destination_acknowledged` trước xác nhận, gồm destination và acknowledged; không gửi lệnh khi acknowledged = false. Theo dõi hằng tuần `ticket_reopened` có reason = nham_noi_nhan; từ 1 ca/tuần thì rà nội dung hướng dẫn. | Hiển thị rõ “hoàn về ví LogiX trong 5 phút” trước xác nhận và trong thông báo hoàn; cho khách xác nhận nơi nhận, nêu cách dùng/rút tiền theo chính sách hiện hành. | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Kiểm tra tuổi đơn ở mọi yêu cầu; nếu trên 12 tháng thì ghi `handoff_to_staff` với reason = ngoai_cua_so_du_lieu, tuổi đơn và trace_id. Đối soát mỗi ngày: mọi ca bị giới hạn phải có bản ghi chuyển nhân viên. | Thông báo rõ chỉ tra được 12 tháng, không tự suy đoán hay từ chối quyền lợi; chuyển kèm mã đơn và tóm tắt cho nhân viên có quyền tra kho lưu trữ. | Trưởng nhóm vận hành CSKH |
| 17 | Ngầm | Ghi policy_version, effective_date và so_tien_dung trong `audit_sample_checked`; so phiên bản cache với bảng giá hiệu lực trước mỗi phép tính. Chặn ngay nếu sai phiên bản; kiểm tra mẫu 100 đơn/tuần, từ 1 đơn lệch tiền thì mở điều tra. | Vô hiệu cache khi bảng giá đổi, đưa phiên bản chính sách vào khoá cache và lưu phiên bản trên giao dịch. Đối soát toàn bộ 212 đơn trong 9 ngày của ca mẫu, xác định số tiền lệch từng đơn và chuyển kế toán điều chỉnh theo quy trình. | Trưởng nhóm dữ liệu và chính sách |
