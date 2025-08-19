import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QPen
from rectangle_drawer import RectangleDrawer

class DrawingCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600, 400)
        self.canvas_image = QPixmap(600, 400)
        self.canvas_image.fill(Qt.white)
        self.rectangle_drawer = RectangleDrawer(self)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.canvas_image)
        # 미리보기 그리기
        self.rectangle_drawer.draw_preview(painter)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.rectangle_drawer.start_drawing(event.x(), event.y())
            
    def mouseMoveEvent(self, event):
        self.rectangle_drawer.update_drawing(event.x(), event.y())
        self.update()
        
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.rectangle_drawer.finish_drawing()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("간단한 그림 그리기")
        self.setGeometry(100, 100, 800, 600)
        
        # 메인 위젯 설정
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # 레이아웃 생성
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        
        # 캔버스 생성
        self.canvas = DrawingCanvas()
        layout.addWidget(self.canvas)
        
        # 사각형 버튼 추가
        self.rect_btn = QPushButton("사각형 그리기 모드")
        layout.addWidget(self.rect_btn)
        
        # 기본 버튼
        self.clear_btn = QPushButton("지우기")
        self.clear_btn.clicked.connect(self.clear_canvas)
        layout.addWidget(self.clear_btn)
        
    def clear_canvas(self):
        self.canvas.canvas_image.fill(Qt.white)
        self.canvas.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())