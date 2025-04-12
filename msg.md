What is the issue with my code
#include "gen_image.hpp"
#include <argparse/argparse.hpp>
#include <string.h>
#include <iostream>

int main(int argc, char* argv[]) {
  [[maybe_unused]] bool text_extraction_mode{false};
  [[maybe_unused]] int page_number{1};
  [[maybe_unused]] float scale_factor{1.0f};
  [[maybe_unused]] int total_pages{1};


  argparse::ArgumentParser program("pdfViewer using pdfmium", "135.0.7087.0",
                                   argparse::default_arguments::help, false);

  program.add_argument("-i")
    .required()
    .help("Name of the pdf file");

program.add_argument("-m", "--mode")
    .help("add to change mode to text extraction mode");
program.add_argument("-T","--total-pages")
  .flag()
  .help("Get the total pages in the current pdf file");

  program.add_argument("-p", "--page")
      .store_into(page_number
          )
      .help("page to view");

  program.add_argument("-s", "--scale_factor")
      .store_into(scale_factor)
      .help("factor by which to scale the page image");

  try {
    program.parse_args(argc, argv);
    if (auto arg = program.present("-i")) {
      const char *fname = arg->c_str();
      auto is_get_total_pages=program.present("--total-pages");
      if(is_get_total_pages){
        std::cout<<get_total_pages(fname);
      }else{
      gen_page_image(fname,page_number,scale_factor);
      }
    }
  } catch (const std::runtime_error &err) {
    std::cerr << err.what() << "\n";
    std::cerr << program << "\n";
    return 1;
  }
  return 0;
}

Error libc++abi: terminating due to uncaught exception of type std::logic_error: Argument with default value always presents