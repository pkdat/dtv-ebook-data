# Crawl dữ liệu dtv-ebook.com.vn
Mỗi trang dạng https://dtv-ebook.com.vn/sach-truyen-ebook-313/230.html#gsc.tab=0 liệt kê thông tin về 12 quyển sách.

Lặp lần lượt từng trang để lấy dữ liệu.
```python
for i in range(230, 1000): # Lấy từ trang 230 đến trang 999
    url = f'https://dtv-ebook.com.vn/sach-truyen-ebook-313/{i}.html#gsc.tab=0'
```
Hàm `get_details_urls` trả về các link đến trang thông tin chi tiết.
```python
def get_detail_urls(list_url):
    ...
    return detail_urls # 12 urls
```

Hàm `get_data` lấy dữ liệu của từng trang.
```python
def get_data(detail_url):
    ...
```
Dữ liệu sẽ được lưu vào `dtv-ebook.db` đồng thời được in ra.
```commandline
Error: 230 UNIQUE constraint failed: books.url https://dtv-ebook.com.vn/nhat-mau_17971.html
Error: 230 UNIQUE constraint failed: books.url https://dtv-ebook.com.vn/moi-sung-than-thuong_17970.html
Error: 230 UNIQUE constraint failed: books.url https://dtv-ebook.com.vn/mieu-me-tran-tuyen-lien-manh_17969.html
230 ('https://dtv-ebook.com.vn/le-sinh-diet-ly-tu-hanh_17968.html', 'Lẽ Sinh Diệt Lý Tu Hành', '', 'Ajahn Chah', 'Tôn giáo - Thiền', 'Hoàn Thành', 'eBook, mobi, pdf, epub, azw3', '3255', 'eBook, mobi, pdf, epub, azw3, full, Ajahn Chah, Tôn Giáo, Phật Giáo', 'https://docs.google.com/uc?id=19BiUZVigIldQBT5_R24zk3HtOJvBZ8XN', 'https://docs.google.com/uc?id=1bZCoJ7mX-od3jOqiAcywh_AvNvZsVCJ7', 'https://docs.google.com/uc?id=1jAOOmqtTYEvUF4kG1WOF6UaxKd54r2Cx', 'https://docs.google.com/uc?id=1HVodPMnHbiOaPhEV_371X1Hksq1TfAS_')
230 ('https://dtv-ebook.com.vn/hoa-phung-hoang_17967.html', 'Hỏa Phụng Hoàng', '', 'Minh Nguyệt Vô Ưu', 'Đam Mỹ', 'Hoàn Thành', 'eBook, mobi, pdf, epub, azw3', '3698', 'eBook, mobi, pdf, epub, azw3, full, Minh Nguyệt Vô Ưu, Ngôn Tình, Đam Mỹ, Huyền Ảo, Công Sủng Thụ, Sư Đồ, Niên Thượng, Trọng Sinh, Ngược, H, HE, Văn học phương Đông', 'https://docs.google.com/uc?id=1dQtpA55iKtOzZcIXfdnI3cSHTECXWmR-', 'https://docs.google.com/uc?id=1b66dgVjj2syA3P1txcMfL4POOWtRGAVd', 'https://docs.google.com/uc?id=1WrbpcruCe6-1vRhSqKkJL8ONcpTWdPCl', 'https://docs.google.com/uc?id=1Ey2tCDPHSAOChJz4kJOxMAwLnnnUbCdk')
230 ('https://dtv-ebook.com.vn/ban-tinh-ca-nho_17966.html', 'Bản Tình Ca Nhỏ', '', 'Mạc Thanh Vũ', 'Đam Mỹ', 'Hoàn Thành', 'eBook, mobi, pdf, epub, azw3', '3132', 'eBook, mobi, pdf, epub, azw3, full, Mạc Thanh Vũ, Ngôn Tình, Đam Mỹ, Hiện Đại, Ấm Áp, Hiện Thực, Niên Thượng, 1×1, HE, Văn học phương Đông', 'https://docs.google.com/uc?id=1GNhXdEnab8_5UqtT8cwr8KBLh8HJkCf1', 'https://docs.google.com/uc?id=1iOmqzkT4gUinSESeb3Axcqp5m1vgFRf_', 'https://docs.google.com/uc?id=1waALy95krexlAeNlAVi9jydJ1TF8SCkG', 'https://docs.google.com/uc?id=10rE4ee-4p5fYR9LxCNmv1cGG-KHtlRft')
```
Lỗi `Error: 230 UNIQUE constraint failed: books.url ...` là dữ liệu ở trang đó đã được lưu trước đó.