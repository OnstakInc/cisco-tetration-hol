# Cisco Tetration - Hands-On Lab
  
## Module26: AWS Lambda
  

### Steps for this Module  

<a href="https://cisco-tetration-hol-content.s3.amazonaws.com/videos/24_aws_lambda.mp4" style="font-weight:bold" title="AWS Lambda"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/video_icon_mini.png"> Click here to view a video of the tasks to create policy necessary to allow workloads to recieve traffic from the AWS Serverless technology called Lambda.</a>


#### Diagrams Used in this Module

This diagram depicts how AWS Lambda (aka 'Serverles') plays nice with Tetration from a policy perspective. AWS requires that you assign a VPC-created subnet to Lambda in order to use when it comes online to perform an event-driven function. In our lab, we have configured the triggering event to be time - specifically that every 60 seconds two functions are run using Node.js and they each make a single HTTPS call, one to the Windows-based nopCommerce app and the other to the Linux-based OpenCart app. This is helpful in two ways - firstly in that it allows us to include the concept of adding logic to your Tetration policy that accounts for AWS Serverless technologies, and secondly in that it actually ensures that there is constant traffic hitting these two applications and ensuring that there is plenty of flow data present in the Tetration collectors when it's time for you to run ADM for each app in order to generate that policy. If you're wondering why we don't have a function calling the Container-based Sock Shop app, it's due to the fact that Tetration agents do not collect flow telemetry information from container workloads and therefore wouldn't have much value since running ADM for container apps is a moot point, and needing to manually generate policy for these apps to include allowing serverless sources such as Lambda would have already been covered by the other two apps. 

<a href="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_008.png"><img src="https://onstakinc.github.io/cisco-tetration-hol/labguide/diagrams/images/diagrams_008.png" style="width:100%;height:100%;"></a>  
  

| [Return to Table of Contents](https://onstakinc.github.io/cisco-tetration-hol/labguide/) | [Go to Top of the Page](https://onstakinc.github.io/cisco-tetration-hol/labguide/module26/) | [Continue to the Next Module](https://onstakinc.github.io/cisco-tetration-hol/labguide/module27/) |