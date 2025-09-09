# Sample Terraform configuration #


This is a sample [Terraform root module](https://developer.hashicorp.com/terraform/language/modules#the-root-module)
configuration.

See [here](https://www.terraform.io/docs/modules/index.html) for more
details on Terraform modules and the standard module structure.

## Pre-requisites ##

- [Terraform](https://www.terraform.io/) installed on your system.
- AWS CLI access [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
  for the appropriate account on your system.
- An accessible AWS S3 bucket to store Terraform state
  (specified in [`backend.tf`](backend.tf)).
- An accessible AWS DynamoDB database to store the Terraform state lock
  (specified in [`backend.tf`](backend.tf)).

## Building the Terraform-based infrastructure ##

1. Create a backend configuration file named `<environment>.tfconfig` containing
   the name of the bucket where your environment's Terraform state is stored -
   this file is required to initialize the Terraform backend in an environment:

   ```hcl
   bucket = "my-environment-terraform-state-bucket"
   ```

1. Initialize the Terraform backend for the environment using your backend
   configuration file:

   ```console
   terraform init -backend-config=<environment>.tfconfig
   ```

   > [!NOTE]
   > When performing this step for any additional environments (i.e. not your
   > first environment), use the `-reconfigure` flag:
   >
   > ```console
   > terraform init -backend-config=other-env.tfconfig -reconfigure
   > ```

1. Create a Terraform workspace (if you haven't already done so) by running
   `terraform workspace new <workspace_name>`.
1. Create a `<workspace_name>.tfvars` file with all of the required
   variables (see [Inputs](#inputs) below for details).
1. Run the command `terraform init`.
1. Create the Terraform infrastructure by running the command:

   ```console
   terraform apply -var-file=<workspace_name>.tfvars
   ```

## Tearing down the Terraform-based infrastructure ##

1. Select the appropriate Terraform workspace by running
   `terraform workspace select <workspace_name>`.
1. Destroy the Terraform infrastructure in that workspace by running
   `terraform destroy -var-file=<workspace_name>.tfvars`.

<!-- BEGIN_TF_DOCS -->
## Requirements ##

| Name | Version |
|------|---------|
| terraform | ~> 1.1 |
| aws | ~> 4.9 |

## Providers ##

| Name | Version |
|------|---------|
| aws | ~> 4.9 |

## Modules ##

| Name | Source | Version |
|------|--------|---------|
| example | github.com/cisagov/skeleton-tf-module | v1.0.0 |

## Resources ##

| Name | Type |
|------|------|
| [aws_subnet.example](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/subnet) | resource |
| [aws_vpc.example](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc) | resource |

## Inputs ##

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| ami\_owner\_account\_id | The ID of the AWS account that owns the AMI, or "self" if the AMI is owned by the same account as the provisioner. | `string` | `"self"` | no |
| aws\_availability\_zone | The AWS availability zone to deploy into (e.g. a, b, c, etc.). | `string` | `"a"` | no |
| aws\_region | The AWS region to deploy into (e.g. us-east-1). | `string` | `"us-east-1"` | no |
| tags | Tags to apply to all AWS resources created. | `map(string)` | ```{ "Testing": true }``` | no |
| tf\_role\_arn | The ARN of the role that can terraform non-specialized resources. | `string` | n/a | yes |

## Outputs ##

| Name | Description |
|------|-------------|
| arn | The EC2 instance ARN. |
| availability\_zone | The AZ where the EC2 instance is deployed. |
| id | The EC2 instance ID. |
| private\_ip | The private IP of the EC2 instance. |
| subnet\_id | The ID of the subnet where the EC2 instance is deployed. |
<!-- END_TF_DOCS -->
