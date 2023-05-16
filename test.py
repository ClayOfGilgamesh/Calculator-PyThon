from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

app = QApplication([])
window = QWidget()

layout = QVBoxLayout()

label = QLabel("Đây là một chuỗi văn bản dài hơn chiều dài của label và chúng ta sẽ thử sử dụng thuộc tính setWordWrap để cho phép label tự động xuống hàng.")

#label.setWordWrap(True)

layout.addWidget(label)
window.setLayout(layout)
window.show()
app.exec_()
