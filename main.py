import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QPen
from rectangle_drawer import RectangleDrawer
from circle_drawer import CircleDrawer

class DrawingCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600, 400)
        self.canvas_image = QPixmap(600, 400)
        self.canvas_image.fill(Qt.white)
        
        # 두 그리기 모드 초기화
        self.rectangle_drawer = RectangleDrawer(self)
        self.circle_drawer = CircleDrawer(self)
        self.current_mode = "rectangle"  # 기본 모드
        
    def set_mode(self, mode):
        """그리기 모드 변경"""
        self.current_mode = mode
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.canvas_image)
        
        # 현재 모드에 따라 미리보기 그리기
        if self.current_mode == "rectangle":
            self.rectangle_drawer.draw_preview(painter)
        elif self.current_mode == "circle":
            self.circle_drawer.draw_preview(painter)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.current_mode == "rectangle":
                self.rectangle_drawer.start_drawing(event.x(), event.y())
            elif self.current_mode == "circle":
                self.circle_drawer.start_drawing(event.x(), event.y())
            
    def mouseMoveEvent(self, event):
        if self.current_mode == "rectangle":
            self.rectangle_drawer.update_drawing(event.x(), event.y())
        elif self.current_mode == "circle":
            self.circle_drawer.update_drawing(event.x(), event.y())
        self.update()
        
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.current_mode == "rectangle":
                self.rectangle_drawer.finish_drawing()
            elif self.current_mode == "circle":
                self.circle_drawer.finish_drawing()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("통합된 그림 그리기 - 사각형 & 원")
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
        
        # 버튼 레이아웃
        button_layout = QHBoxLayout()
        
        # 모드 선택 버튼들
        self.rect_btn = QPushButton("사각형 모드")
        self.rect_btn.clicked.connect(lambda: self.set_mode("rectangle"))
        button_layout.addWidget(self.rect_btn)
        
        self.circle_btn = QPushButton("원 모드")
        self.circle_btn.clicked.connect(lambda: self.set_mode("circle"))
        button_layout.addWidget(self.circle_btn)
        
        # 지우기 버튼
        self.clear_btn = QPushButton("지우기")
        self.clear_btn.clicked.connect(self.clear_canvas)
        button_layout.addWidget(self.clear_btn)
        
        layout.addLayout(button_layout)
        
        # 기본 모드 표시
        self.set_mode("rectangle")
        
    def set_mode(self, mode):
        """그리기 모드 변경 및 버튼 상태 업데이트"""
        self.canvas.set_mode(mode)
        
        # 버튼 스타일 업데이트
        if mode == "rectangle":
            self.rect_btn.setStyleSheet("background-color: lightblue;")
            self.circle_btn.setStyleSheet("")
        elif mode == "circle":
            self.circle_btn.setStyleSheet("background-color: lightgreen;")
            self.rect_btn.setStyleSheet("")
        
    def clear_canvas(self):
        """캔버스 지우기"""
        self.canvas.canvas_image.fill(Qt.white)
        self.canvas.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())