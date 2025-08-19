from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
import math

class CircleDrawer:
    def __init__(self, canvas_widget):
        self.canvas = canvas_widget
        self.is_drawing = False
        self.center_x = 0
        self.center_y = 0
        self.current_x = 0
        self.current_y = 0
        
    def start_drawing(self, x, y):
        """원 그리기 시작"""
        self.is_drawing = True
        self.center_x = x
        self.center_y = y
        self.current_x = x
        self.current_y = y
        
    def update_drawing(self, x, y):
        """마우스 이동시 원 크기 업데이트"""
        if self.is_drawing:
            self.current_x = x
            self.current_y = y
            
    def finish_drawing(self):
        """원 그리기 완료"""
        if self.is_drawing:
            painter = QPainter(self.canvas.canvas_image)
            pen = QPen(Qt.blue, 2)
            painter.setPen(pen)
            
            # 반지름 계산
            radius = self.get_radius()
            
            # 원 그리기
            painter.drawEllipse(
                self.center_x - radius, 
                self.center_y - radius, 
                radius * 2, 
                radius * 2
            )
            
            painter.end()
            self.canvas.update()
            self.is_drawing = False
            
    def get_radius(self):
        """중심점에서 현재 마우스 위치까지의 거리 계산"""
        dx = self.current_x - self.center_x
        dy = self.current_y - self.center_y
        return int(math.sqrt(dx * dx + dy * dy))
            
    def draw_preview(self, painter):
        """그리는 중 미리보기"""
        if self.is_drawing:
            pen = QPen(Qt.green, 1, Qt.DashLine)
            painter.setPen(pen)
            radius = self.get_radius()
            painter.drawEllipse(
                self.center_x - radius, 
                self.center_y - radius, 
                radius * 2, 
                radius * 2
            )