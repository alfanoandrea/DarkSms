# DarkSMS

<div align="center">

**An Advanced Python CLI Tool for Anonymous SMS Messaging**

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Active-brightgreen.svg)](https://github.com/alfanoandrea/DarkSms)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Security & Compliance](#security--compliance)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)
- [Support](#support)

---

## 🎯 Overview

**DarkSMS** is a lightweight yet powerful Python application designed to facilitate the sending of anonymous SMS messages through the Textbelt API. Built with security and ease-of-use in mind, DarkSMS provides a command-line interface that handles all the complexities of SMS delivery while maintaining user anonymity.

### Key Characteristics

- **Anonymous Messaging**: Send SMS messages without revealing your identity
- **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux
- **User-Friendly Interface**: Interactive CLI with clear prompts and feedback
- **Automatic Updates**: Built-in version checking and update notifications
- **Connection Monitoring**: Real-time internet connectivity verification
- **Input Validation**: Comprehensive regex-based phone number validation
- **Color-Coded Output**: Enhanced readability with terminal color support

---

## ✨ Features

- ✅ **Anonymous SMS Delivery** - Send messages without personal identification
- ✅ **International Support** - Support for country-specific international prefixes
- ✅ **Validation System** - Automatic phone number and message validation
- ✅ **Auto-Update** - Checks for script updates on launch
- ✅ **Network Detection** - Verifies internet connectivity before sending
- ✅ **Colored CLI Output** - Enhanced user experience with formatted terminal colors
- ✅ **Error Handling** - Robust error management with user-friendly messages
- ✅ **Version Management** - Current version: 1.2

---

## 📋 Prerequisites

Before installing DarkSMS, ensure your system meets the following requirements:

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python Version**: Python 3.6 or higher
- **Internet Connection**: Required for API communication
- **Terminal/Command Line**: Access to command-line interface

### Required Permissions
- Read/Write access to the project directory
- Outbound internet access (HTTPS on port 443)

---

## 🚀 Installation

### Step 1: Clone the Repository

Open your terminal or command prompt and execute:

```bash
git clone https://github.com/alfanoandrea/DarkSms.git
cd DarkSms
```

### Step 2: Verify Python Installation

Confirm Python is installed on your system:

```bash
python --version
# or
python3 --version
```

### Step 3: Install Dependencies

Install all required Python packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

**Dependencies:**
- `requests` - HTTP library for API communication with Textbelt service

### Step 4: Verify Installation

Confirm the installation was successful:

```bash
python DarkSms.py
```

You should see the DarkSMS banner and welcome screen.

---

## 📖 Usage

### Basic Usage

1. **Navigate to Project Directory**
   ```bash
   cd path/to/DarkSms
   ```

2. **Launch the Application**
   ```bash
   python DarkSms.py
   # or
   python3 DarkSms.py
   ```

3. **Follow Interactive Prompts**
   - Enter the **international prefix** (e.g., +39 for Italy, +1 for USA)
   - Enter the **phone number** (without the prefix)
   - Type your **message content**
   - Confirm sending when prompted

4. **Receive Confirmation**
   - Success or error messages will be displayed
   - Check Textbelt service status if issues occur

### Interactive Mode

The application guides you through each step:

```
Enter international prefix: +39
Enter phone number: 3331234567
Enter message: Hello, this is a test message
Confirm sending? (y/n): y
```

---

## ⚙️ Configuration

### Textbelt Service

DarkSMS uses the **Textbelt** API for message delivery. The service provides:
- Free tier with rate limiting
- 100% delivery guarantee
- Global SMS coverage
- No authentication required for basic usage

### Default Settings

- **API Endpoint**: Textbelt's official SMS service
- **Timeout**: 5 seconds for API requests
- **Update Check**: Performed on application startup
- **Max Retries**: Automatic retry on network failures

---

## 🔌 API Reference

### Core Functions

#### `send_sms(prefix, number, message)`
Sends an SMS message to the specified recipient.

**Parameters:**
- `prefix` (str): International country code (e.g., "+39")
- `number` (str): Phone number without country code
- `message` (str): Message content to send

**Returns:**
- `bool`: True if successful, False otherwise

#### `validate_phone_number(number)`
Validates phone number format using regex patterns.

**Parameters:**
- `number` (str): Phone number to validate

**Returns:**
- `bool`: True if valid format, False otherwise

#### `check_internet()`
Verifies internet connectivity before sending.

**Returns:**
- `bool`: True if connected, False otherwise

---

## 💡 Examples

### Example 1: Sending a Simple Message

```bash
$ python DarkSms.py

     ___           __    ____         
    / _ \___  ____/ /__ / __/_ _  ___ 
   / // / _ `/ __/  '_/_\ \/  ' \(_-< 
  /____/\_,_/_/ /_/\_\/___/_/_/_/___/

Enter international prefix: +39
Enter phone number: 3331234567
Enter message: Hello World!
Confirm sending? (y/n): y

✓ Message sent successfully!
```

### Example 2: International Messaging

```bash
Enter international prefix: +1
Enter phone number: 5551234567
Enter message: Hi from DarkSMS!
Confirm sending? (y/n): y
```

---

## 🔒 Security & Compliance

### Important Legal Considerations

**⚠️ DISCLAIMER**: Users are solely responsible for the legal use of this application.

### Compliance Requirements

- **Jurisdiction Laws**: Comply with SMS regulations in your country
- **Privacy Laws**: Respect GDPR, CCPA, and similar privacy regulations
- **Carrier Policies**: Follow your carrier's acceptable use policies
- **Service Terms**: Adhere to Textbelt's Terms of Service

### Prohibited Uses

❌ Spam and unsolicited messages  
❌ Phishing or social engineering attacks  
❌ Harassment or threats  
❌ Fraudulent activities  
❌ Commercial bulk messaging without consent  
❌ Messages violating local telecommunications laws  

### Best Practices

✅ Always obtain recipient consent before sending  
✅ Include identification information when legally required  
✅ Monitor for abuse reports and cease problematic messaging  
✅ Keep audit logs of sent messages  
✅ Use appropriate message intervals to avoid rate limiting  

---

## 🐛 Troubleshooting

### Common Issues

#### Issue: "No module named 'requests'"
**Solution**: Install dependencies again
```bash
pip install --upgrade -r requirements.txt
```

#### Issue: "Network connection failed"
**Solution**: 
- Check your internet connection
- Verify firewall settings allow HTTPS
- Try using a VPN if service is region-blocked

#### Issue: "Invalid phone number"
**Solution**:
- Verify the format matches the country code
- Remove any spaces or dashes
- Ensure you're using the correct international prefix

#### Issue: "Message sending failed"
**Solution**:
- Check Textbelt service status (online availability)
- Verify phone number is correct
- Try resending with a different message
- Check rate limiting (max messages per hour)

#### Issue: "Update check failed"
**Solution**:
- This is non-critical; the application will continue normally
- Check your internet connection
- The application will still function without updating

### Debug Mode

For detailed troubleshooting, check the console output for error messages. The application provides specific error details to help identify issues.

---

## 🤝 Contributing

Contributions are welcome! To contribute to DarkSMS:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/improvement`)
3. **Commit** your changes (`git commit -m 'Add feature'`)
4. **Push** to the branch (`git push origin feature/improvement`)
5. **Open** a Pull Request with detailed description

### Contribution Areas
- Bug fixes and issue resolution
- Feature enhancements
- Documentation improvements
- Code optimization
- Localization support

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for complete details.

### MIT License Summary
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ⚠️ Liability: PROVIDED AS-IS
- ⚠️ Warranty: NONE PROVIDED

---

## 👤 Credits

**DarkSMS** was created and is maintained by **alfanowski**.

- **GitHub**: [@alfanoandrea](https://github.com/alfanoandrea)
- **Project Repository**: [DarkSms](https://github.com/alfanoandrea/DarkSms)

### Acknowledgments
- **Textbelt**: For providing reliable SMS delivery service
- **Community**: For feedback and contributions

---

## 🆘 Support

### Getting Help

If you encounter issues or have questions:

1. **Check Troubleshooting**: Review the [Troubleshooting](#troubleshooting) section
2. **GitHub Issues**: Open an issue on the [project repository](https://github.com/alfanoandrea/DarkSms/issues)
3. **Documentation**: Review this README for comprehensive guidance
4. **Service Status**: Check Textbelt service status for API-related issues

### Reporting Bugs

When reporting bugs, please include:
- Operating system and Python version
- Exact error messages
- Steps to reproduce the issue
- Expected vs. actual behavior

---

<div align="center">

**Made with ❤️ by alfanowski**

[⬆ Back to top](#darksms)

</div>
