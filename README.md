1. Trạng thái bài toán: Gọi (r, c) là toạ độ của các “ô” được di chuyển tới trong mê cung (maze) được mô tả bằng một ma trận 10x10. r là chỉ số dòng, c là chỉ số cột trong ma trận.
2. Trạng thái khởi đầu: (0, 0)
3. Trạng thái kết thúc: (9, 9)
4. Các luật di chuyển: Mỗi lần ta được di chuyển qua một ô liền kề: lên, xuống, trái, phải, không được di chuyển chéo, tức là: (r c) = (r c) + m với m ∈ {(-1 0), (0 1), (0 -1), (1 0)}
5. Hàm lượng giá:
    g: khoảng cách từ trạng thái khởi đầu đến trạng thái đang xét. Quy ước mỗi lần di chuyển sang một ô thì g = g + 1.
    h: khoảng cách từ trạng thái đang xét đến trạng thái kết thúc (trạng thái đích). Giả sử với trạng thái đích là (9, 9), trạng thái đang xét là (4, 3) thì h2 = (9 - 4)2 + (9 - 3)2 = 25 + 9 = 34.
    F = g + h.



