import cv2
import numpy as np
import os

class TemplateMatcher:
    def __init__(self, template_folder):
        self.templates = []
        for file in os.listdir(template_folder):
            path = os.path.join(template_folder, file)
            img = cv2.imread(path, 0)
            self.templates.append(img)

    def find(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        points = []

        for template in self.templates:
            res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= 0.7)

            for pt in zip(*loc[::-1]):
                points.append(pt)

        return self.filter_points(points)

    def filter_points(self, points, min_dist=25):
        filtered = []
        for p in points:
            if all(abs(p[0]-fp[0])>min_dist or abs(p[1]-fp[1])>min_dist for fp in filtered):
                filtered.append(p)
        return filtered