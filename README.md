# Network CI/CD Pipeline Proof of Concept

## setup the routers
https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_usr_ssh/configuration/xe-16/sec-usr-ssh-xe-16-book/sec-usr-ssh-sec-copy.pdf

! AAA authentication and authorization must be configured properly for SCP to work.
aaa new-model
aaa authentication login default local
aaa authorization exec default local
username Sam privilege 15 password 0 Test123!
! SSH must be configured and functioning properly.
ip ssh time-out 120
ip ssh authentication-retries 3
ip scp server enable

https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/syst-mgmt/b-system-management/m_cm-config-versioning.html
configure terminal
archive
path bootflash:myconfig
maximum 14
time-period 10
end
archive config



I learend so much building out this POC and I want to thank everyone that has checked out the blog series that references this code base. I hope you brave souls that have started building your own can use some of these tools or concepts in your future deployments. Please check out the blog posts where I go into detail about every phase!

- [Building a Network CI/CD Pipeline Part 1 - Installing Docker](https://juliopdx.com/2021/10/20/building-a-network-ci/cd-pipeline-part-1/)
- [Building a Network CI/CD Pipeline Part 2 - Installing Drone Server and Runner](https://juliopdx.com/2021/10/20/building-a-network-ci/cd-pipeline-part-2/)
- [Building a Network CI/CD Pipeline Part 3 - .drone.yml and Building a Docker Image](https://juliopdx.com/2021/10/20/building-a-network-ci/cd-pipeline-part-3/)
- [Building a Network CI/CD Pipeline Part 4 - Testing with Batfish](https://juliopdx.com/2021/10/31/building-a-network-ci/cd-pipeline-part-4/)
- [Building a Network CI/CD Pipeline Part 5 - Deployments with Nornir and NAPALM](https://juliopdx.com/2021/11/08/building-a-network-ci/cd-pipeline-part-5/)
- [Building a Network CI/CD Pipeline Part 6 - Post Tests with Suzieq](https://juliopdx.com/2021/11/12/building-a-network-ci/cd-pipeline-part-6/)
