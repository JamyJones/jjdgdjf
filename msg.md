fz_rect page_bounds = fz_bound_page(doc, page);
float scale_x = (page_bounds.x1 - page_bounds.x0);
float scale_y = (page_bounds.y1 - page_bounds.y0);
fz_matrix transform = fz_scale(scale_x, scale_y);

Why how can i scale with the same factor along the width and height such that they adjust accordingly