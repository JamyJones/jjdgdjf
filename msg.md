How do i fix
ld.lld: error: undefined symbol: crc32
 >>> referenced by zip.c
 >>>               zip.o:(fz_write_zip_entry) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by zip.c
 >>>               zip.o:(fz_write_zip_entry) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by output-png.c
 >>>               output-png.o:(png_write_header) in archive /data/data/com.termux/files/usr/lib/libmupdf.a                         >>> referenced 11 more times

 ld.lld: error: undefined symbol: FT_Set_Charmap
 >>> referenced by xps-glyphs.c
 >>>               xps-glyphs.o:(xps_select_font_encoding) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by xps-glyphs.c                                    >>>               xps-glyphs.o:(xps_lookup_font) in archive /data/data/com.termux/files/usr/lib/libmupdf.a                          >>> referenced by pdf-font.c
 >>>               pdf-font.o:(pdf_load_simple_font) in archive /data/data/com.termux/files/usr/lib/libmupdf.a                      
 ld.lld: error: undefined symbol: FT_Get_Char_Index                >>> referenced by xps-glyphs.c
 >>>               xps-glyphs.o:(xps_encode_font_char) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by xps-glyphs.c
 >>>               xps-glyphs.o:(xps_encode_font_char) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by xps-glyphs.c
 >>>               xps-glyphs.o:(xps_parse_glyphs_imp) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced 35 more times

 ld.lld: error: undefined symbol: FT_Get_Advance
 >>> referenced by xps-glyphs.c
 >>>               xps-glyphs.o:(xps_measure_font_glyph) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by xps-glyphs.c
 >>>               xps-glyphs.o:(xps_measure_font_glyph) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by xps-glyphs.c
 >>>               xps-glyphs.o:(xps_parse_glyphs_imp) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced 4 more times

 ld.lld: error: undefined symbol: hb_buffer_destroy
 >>> referenced by html-layout.c
 >>>               html-layout.o:(fz_layout_html) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by html-layout.c
 >>>               html-layout.o:(fz_draw_html) in archive /data/data/com.termux/files/usr/lib/libmupdf.a

 ld.lld: error: undefined symbol: hb_buffer_create
 >>> referenced by html-layout.c
 >>>               html-layout.o:(fz_layout_html) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by html-layout.c
 >>>               html-layout.o:(fz_draw_html) in archive /data/data/com.termux/files/usr/lib/libmupdf.a

 ld.lld: error: undefined symbol: FT_Set_Char_Size
 >>> referenced by html-layout.c
 >>>               html-layout.o:(walk_string) in archive /data/data/com.termux/files/usr/lib/libmupdf.a