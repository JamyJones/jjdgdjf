Show me how ti render a page in pdfium
#if defined(PDF_USE_SKIA)
// Experimental API.
// Function: FPDF_RenderPageSkia
//          Render contents of a page to a Skia SkCanvas.
// Parameters:
//          canvas      -   SkCanvas to render to.
//          page        -   Handle to the page.
//          size_x      -   Horizontal size (in pixels) for displaying the page.
//          size_y      -   Vertical size (in pixels) for displaying the page.
// Return value:
//          None.
FPDF_EXPORT void FPDF_CALLCONV FPDF_RenderPageSkia(FPDF_SKIA_CANVAS canvas,
                                                   FPDF_PAGE page,
                                                   int size_x,
                                                   int size_y);
#endif