Can i tell the compiler to get past these error
src/mupdf-src/archive.c:169:9: error: assigning to 'fz_archive *' from incompatible type 'void *'
   169 |         arch = Memento_label(fz_calloc(ctx, 1, size), "fz_archive");
       |                ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 ./include/mupdf/memento.h:388:44: note: expanded from macro 'Memento_label'
   388 | #define Memento_label(A,B)                 (A)
       |                                            ^~~
 src/mupdf-src/archive.c:254:13: error: cannot initialize a variable of type 'fz_buffer *' with an rvalue of type 'void *'
   254 |         fz_buffer *ent = fz_tree_lookup(ctx, tree, name);
       |                    ^     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 src/mupdf-src/archive.c:261:13: error: cannot initialize a variable of type 'fz_buffer *' with an rvalue of type 'void *'
   261 |         fz_buffer *ent = fz_tree_lookup(ctx, tree, name);
       |                    ^     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 src/mupdf-src/archive.c:268:13: error: cannot initialize a variable of type 'fz_buffer *' with an rvalue of type 'void *'
   268 |         fz_buffer *ent = fz_tree_lookup(ctx, tree, name);
       |                    ^     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 src/mupdf-src/archive.c:274:2: error: no matching function for call to 'fz_drop_buffer'
   274 |         fz_drop_buffer(ctx, ent);
       |         ^~~~~~~~~~~~~~
 ./include/mupdf/fitz/buffer.h:63:6: note: candidate function not viable: cannot convert argument of incomplete type 'void *' to 'fz_buffer *' for 2nd argument
    63 | void fz_drop_buffer(fz_context *ctx, fz_buffer *buf);
       |      ^                               ~~~~~~~~~~~~~~
 src/mupdf-src/archive.c:327:8: error: no matching function for call to 'fz_new_buffer_from_copied_data'
   327 |         buf = fz_new_buffer_from_copied_data(ctx, data, size);
       |               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 ./include/mupdf/fitz/buffer.h:105:12: note: candidate function not viable: cannot convert argument of incomplete type 'const void *' to 'const unsigned char *' for 2nd argument
   105 | fz_buffer *fz_new_buffer_from_copied_data(fz_context *ctx, const unsigned char *data, size_t size);
       |            ^                                               ~~~~~~~~~~~~~~~~~~~~~~~~~
 src/mupdf-src/archive.c:475:15: error: assigning to 'multi_archive_entry *' from incompatible type 'void *'
   475 |                 arch->sub = fz_realloc(ctx, arch->sub, sizeof(*arch->sub) * n);
       |                             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 src/mupdf-src/archive.c:545:9: error: cannot initialize return object of type 'fz_archive_handler_context *' with an rvalue of type 'void *'
   545 |         return fz_keep_imp(ctx, ctx->archive, &ctx->archive->refs);