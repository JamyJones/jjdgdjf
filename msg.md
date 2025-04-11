Why is my tesseract cpp program being aborted on starting

#include <string.h>
#include <tesseract/baseapi.h>
#include <leptonica/allheaders.h>
#include <opencv2/opencv.hpp>
#include <iostream>
#include "extract_text.hpp"

cv::Mat getRegionOfInterest(const cv::Mat& image, int x, int y, int width, int height) {
    cv::Rect roi(x, y, width, height);
    return image(roi);
}

cv::Mat convert_ROI_grayscale(const cv::Mat& croppedImage){
    cv::Mat grayImage;
    cv::cvtColor(croppedImage, grayImage, cv::COLOR_BGR2GRAY);
    return grayImage;
}

std::string extractText(const cv::Mat& grayImage){
    const char* tess_data_path = "/data/data/com.termux/files/home/tesseract/data/data/com.termux/files/usr/share/tessdata";
    tesseract::TessBaseAPI ocr;
    if (ocr.Init(tess_data_path, "eng", tesseract::OEM_LSTM_ONLY)) {
        std::cerr << "Could not initialize Tesseract." << std::endl;
        return "";
    }
    ocr.SetImage(grayImage.data, grayImage.cols, grayImage.rows, grayImage.channels(), grayImage.step);
    char* text = ocr.GetUTF8Text();
    std::string extractedText(text);
    ocr.End();
    delete[] text;
    return extractedText;
}
void getSelectedText(const char* image_name,float x, float y, int width,int height){
  cv::Mat img = cv::imread(image_name);
  cv::Mat croppedImage = getRegionOfInterest(img,x,y,width,height);
  cv::Mat grayImage = convert_ROI_grayscale(croppedImage);
  std::string text_selection = extractText(grayImage);
  std::cout<<text_selection<<"\n";
}