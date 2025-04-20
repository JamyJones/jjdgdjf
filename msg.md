float max_dimension = fz_max(page_bounds.x1 - page_bounds.x0, page_bounds.y1 - page_bounds.y0);
float desired_size = 500.0; // Example: fit within 500 pixels
float scale = desired_size / max_dimension;
fz_matrix transform = fz_scale(scale, scale);
Why the image has no height after scaling