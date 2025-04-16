How can i fix
ld.lld: error: undefined symbol: jbig2_release_page
 >>> referenced by load-jbig2.c
 >>>               load-jbig2.o:(jbig2_read_image) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by load-jbig2.c
 >>>               load-jbig2.o:(jbig2_read_image) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by load-jbig2.c
 >>>               load-jbig2.o:(jbig2_read_image) in archive /data/data/com.termux/files/usr/lib/libmupdf.a                         >>> referenced 2 more times

 ld.lld: error: undefined symbol: jbig2_ctx_free
 >>> referenced by load-jbig2.c
 >>>               load-jbig2.o:(jbig2_read_image) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by filter-jbig2.c                                  >>>               filter-jbig2.o:(close_jbig2d) in archive /data/data/com.termux/files/usr/lib/libmupdf.a                          
 ld.lld: error: undefined symbol: jbig2_ctx_new_imp
 >>> referenced by load-jbig2.c                                    >>>               load-jbig2.o:(jbig2_read_image) in archive /data/data/com.termux/files/usr/lib/libmupdf.a                         >>> referenced by filter-jbig2.c                                  >>>               filter-jbig2.o:(fz_load_jbig2_globals) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by filter-jbig2.c
 >>>               filter-jbig2.o:(fz_open_jbig2d) in archive /data/data/com.termux/files/usr/lib/libmupdf.a

 ld.lld: error: undefined symbol: jbig2_data_in
 >>> referenced by load-jbig2.c
 >>>               load-jbig2.o:(jbig2_read_image) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by filter-jbig2.c
 >>>               filter-jbig2.o:(fz_load_jbig2_globals) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by filter-jbig2.c
 >>>               filter-jbig2.o:(next_jbig2d) in archive /data/data/com.termux/files/usr/lib/libmupdf.a

 ld.lld: error: undefined symbol: jbig2_complete_page
 >>> referenced by load-jbig2.c
 >>>               load-jbig2.o:(jbig2_read_image) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by filter-jbig2.c
 >>>               filter-jbig2.o:(next_jbig2d) in archive /data/data/com.termux/files/usr/lib/libmupdf.a

 ld.lld: error: undefined symbol: jbig2_page_out
 >>> referenced by load-jbig2.c
 >>>               load-jbig2.o:(jbig2_read_image) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by load-jbig2.c
 >>>               load-jbig2.o:(jbig2_read_image) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by load-jbig2.c
 >>>               load-jbig2.o:(jbig2_read_image) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced 4 more times

 ld.lld: error: undefined symbol: jpeg_std_error
 >>> referenced by load-jpeg.c
 >>>               load-jpeg.o:(fz_load_jpeg) in archive /data/data/com.termux/files/usr/lib/libmupdf.a
 >>> referenced by load-jpeg.c