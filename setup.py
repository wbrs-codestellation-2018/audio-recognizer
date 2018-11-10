from setuptools import setup
setup(name='audio_recognizer',
      version='0.1',
      description='Gets genre info from files',
      url='https://github.com/wbrs-codestellation-2018/audio-recognizer',
      author='Sam Stern',
      author_email='sternj@brandeis.edu',
      license='MIT',
      packages=['audio_recognizer'],
      dependency_links=['https://github.com/acrcloud/acrcloud_sdk_python/tarball/master'],
      zip_safe=False)