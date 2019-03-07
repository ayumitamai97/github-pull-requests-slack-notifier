# Usage
1. Execute `pip3 install -r requirements.txt -t .`
2. Set your AWS configuration in `~/.aws/config` and `~/.aws/credentials`
3. Set environmental variables by creating new file `variables.yml` in project root directory  
   See variable name by referencing `functions.environment` in serverless.yml
4. Execute `serverless deploy`

# CloudWatch Events
- This function will fire 1:00 UTC (10:00 JST) on Monday, Thursday and Saturday by default  
  as stated in `serverless.yml`.
- Please check CloudWatch Event schedules by AWS CLI or AWS management console after deployment.  
  I made a mistake on cron statement and executed the function no less than 60 times in one hour.

