## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | 3.68.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | 3.68.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_alb"></a> [alb](#module\_alb) | ./modules/alb | n/a |
| <a name="module_ec2"></a> [ec2](#module\_ec2) | ./modules/ec2 | n/a |
| <a name="module_rds"></a> [rds](#module\_rds) | ./modules/rds | n/a |
| <a name="module_vpc"></a> [vpc](#module\_vpc) | ./modules/vpc | n/a |

## Resources

| Name | Type |
|------|------|
| [aws_ami.amazon_linux](https://registry.terraform.io/providers/hashicorp/aws/3.68.0/docs/data-sources/ami) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_alb_name"></a> [alb\_name](#input\_alb\_name) | application load balancer name | `string` | `"umesh-alb"` | no |
| <a name="input_azs"></a> [azs](#input\_azs) | availability zones for subnets | `list(string)` | n/a | yes |
| <a name="input_db_name"></a> [db\_name](#input\_db\_name) | Database name | `string` | `"todo"` | no |
| <a name="input_db_pass"></a> [db\_pass](#input\_db\_pass) | Database password | `string` | n/a | yes |
| <a name="input_db_username"></a> [db\_username](#input\_db\_username) | Database username | `string` | n/a | yes |
| <a name="input_instance_type"></a> [instance\_type](#input\_instance\_type) | instance type | `string` | `"t2.micro"` | no |
| <a name="input_key_name"></a> [key\_name](#input\_key\_name) | key name | `string` | `"UmeshKey"` | no |
| <a name="input_private_subnet_cidr"></a> [private\_subnet\_cidr](#input\_private\_subnet\_cidr) | private subnet cidr | `list(any)` | n/a | yes |
| <a name="input_public_subnet_cidr"></a> [public\_subnet\_cidr](#input\_public\_subnet\_cidr) | public subnet cidr | `list(any)` | n/a | yes |
| <a name="input_rds_instance_name"></a> [rds\_instance\_name](#input\_rds\_instance\_name) | rds instance name | `string` | `"umesh-rds"` | no |
| <a name="input_security_group_name"></a> [security\_group\_name](#input\_security\_group\_name) | database security group name | `string` | `"umesh-rds-subnet-group"` | no |
| <a name="input_sg_ports"></a> [sg\_ports](#input\_sg\_ports) | webserver security group port | `list(string)` | <pre>[<br>  "80",<br>  "22"<br>]</pre> | no |
| <a name="input_ssh_client"></a> [ssh\_client](#input\_ssh\_client) | n/a | `string` | n/a | yes |
| <a name="input_subnet_group_name"></a> [subnet\_group\_name](#input\_subnet\_group\_name) | database subnet group name | `string` | `"umesh-db-sg"` | no |
| <a name="input_target_group_name"></a> [target\_group\_name](#input\_target\_group\_name) | application load balancer target group name | `string` | `"umesh-tg"` | no |
| <a name="input_vpc_cidr"></a> [vpc\_cidr](#input\_vpc\_cidr) | custom vpc | `any` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_alb_dns"></a> [alb\_dns](#output\_alb\_dns) | alb dns name |
| <a name="output_instance_public_ips"></a> [instance\_public\_ips](#output\_instance\_public\_ips) | webserver public ips |
| <a name="output_public_subnet_ids"></a> [public\_subnet\_ids](#output\_public\_subnet\_ids) | publict subnet ids |
| <a name="output_rds_endoint"></a> [rds\_endoint](#output\_rds\_endoint) | rds endpoint |
<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | 3.68.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | 3.68.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_alb"></a> [alb](#module\_alb) | ./modules/alb | n/a |
| <a name="module_ec2"></a> [ec2](#module\_ec2) | ./modules/ec2 | n/a |
| <a name="module_rds"></a> [rds](#module\_rds) | ./modules/rds | n/a |
| <a name="module_vpc"></a> [vpc](#module\_vpc) | ./modules/vpc | n/a |

## Resources

| Name | Type |
|------|------|
| [aws_ami.amazon_linux](https://registry.terraform.io/providers/hashicorp/aws/3.68.0/docs/data-sources/ami) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_alb_name"></a> [alb\_name](#input\_alb\_name) | application load balancer name | `string` | `"umesh-alb"` | no |
| <a name="input_azs"></a> [azs](#input\_azs) | availability zones for subnets | `list(string)` | n/a | yes |
| <a name="input_db_name"></a> [db\_name](#input\_db\_name) | Database name | `string` | `"todo"` | no |
| <a name="input_db_pass"></a> [db\_pass](#input\_db\_pass) | Database password | `string` | n/a | yes |
| <a name="input_db_username"></a> [db\_username](#input\_db\_username) | Database username | `string` | n/a | yes |
| <a name="input_instance_type"></a> [instance\_type](#input\_instance\_type) | instance type | `string` | `"t2.micro"` | no |
| <a name="input_key_name"></a> [key\_name](#input\_key\_name) | key name | `string` | `"UmeshKey"` | no |
| <a name="input_private_subnet_cidr"></a> [private\_subnet\_cidr](#input\_private\_subnet\_cidr) | private subnet cidr | `list(any)` | n/a | yes |
| <a name="input_public_subnet_cidr"></a> [public\_subnet\_cidr](#input\_public\_subnet\_cidr) | public subnet cidr | `list(any)` | n/a | yes |
| <a name="input_rds_instance_name"></a> [rds\_instance\_name](#input\_rds\_instance\_name) | rds instance name | `string` | `"umesh-rds"` | no |
| <a name="input_security_group_name"></a> [security\_group\_name](#input\_security\_group\_name) | database security group name | `string` | `"umesh-rds-subnet-group"` | no |
| <a name="input_sg_ports"></a> [sg\_ports](#input\_sg\_ports) | webserver security group port | `list(string)` | <pre>[<br>  "80"<br>]</pre> | no |
| <a name="input_ssh_client"></a> [ssh\_client](#input\_ssh\_client) | n/a | `string` | n/a | yes |
| <a name="input_subnet_group_name"></a> [subnet\_group\_name](#input\_subnet\_group\_name) | database subnet group name | `string` | `"umesh-db-sg"` | no |
| <a name="input_target_group_name"></a> [target\_group\_name](#input\_target\_group\_name) | application load balancer target group name | `string` | `"umesh-tg"` | no |
| <a name="input_vpc_cidr"></a> [vpc\_cidr](#input\_vpc\_cidr) | custom vpc | `any` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_alb_dns"></a> [alb\_dns](#output\_alb\_dns) | alb dns name |
| <a name="output_instance_public_ips"></a> [instance\_public\_ips](#output\_instance\_public\_ips) | webserver public ips |
| <a name="output_public_subnet_ids"></a> [public\_subnet\_ids](#output\_public\_subnet\_ids) | publict subnet ids |
| <a name="output_rds_endoint"></a> [rds\_endoint](#output\_rds\_endoint) | rds endpoint |
<!-- END_TF_DOCS -->
