cd venv/lib/site-packages
zip -r ../../../deployment.zip .
cd ../../../src/get_current_sentiments
zip -r ../../deployment.zip .
cd ../..
aws lambda update-function-code --profile reddit_lambda_user --function-name get_current_sentiments --zip-file fileb://deployment.zip