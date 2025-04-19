Don't i have to render first before generating buffer because i need the page image
fz_context *ctx = fz_new_context(NULL, NULL, FZ_STORE_DEFAULT);
fz_document *doc = fz_open_document(ctx, "example.pdf");
fz_pixmap *pixmap = fz_new_pixmap_from_page_number(ctx, doc, 0, NULL, 0);
unsigned char *buffer = fz_pixmap_samples(ctx, pixmap);
int width = fz_pixmap_width(ctx, pixmap);
int height = fz_pixmap_height(ctx, pixmap);

printf("Buffer obtained: %p\nWidth: %d\nHeight: %d\n", buffer, width, height);