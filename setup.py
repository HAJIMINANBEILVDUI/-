from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="chest_ct_lobe_segmentation",
    version="1.0.0",
    author="HAJIMINANBEILVDUI",
    author_email="2798073200@qq.com",
    description="胸部CT影像肺叶自动分割系统，基于nnU-Net v2",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HAJIMINANBEILVDUI/Technical-documentation",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8, <3.11",
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    entry_points={
        "console_scripts": [
            "ct_segment_train=scripts.train_model:main",
            "ct_segment_infer=scripts.run_inference:main",
        ],
    },
)