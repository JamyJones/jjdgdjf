Is this the correct in c++
std::filesytem::path absPath = std::filesystem::absolute("foo.py");
Versus
std::filesystem::path p("foo.py")
std::string filepath = std::filesystem::absolute(p)