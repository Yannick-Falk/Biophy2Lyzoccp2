import cv2
import numpy as np
import matplotlib.pyplot as plt

# Bild laden
image_path = '/Spektrum.png'
image = cv2.imread(image_path)

# Bild in Graustufen umwandeln
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Kanten im Bild erkennen
edges = cv2.Canny(gray, 50, 150)

# Konturen finden
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Größte Kontur finden (das ist wahrscheinlich der Graph)
largest_contour = max(contours, key=cv2.contourArea)

# Bounding Box um die größte Kontur
x, y, w, h = cv2.boundingRect(largest_contour)

# Bereich des Graphen extrahieren
graph_roi = gray[y:y+h, x:x+w]

# Konturen im Bereich des Graphen finden
graph_contours, _ = cv2.findContours(graph_roi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Größte Kontur im Bereich des Graphen finden (das ist die Linie des Graphen)
graph_line_contour = max(graph_contours, key=cv2.contourArea)

# Koordinaten der Punkte auf der Linie extrahieren
graph_points = graph_line_contour[:, 0, :]

# Plot der extrahierten Punkte
plt.figure(figsize=(10, 5))
plt.imshow(gray, cmap='gray')
plt.plot(graph_points[:, 0] + x, graph_points[:, 1] + y, color='red')
plt.title('Extracted Graph Line')
plt.show()

# Zurückgeben der extrahierten Punkte für die weitere Verarbeitung
graph_points, (x, y, w, h)
