cd venv/lib/site-packages
zip -r ../../../deployment.zip .
cd ../../../src/%1
zip -r ../../deployment.zip .
cd ../..
aws lambda update-function-code --profile reddit_lambda_user --function-name %1 --zip-file fileb://deployment.zip