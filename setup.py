# To build locally: python setup.py egg_info -RDb "" bdist_egg 
# To release: python setup.py egg_info -RD sdist bdist_egg register upload
# To create a named release: python setup.py egg_info -RDb "a1" sdist bdist_egg register upload
# To release a dev build: python setup.py egg_info -rD sdist bdist_egg register upload
# See http://peak.telecommunity.com/DevCenter/setuptools#release-tagging-options for more information.

from setuptools import setup, find_packages
import os, sys
import hookbox

static_types = [
    '*.js', 
    '*.html',
    '*.css', 
    '*.ico', 
    '*.gif', 
    '*.jpg', 
    '*.png', 
    '*.txt*',
    '*.py',
    '*.template',
    '*.pkg'
]

#if sys.platform != "win32":
#    _install_requires.append("Twisted")

_install_requires = [
    'eventlet>=0.9.10', 
    'paste', 
    'csp_eventlet>=0.5.1', 
    'rtjp_eventlet>=0.3.2', 
    'pygments',
    'restkit==4.1.3',
    'event==0.4.2',
#    'nose==0.11.1',
#    'coverage',
]

# python <= 2.5
if sys.version_info[1] <= 5:
    _install_requires.append('simplejson')


def find_package_data():
    targets = [ 
        os.path.join('hookbox', 'static'),
        os.path.join('hookbox', 'admin', 'static'),
        os.path.join('hookbox', 'js_src')
    ]
    package_data = {'': reduce(list.__add__, [ '.git' not in d and [ os.path.join(d[len('hookbox/'):], e) for e in
            static_types ] or [] for (d, s, f) in reduce(list.__add__, [ [ i for i in os.walk(target) ] for target in targets ])
        ]) }
    return package_data

def main():
    setup(
        name='hookbox',
        version=hookbox.__version__,
        author='Michael Carter',
        author_email='CarterMichael@gmail.com',
        maintainer='Dax Reyes',
        maintainer_email='raikage@gmail.com',
        url='https://github.com/hookbox/hookbox',
        license='MIT License',
        description='HookBox is a Comet server and message queue that tightly integrates with your existing web application via web hooks and a REST interface.',
        long_description='',
        packages= find_packages(),
        package_data = find_package_data(),
        zip_safe = False,
        install_requires = _install_requires,
        entry_points = '''    
            [console_scripts]
            hookbox = hookbox.start:main
        ''',
        
        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],        
    )


if __name__ == '__main__':
    main()
