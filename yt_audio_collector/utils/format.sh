cd ../..
black $(git ls-files "*.py")
isort --profile black $(git ls-files "*.py")