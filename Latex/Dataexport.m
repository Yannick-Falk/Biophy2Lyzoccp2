% Load image
image = imread('Spektrum.png');

% Convert image to grayscale
gray = rgb2gray(image);

% Detect edges in the grayscale image
edges = edge(gray, 'Canny');

% Find boundaries (contours) in the edge-detected image
[B, L] = bwboundaries(edges, 'noholes');

% Find the largest boundary (assumed to be the graph)
max_boundary = max(cellfun(@length, B));
graph_contour = B{find(cellfun(@length, B) == max_boundary)};

% Define axis ranges for conversion
x_min = 251.138;
x_max = 700.448;
y_min = -0.1;
y_max = 0.8;

% Get image dimensions
[height, width] = size(gray);

% Calculate scaling factors
x_scale = (x_max - x_min) / width;
y_scale = (y_max - y_min) / height;

% Convert pixel coordinates to numerical values
graph_x = x_min + graph_contour(:,2) * x_scale;
graph_y = y_max - (graph_contour(:,1) * y_scale); % Invert y-values

% Display and plot extracted graph
figure;
plot(graph_x, graph_y, 'b', 'LineWidth', 2);
hold on;

% Plot function a*x^4
a = 9.276e-11;
x_vals = linspace(min(graph_x), max(graph_x), 100);
y_vals = a * x_vals.^4;
plot(x_vals, y_vals, 'r--', 'LineWidth', 2);

xlabel('Wavelength/Lambda (nm)');
ylabel('Absorption');
title('Graph with a*x^4 Overlay');
legend('Extracted Graph', 'a \cdot x^4', 'Location', 'best');
grid on;
