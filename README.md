# AWS Production-Grade VPC Architecture (High Availability + Secure Design)

A production-style AWS cloud architecture demonstrating secure, scalable, and highly available infrastructure using VPC networking best practices.

This project replicates real-world enterprise cloud design patterns used in modern DevOps environments.

---

## Architecture Overview

This infrastructure is designed with **security, scalability, and fault tolerance** as core principles.

It includes:

- Custom VPC with isolated network boundary
- Multi-AZ public and private subnets
- Internet Gateway for controlled public access
- NAT Gateway for secure outbound connectivity
- Bastion Host for secure SSH access
- Application Load Balancer (ALB)
- Auto Scaling Group (ASG)
- EC2 instances running application workload

---

## High-Level Architecture Flow

User Traffic
→ Application Load Balancer
→ Private EC2 Instances (Auto Scaling Group)
→ Multi-AZ Deployment

Admin Access
→ Bastion Host (Public Subnet)
→ Private EC2 Instances (SSH)

Outbound Internet Access (Private Instances)
→ NAT Gateway
→ Internet Gateway

---

## Key Design Principles

### 1. Security First Architecture
- Application servers deployed in private subnets
- No direct public access to EC2 instances
- Controlled SSH access via Bastion Host
- Security Groups enforce strict inbound rules

---

### 2. High Availability
- Resources distributed across 2 Availability Zones
- Load Balancer ensures fault-tolerant traffic distribution
- Auto Scaling maintains desired instance capacity

---

### 3. Scalability
- Auto Scaling Group dynamically adjusts EC2 instances
- Launch Template ensures consistent provisioning
- Stateless application design

---

### 4. Network Isolation
- Public subnet: ALB, NAT Gateway, Bastion Host
- Private subnet: Application EC2 instances only
- Route tables control traffic flow precisely

---

## AWS Services Used

| Service | Purpose |
|--------|--------|
| VPC | Network isolation |
| Subnets | Public/Private segmentation |
| Internet Gateway | Public internet access |
| NAT Gateway | Secure outbound traffic |
| EC2 | Application compute |
| Auto Scaling Group | Dynamic scaling |
| Launch Template | Instance configuration |
| Application Load Balancer | Traffic distribution |
| Security Groups | Instance-level firewall |

---

## Implementation Summary

1. Created a custom VPC using AWS VPC Wizard
2. Configured public and private subnets across two AZs
3. Attached Internet Gateway for public resources
4. Configured NAT Gateway for private subnet internet access
5. Deployed Bastion Host in public subnet for SSH access
6. Created Launch Template for EC2 configuration
7. Deployed Auto Scaling Group in private subnets
8. Configured Application Load Balancer with Target Group
9. Verified application access via ALB DNS endpoint

---

## Security Model

- Private EC2 instances are not directly reachable from the internet
- SSH access is only possible through Bastion Host
- Security Groups restrict traffic at each layer
- Only Load Balancer is publicly exposed

---

## What This Project Demonstrates

- Real-world AWS networking architecture design
- Secure cloud infrastructure principles
- Multi-tier application deployment
- High availability and fault tolerance design
- Production-level DevOps understanding

---

## Future Enhancements

- Terraform/IaC implementation
- CI/CD pipeline integration (GitHub Actions)
- CloudWatch monitoring + alarms
- HTTPS with ACM + Route53 domain setup
- Dockerized application deployment
- Kubernetes migration (EKS)

---

## Screenshots

> Add AWS console screenshots inside `/architecture/screenshots`

---

## Author

Built as part of a cloud engineering and DevOps learning journey focused on real-world production infrastructure design.