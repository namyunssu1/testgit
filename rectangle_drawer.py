from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen

class RectangleDrawer:
    def __init__(self, canvas_widget):
        self.canvas = canvas_widget
        self.is_drawing = False
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        
    def start_drawing(self, x, y):
        """사각형 그리기 시작"""
        self.is_drawing = True
        self.start_x = x
        self.start_y = y
        self.end_x = x
        self.end_y = y
        
    def update_drawing(self, x, y):
        """마우스 이동시 사각형 크기 업데이트"""
        if self.is_drawing:
            self.end_x = x
            self.end_y = y
            
    def finish_drawing(self):
        """사각형 그리기 완료"""
        if self.is_drawing:
            painter = QPainter(self.canvas.canvas_image)
            pen = QPen(Qt.black, 2)
            painter.setPen(pen)
            
            # 사각형 그리기
            width = self.end_x - self.start_x
            height = self.end_y - self.start_y
            painter.drawRect(self.start_x, self.start_y, width, height)
            
            painter.end()
            self.canvas.update()
            self.is_drawing = False
            
    def draw_preview(self, painter):
        """그리는 중 미리보기"""
        if self.is_drawing:
            pen = QPen(Qt.red, 1, Qt.DashLine)
            painter.setPen(pen)
            width = self.end_x - self.start_x
            height = self.end_y - self.start_y
            painter.drawRect(self.start_x, self.start_y, width, height)