"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        # Phân phối hình học: trung bình 1/p lần chạy đến lần đúng đầu tiên.
        return 1 / p
    # Lần chạy thứ i xảy ra khi i-1 lần trước đều sai: tổng (1-p)^(i-1), i=1..k.
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    # Chỉ thất bại khi cả k lần đều sai.
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # Tử số: mọi lần chạy (kể cả lần sai); mẫu số: chỉ yêu cầu thành công.
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    # Chỉ giữ các lần chạy thuộc nhóm yêu cầu đang xét (để A3 gọi lại theo từng loại).
    runs = runs[runs['request_id'].isin(reqs['request_id'])]

    if max_lan_chay is not None:
        # B1, B3: bỏ các lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi như chuyển nhân viên,
        # khi đó không còn phút xem lại / làm lại của trợ lý.
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    # Tử số: MỌI lần chạy, kể cả lần lỗi. Giá token tính cho 1.000 token.
    tien_moi_lan = (runs['tokens_in'] / 1000 * gia_vao
                    + runs['tokens_out'] / 1000 * gia_ra
                    + runs['tool_calls'] * gia_tool)
    token = (runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra).sum()
    tool = (runs['tool_calls'] * gia_tool).sum()
    chay_lai = tien_moi_lan[runs['attempt'] > 1].sum()   # phần của lần chạy thứ 2 và 3

    # Giờ nhân viên — số GIẢ LẬP (simulated).
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai

    tong = token + tool + xem_lai + lam_lai
    # Mẫu số: chỉ yêu cầu thành công.
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=token, tool=tool, chay_lai=chay_lai,
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(token + tool) / len(reqs))


# ---------- Nhiệm vụ A3 · Tách theo loại yêu cầu ----------
def bang_theo_loai(runs, reqs):
    """Mỗi loại một dòng: số yêu cầu, tỉ lệ thành công, số lần chạy mỗi yêu cầu,
    chi phí mỗi việc thành công (simulated) và bội số so với BASELINE."""
    dong = []
    for loai, nhom in reqs.groupby('loai', sort=False):
        kq = mo_hinh(runs, nhom)
        so_lan = runs['request_id'].isin(nhom['request_id']).sum()
        dong.append(dict(loai=loai, so_yc=len(nhom),
                         ti_le_tc=kq['thanh_cong'] / len(nhom),
                         lan_chay_moi_yc=so_lan / len(nhom),
                         cps=kq['cps'], so_voi_baseline=kq['cps'] / BASELINE))
    thu_tu = ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']
    return pd.DataFrame(dong).set_index('loai').reindex(thu_tu)


def ti_le_ok_theo_lan_thu(runs, reqs):
    """Tỉ lệ status == 'ok' theo loại × attempt: chạy lại có giúp không?"""
    gop = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    gop['ok'] = (gop['status'] == 'ok').astype(float)
    return gop.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    print('\nA3 · Theo loại yêu cầu (chi phí mỗi việc thành công là simulated)')
    print(f"{'loai':10s} {'so_yc':>6s} {'ti_le_tc':>9s} {'lan/yc':>7s} {'cps':>8s} {'x12000':>7s}")
    for loai, d in bang_theo_loai(runs, reqs).iterrows():
        print(f"{loai:10s} {d.so_yc:6.0f} {d.ti_le_tc:9.1%} {d.lan_chay_moi_yc:7.2f} "
              f"{d.cps:8,.0f} {d.so_voi_baseline:6.2f}x")
    print('\nTỉ lệ ok theo lần thử (attempt)')
    print(ti_le_ok_theo_lan_thu(runs, reqs).round(3).to_string())
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
