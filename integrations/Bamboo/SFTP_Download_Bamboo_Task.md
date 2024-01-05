# SFTP Download Bamboo Task

You can use the SFTP Download task to transfer files and directories
from a remote SFTP server to the local working directory

Task Availability

This task is available after installing the **MettleCI - SFTP Plugin**
(dm-bamboo-sftp-plugin.jar) which contains the following tasks:

[SFTP Download Bamboo Task](SFTP_Download_Bamboo_Task) - Transfer files
from a remote server to the local working directory

<a href="SFTP_Upload_Bamboo_Task" data-linked-resource-id="499056670"
data-linked-resource-version="3" data-linked-resource-type="page">SFTP
Upload Bamboo Task</a> - Transfer files in the local working directory
to a remote server

## Configuration Steps

1.  Navigate to the **Tasks** configuration tab for the job (this will
    be the default job if creating a new plan).

2.  Click the name of an existing SFTP Download task, or click **Add
    Task** and then search 'SFTP' to easily locate the SFTP Download
    task type, in order to create a new task.

3.  Complete the following settings:

    |                                           |                                                                                                                                                             |
    |-----------------------|-------------------------------------------------|
    | Task Description                          | A description of the task, which is displayed in Bamboo.                                                                                                    |
    | Disable this task                         | Check, or clear, to selectively run this task.                                                                                                              |
    | Host                                      | The hostname or IP address of the remote server to which the files will be copied.                                                                          |
    | Authentication Type                       | **Username and Password** - Enter username and password to use when connecting to remote host.                                                              |
    |                                           | **SSH Private Key** - Browse to the SSH private key with which to authenticate with the remote host.  A passphrase for the key can be supplied if required. |
    | Remote Directory                          | The path to the download source directory on the remote server                                                                                              |
    | Include Pattern                           | A comma separated list of files to be downloaded relative to the remote directory path.  You can use Ant-style <a                                           
                                                 href="https://confluence.atlassian.com/bamboo0600/pattern-matching-reference-894742650.html"                                                                 
                                                 rel="nofollow">pattern matching</a> to include multiple files, such as `**/target/*.jar`.                                                                    |
    | Local Directory                           | The path to the download destination directory (relative to the Bamboo working directory).                                                                  |
    | Verify remote host fingerprint on connect | Enter the host fingerprint to be verified.  See [below](#SFTPDownloadBambooTask-fingerprint) for more details.                                              |
    | Port                                      | The port number of the remote host that is used for the SSH connection. The default value is 22.                                                            |

4.  Click **Save**  

    <img src="attachments/499220487/499056661.png" loading="lazy"
    data-image-src="attachments/499220487/499056661.png"
    data-unresolved-comment-count="0" data-linked-resource-id="499056661"
    data-linked-resource-version="1" data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image2020-1-8_12-8-10.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="499220487"
    data-linked-resource-container-version="3"
    data-media-id="f6865e37-1da9-4c1f-9979-23aad1ea2f21"
    data-media-type="file" />

## Host fingerprint

You can determine the fingerprint for a host by running:

``` java
ssh-keygen -l -F <HOSTNAME>
```

The fingerprint is the part of the response shown in the screenshot
below:

  

  

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2018-3-29_15-27-43.png](attachments/499220487/499220490.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-1-8_12-8-10.png](attachments/499220487/499056661.png)
(image/png)  
