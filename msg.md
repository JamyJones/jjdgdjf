fz_context *ctx = fz_new_context(NULL, NULL, FZ_STORE_UNLIMITED);
fz_colorspace *cs = fz_device_rgb(ctx);
fz_irect bbox = {0, 0, 500, 500}; // Defines a 500x500 pixel area
fz_pixmap *pixmap = fz_new_pixmap_with_bbox(ctx, cs, bbox, NULL, 1);

If the bbox specified is too small to maybe be occupied by the all the pixels what happens to the pixmap