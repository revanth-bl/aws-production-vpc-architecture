# Networking Architecture

## VPC Design
A custom Virtual Private Cloud is created to isolate resources from default AWS network.

---

## Subnet Strategy

### Public Subnet
- Bastion Host
- NAT Gateway
- Application Load Balancer

### Private Subnet
- EC2 Application Servers (Auto Scaling Group)

---

## Traffic Flow

Internet → ALB → Private EC2

Admin Access → Bastion Host → Private EC2

Private EC2 → NAT Gateway → Internet