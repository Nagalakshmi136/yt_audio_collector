cd ../..
echo "Running mypy check..."
mypy $(git ls-files "*.py")

echo "Running pylint check..."
pylint $(git ls-files "*.py")