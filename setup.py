from setuptools import setup, find_packages

setup(
    name="grpc-extensions",
    version="0.0.3",
    python_requires=">=3.7.9",
    description="Python Grpc Library",
    long_description="python grpc library, provide various tools and middlewares",
    license="MIT Licence",
    url="https://github.com/go-zs/python-grpc",
    author="haoyinqianzui",
    author_email="810909753@qq.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[
        "grpcio>=1.32.0",
        "protobuf>=3.14.0",
    ],
)
