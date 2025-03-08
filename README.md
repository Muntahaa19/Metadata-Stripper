**Advanced Metadata Anonymizer**

:pushpin:**Overview**

The Advanced Metadata Anonymizer is a Python-based tool designed to remove and modify metadata from various file types, ensuring complete digital privacy. Unlike traditional metadata strippers, this tool not only deletes metadata but also alters timestamps, changes file structures, randomizes attributes, and modifies file formats to prevent forensic tracking.

This tool is perfect for privacy-conscious users, journalists, cybersecurity professionals, and organizations looking to protect sensitive information and maintain anonymity.

:pushpin:**Features**

✅ Removes metadata from images, videos, audio files, PDFs, and documents
✅ Randomizes timestamps to prevent forensic tracing
✅ Alters file structure for enhanced anonymity
✅ Changes file format to disrupt signature-based identification
✅ Modifies image resolution & attributes
✅ User-friendly GUI using Tkinter
✅ No dependency on external tools like FFmpeg or ExifTool
✅ Cross-platform compatibility (Windows, macOS, Linux)

:pushpin:**Supported File Types**

Images: JPG, JPEG, PNG, WebP, BMP, TIFF

Videos: MP4, MOV, AVI, MKV, WMV, FLV

Audio: MP3, FLAC, OGG, Opus, AAC, WAV

Documents: DOC, DOCX, PDF

:pushpin:**Installation**

Ensure you have Python 3.7+ installed. Then, install the required dependencies:

*pip install pillow piexif pymupdf mutagen python-docx numpy tk*

Alternatively, install dependencies using the requirements file:

*pip install -r requirements.txt*

:pushpin:**Usage**

Run the script to open a simple GUI for selecting files:

python metadata_anonymizer.py

:pushpin:**Manual Usage (Command Line)**

You can also modify and remove metadata from specific files using:

from metadata_anonymizer import remove_metadata
remove_metadata("path/to/your/file")

:pushpin:**Contact**

For any issues, improvements, or contributions, feel free to reach out:

Github: https://github.com/Muntahaa19
🔗 LinkedIn: https://www.linkedin.com/in/muntaha-nasir-631307239?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app