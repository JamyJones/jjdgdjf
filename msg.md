What am doing wrong in this bash script
#!/bin/bash
do_this=$1
filename=$(cat Db/pdf_name.txt)
if [[ $do_this -eq "total_pages" ]]; then
  ~/./pdfviewer.so --total-pages -i "$filename"
elif [[ $do_this -eq "gen_page" ]]; then
  page_no=$2
  rm images/*.png
  ~/./pdfviewer.so --page "$page_no" -i "$filename"
fi