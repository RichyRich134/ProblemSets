# File extensions (for instan.jpg, .txt, .mp3). When double clicking something, the OS figures out through the extension which program to launch. It is a naming convention to identify file types on a disk.
# Media types (MIME) is mainly for programs and browsers, while it is being processed/transferred. It tells how to interpret the files content, and display it.

# Split the x value, and then match it. 

x = input("File name:").strip().lower()

# Reverse split(new), split at most one time.
if "." in x:
    _, value = x.rsplit(".", 1)
match value:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("plain/txt")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")


