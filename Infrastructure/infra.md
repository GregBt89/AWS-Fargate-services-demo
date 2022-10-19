# **Deploying demo application with AWS CloudFormation**

The [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) service makes easier the deployment and provisioning of resources . A template (i.e. blueprint) written in yaml or json format defines the required resources with the approriate configurations for a particular application and AWS automatically creates them. The creation of the resources from the template is stored in a stack. 

Here the [template](./ApplicationTemplate.yml) includes the configuration of a VPC, Subent, route table, etc. as well as the task definition and AWS ECS service for running the demo applicaiton in AWS. 