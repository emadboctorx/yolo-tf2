from setuptools import setup, find_packages

install_requires = [
    'pandas==1.1.2',
    'lxml==4.5.0',
    'opencv_python_headless==4.4.0.44',
    'imagesize==1.2.0',
    'seaborn==0.10.0',
    'tensorflow==2.3.1',
    # 'tensorflow-gpu==2.3',
    'numpy~=1.18.5',
    'matplotlib==3.2.1',
    'imgaug==0.4.0',
    'imagecorruptions==1.1.0',
    'tensorflow-addons==0.11.2',
    'configparser~=5.0.0',
    'scipy==1.4.1',
]

setup(
    name='yolo_tf2',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/emadboctorx/yolov3-keras-tf2',
    license='MIT',
    author='emadboctor',
    author_email='emad_1989@hotmail.com',
    description='yolo(v3/v4) implementation in keras and tensorflow 2.2',
    install_requires=install_requires,
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'yolotf2=yolo_tf2.cli:execute',
        ],
    },
)
