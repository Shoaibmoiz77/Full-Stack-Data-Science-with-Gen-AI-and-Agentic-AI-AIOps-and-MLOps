# MySQL Installation Guide

A step-by-step walkthrough for downloading and installing MySQL Server on Windows using the MySQL Installer.

## Overview

This guide covers the complete installation process, from selecting a setup type through configuring the server and completing the installation.

## Prerequisites

- Windows operating system (64-bit recommended)
- Administrator privileges on your machine
- A stable internet connection (the installer downloads components during setup)

## Download

Download the official MySQL Installer from the MySQL website:

**[Download MySQL Installer](https://dev.mysql.com/downloads/installer/)**

Choose either:
- **Web Installer** – a smaller file that downloads only the components you select during setup
- **Full Installer** – a larger, all-in-one package that includes every component upfront

## Installation Steps

1. **Choose a Setup Type** – Select from Server only, Client only, Full, or Custom, depending on which MySQL products you need.
2. **Select Products** – Pick the specific components to install, such as MySQL Server, MySQL Shell, and MySQL Workbench.
3. **Download** – The installer downloads the selected products.
4. **Installation** – The selected products are installed on your system.
5. **Type and Networking** – Configure the server type and connectivity options (e.g., TCP/IP port).
6. **Authentication Method** – Choose between strong password encryption or the legacy authentication method.
7. **Accounts and Roles** – Set the MySQL root password and, optionally, add additional user accounts.
8. **Apply Configuration** – Review and execute the configuration steps to finalize the setup.

Detailed screenshots for each step are available in the accompanying [installation guide (PDF)](./mysql_installation_steps.pdf).

## Verifying the Installation

Once installation completes, you can confirm MySQL is running by opening MySQL Workbench or connecting via the command line:

```bash
mysql -u root -p
```

Enter the root password you configured during setup to confirm access.

## Resources

- [MySQL Official Downloads](https://dev.mysql.com/downloads/mysql/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

## License

This documentation is provided for personal learning and reference purposes.

