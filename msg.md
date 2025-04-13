Is this the correct in c++
const char* filename=getname();
std::filesytem::path absPath = std::filesystem::absolute(filename);
Versus
std::filesystem::path p(filename)
std::string filepath = std::filesystem::absolute(p)