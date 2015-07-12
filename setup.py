import setuptools
setuptools.setup(
    name = "GetProjects",
    py_modules = ["getprojects"],
    entry_points = {"console_scripts": ["getprojects=getprojects:main"]},
    version = "0.1.0",
    description = "Clone all your GitHub repos with one command.",
    author = "Gokberk Yaltirakli",
    author_email = "webdosusb@gmail.com",
    url = "https://github.com/gkbrk/GetProjects",
    keywords = ["github", "git", "repo"],
    requires = ["requests"]
)
