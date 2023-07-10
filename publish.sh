rm -rf ./build
rm -rf ./dist
rm -rf ./diz.egg-info

python setup.py sdist bdist_wheel
twine upload dist/*