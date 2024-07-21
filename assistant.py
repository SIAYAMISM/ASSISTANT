import tkinter as tk
import webbrowser
import subprocess

# Main function to execute commands
def TakeCommand(event=None):
    command = entry.get()

    if command.lower() == "open youtube":
        webbrowser.open("https://www.youtube.com")
    elif command.lower() == "open myfavplaylist":
        webbrowser.open("https://www.youtube.com/watch?v=cP3Z4VLG3MI&list=RDMM&start_radio=1&rv=khBu-94O7E8")
    elif command.lower() == "open instagram":
        webbrowser.open("https://www.instagram.com/")
    elif command.lower() == "open notepad":
        subprocess.Popen("notepad.exe")
    elif command.lower() == "open gtasa":
        subprocess.Popen(r"E:\GTA San Andreas - (Www.ApunKaGames.Com)\Game - Copy\enb.exe")
    elif command.lower() == "open chrome":
        subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    elif command.lower() == "open internetexplorer":
        subprocess.Popen(r"C:\Program Files\Internet Explorer\iexplore.exe")
    elif command.lower() == "open needforspeed":
        subprocess.Popen(r"E:\Need_For_Speed_Most_Wanted_Black_Edition\Need for Speed - Most Wanted\speed.exe")
    elif command.lower() == "open adobeillustrator":
        subprocess.Popen(r"C:\Program Files\Adobe\Adobe Illustrator CC 2017\Support Files\Contents\Windows\Illustrator.exe")
    elif command.lower() == "open taskmanager":
        subprocess.Popen("taskmgr.exe")
    elif command.lower() == "open paint":
        subprocess.Popen("mspaint")
    elif command.lower() == "open vlc":
        subprocess.Popen(r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe")
    elif command.lower() == "open vscode":
        subprocess.Popen(r"C:\Users\MY OWN\AppData\Local\Programs\Microsoft VS Code\Code.exe")
    elif command.lower() == "open vsdc":
        subprocess.Popen(r"C:\Program Files\FlashIntegro\VideoEditor\VideoEditor.exe")
    elif command.lower() == "open cineb":
        webbrowser.open("https://www.cineb.rs")
    elif command.lower() == "open facebook":
        webbrowser.open("https://www.facebook.com")
    elif command.lower() == "open tiktok":
        webbrowser.open("https://tiktok.com")
    elif command.lower() == "open music":
        subprocess.Popen("explorer shell:music")
    elif command.lower() == "open snapchat":
        webbrowser.open("https://snapchat.com")
    elif command.lower() == "open pinterest":
        webbrowser.open("https://www.pinterest.com")
    elif command.lower() == "open linkedin":
        webbrowser.open("https://linkedin.com")
    elif command.lower() == "open fiverr":
        webbrowser.open("https://fiverr.com")
    elif command.lower() == "open playlist":
        webbrowser.open("https://www.youtube.com/watch?v=cl0a3i2wFcc&list=RDcl0a3i2wFcc&start_radio=1")
    elif command.lower() == "open chatgpt":
        webbrowser.open("https://chatgpt.com")
    elif command.lower() == "open pxfuel":
        webbrowser.open("https://pxfuel.com")
    elif command.lower() == "open pixels":
        webbrowser.open("https://pixels.com")
    elif command.lower() == "open oceanofgames":
        webbrowser.open("https://oceanofgames.com")
    elif command.lower() == "open savefromnet":
        webbrowser.open("https://en1.savefrom.net/1KB/")
    elif command.lower() == "open ilmkidunya":
        webbrowser.open("https://ilmkidunya.com")
    elif command.lower() == "open daraz":
        webbrowser.open("https://www.daraz.pk")
    elif command.lower() == "open uptodown":
        webbrowser.open("https://www.uptodown.com")
    elif command.lower() == "open khanacademy":
        webbrowser.open("https://www.khanacademy.com")
    elif command.lower() == "open quora":
        webbrowser.open("https://www.quora.com")
    elif command.lower() == "open testprepinsight":
        webbrowser.open("https://testprepinsight.com")
    elif command.lower() == "open amazon":
        webbrowser.open("https://amazon.com")
    elif command.lower() == "open alibaba":
        webbrowser.open("https://alibaba.com")
    elif command.lower() == "open aliexpress":
        webbrowser.open("https://aliexpress.com")
    elif command.lower()==("open roblox"):
        webbrowser.open("https://www.roblox.com")
    elif command.lower() == "open blueprint":
        webbrowser.open("https://www.blueprint.com")
    elif command.lower() == "open intro":
        webbrowser.open("E:\Programming\INTRO\intro.html")  
    elif command.lower() == "open ramfree":
        subprocess.Popen(r"E:\optimise\ram free\Required Softwares\Mem Reduct\64\memreduct.exe")
    elif command.lower()==("open problems over peace"):
        webbrowser.open("https://www.youtube.com/watch?v=OcoEM04ThsU")
    elif command.lower()==("open lovesick"):
        webbrowser.open("https://www.youtube.com/watch?v=2VPYQaS0yVE")
    elif command.lower()==("open 100million"):
        webbrowser.open("https://www.youtube.com/watch?v=0dXiVYq8HBc")
    elif command.lower()==("open myshop"):
        webbrowser.open("https://codecanyon.net/author_dashboard")
    elif command.lower()==("open pythoncoding"):
        webbrowser.open("https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg")
    


    else:
        result_label.config(text="Command not recognized")

    entry.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("YOUR ASSISTANT")
root.geometry("400x300")
root.configure(bg="lightblue")

frame = tk.Frame(root, bg="skyblue")
frame.pack(expand=True, fill="both", padx=20, pady=20)

title_label = tk.Label(frame, text="YOUR ASSISTANT", font=("Arial", 18, "bold"), bg="skyblue", fg="white")
title_label.pack(pady=10)

instruction_label = tk.Label(frame, text="Type 'open <command>' to execute a command.", font=("Arial", 12), bg="skyblue", fg="white")
instruction_label.pack(pady=5)

entry = tk.Entry(frame, width=30, font=("Arial", 12))
entry.pack(pady=5)

execute_button = tk.Button(frame, text="Execute", command=TakeCommand, font=("Arial", 12), bg="white", fg="skyblue")
execute_button.pack(pady=5)

result_label = tk.Label(frame, text="", font=("Arial", 12), bg="skyblue", fg="white")
result_label.pack(pady=5)

entry.focus_set()
entry.bind("<Return>", TakeCommand)

root.mainloop()
