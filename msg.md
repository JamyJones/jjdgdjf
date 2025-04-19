Why do i get a white image without contents
int mupdf_gen_page(const char* name_pdf,int page_number){
  float zoom=10.0f,rotate=0.0f;
  int width,height, page_count;
  fz_context *ctx;
  fz_document *doc;
  fz_pixmap *pix;
  fz_matrix ctm;
  

  ctx =fz_new_context(NULL, NULL, FZ_STORE_UNLIMITED);
  if(!ctx){
    std::cerr << "couldn't create mupdf context"<< "\n";
    return EXIT_FAILURE;
  }
  try{
    fz_register_document_handlers(ctx);
  }
  catch (const std::runtime_error &err)
  {
    std::cerr << err.what() << "\n";
		fz_drop_context(ctx);
		return EXIT_FAILURE;
  }
  try{
		doc = fz_open_document(ctx, name_pdf);
  }
	
catch (const std::runtime_error &err)
	{
    std::cerr<<err.what()<<"\n";
		fz_drop_context(ctx);
		return EXIT_FAILURE;
	}

	/* Compute a transformation matrix for the zoom and rotation desired. */
	/* The default resolution without scaling is 72 dpi. */
	ctm = fz_scale(zoom / 100, zoom / 100);
	ctm = fz_pre_rotate(ctm, rotate);

  try{
		pix = fz_new_pixmap_from_page_number(ctx, doc, page_number, ctm, fz_device_rgb(ctx), 0);
  }
	catch (const std::runtime_error &err)
	{
    std::cerr << err.what() << "\n";
		fz_drop_document(ctx, doc);
		fz_drop_context(ctx);
		return EXIT_FAILURE;
	}
  unsigned char* data = fz_pixmap_samples(ctx,pix);
  width=pix->w;
  height=pix->h;
  std::ostringstream oss;
  oss<<"/storage/emulated/0/.Apps/ReadEra/images/page"<<page_number<<".png";
  std::string out_name_str=oss.str();
  const char* output_page_name = out_name_str.c_str();

 SaveBitmapAsPNG(data, output_page_name,width,height);
fz_drop_pixmap(ctx, pix);
	fz_drop_document(ctx, doc);
	fz_drop_context(ctx);
	return EXIT_SUCCESS;

}