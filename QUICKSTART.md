
# QUICKSTART GUIDE

For Windows:
1. Get edit permission for this repository. Talk with whoever is in charge.
   - If nobody has permission to add new users on this repository, just fork it and start over.
2. Install git-scm:
   - git is a "source control manager". It lets you copy files from this repository to your computer and back again.
   - https://git-scm.com/download/win
     - Direct link: https://github.com/git-for-windows/git/releases/download/v2.40.0.windows.1/Git-2.40.0-64-bit.exe
   - Run installer.
   - Test git is installed.
     - Press `windows + r` to open the "run" menu.
     - Type `cmd` in the box and press enter. This will open the most basic Windows command prompt.
     - Type `git --version` and press enter. This should print out a message like `git version 2.50.0.windows.1`. If not, either the installer failed or your PATH environment variable does not point to git.
3. Install vscode.
   - vscode is an "integrated development environment". Like `notepad` but with syntax highlighting.
   - https://code.visualstudio.com/docs/?dv=win
   - Run installer.
4. Install python.
   - Open command prompt: Press `windows + r`, then type "cmd" and press enter, then type `python` and press enter.
   - If it opens the windows store to install python, click "Get". Then try running `python` again.
   - If it prints something like
```cmd
Python 3.11.3 (tags/v3.11 ... on win32
Type "help", "copyright", ... information.
>>> _
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;then Python is installed. Run `exit()` to exit the Python shell, then `exit` to exit cmd.

5. Install the python libraries we use.
    - Run command `pip install setuptools numpy pyrtlsdr pyserial pyftdi astropy`
    - (I've forgotten some for sure; usually, if a python library is used like `import module_name`, do `pip install module_name`)
6. Download this repository.
   - Option 1: vscode.
     - Open vscode: Press `windows` key, then type "vscode" to search for the program, then press `enter` to run vscode.
     - Open command palette: `ctrl + shift + p`
     - Type "git clone", press enter, then paste in the url of this repository: `https://github.com/RidhaChowdhury/MiniRadioTelescope.git`.
     - Save the repository to your desktop so you can find it again.
     - Open the repository in vscode: Press `ctrl + k` then `ctrl + o`, then navigate to your desktop, select "MiniRadioTelescope", and press `enter`.
     - Configure your git identity: open the terminal: ``ctrl + ` ``.
     - Run `git config user.email "msp5393@psu.edu"` and `git config user.name "Mark Peschel"` with your own email and name.
   - Option 2: cmd. (I do it this way, but you may need to manage credentials which I do not understand on Windows)
     - Open command prompt: `windows + r` -> type `cmd` -> enter.
     - Look at the "prompt": it should be something like `C:\Users\mpeschel>` where `mpeschel` is your username. This is your "home" directory.
       - You must be in the correct directory for commands to work. If you are in the wrong one, type `cd C:\Users\yourusername\` to get back to your home.
       - The "prompt" tells you your "working directory". When you run programs from the command prompt, they start in your working directory.
       - Run `cd Desktop` to navigate to your desktop. If you save files to your desktop, you will be able to find them again.
       - Run `dir` to view the contents of your working directory.
     - Run `git clone https://github.com/RidhaChowdhury/MiniRadioTelescope.git` to download this repository.
     - Run `cd MiniRadioTelescope`
     - Run `git config user.email "msp5393@psu.edu"` and `git config user.name "Mark Peschel"` with your own email and name.
     - Launch vscode: `code .\`.

7. Install python extension for vscode
   - In vscode, press `ctrl + shift + x` to search for extensions.
   - type "@id:ms-python.python"
   - Click "install" on the official microsoft package.
     - these steps are equivalent to opening a python file and clicking the popup to "install recommended python stuffs"
8. Test that you can run stuff.
   - In vscode:
     - Press ``ctrl + ` `` (that's a back-tick; usually top left of keyboard next to 1) to open integrated terminal
     - Run `python test.py`. Tests should complete ok, though astropy may spit out a bunch of garbage about certificates.
   - In cmd:
     - Navigate to your repository: `cd C:\Users\mpeschel\Desktop\MiniRadioTelescope`
     - Run `python test.py`. Tests should complete ok.
9. Test that you can commit and push.
   - In vscode:
     - Open the "CONTRIBUTORS.md" file: Press `ctrl + shift + e` to open file explorer and click on "CONTRIBUTORS.md".
     - Add your name/handle/email/whatever. Save the file.
     - Open source control: `ctrl + shift + g`. Type message "Test commit."
     - "Stage" the change to CONTRIBUTORS.md by clicking the plus sign that shows up when you hover it. Staging a change means putting it in a batch to be committed together. Uncommitted changes will not be made public, and may be erased if you try to sync.
     - Click Commit.
       - If you get an error "configure user.email/user.name", then run `git config user.email "msp5393@psu.edu"` and `git config user.name "Mark Peschel"` in the integrated terminal and try again.
       - Committing adds your changes to git's local history/backups, so if you do something you regret, you can get your old files back.
     - Click Sync Changes.
       - This will run `git pull` and `git push`, which will first update your local repository to any remote changes, then push your changes to the remote repository.
       - The first time you do this, it will ask you to sign in.
     - Go to https://github.com/RidhaChowdhury/MiniRadioTelescope/blob/master/CONTRIBUTORS.md and your name should appear.
   - In cmd:
     - As in vscode, add your name to CONTRIBUTORS.md.
     - Run `git status` to show pending changes. You should see "Changes not staged for commit: modified: CONTRIBUTORS.md".
     - Run `git add .` to stage everything or `git add CONTRIBUTORS.md` to stage just that file.
     - Run `git status`. Expect "Changes to be committed: modified: CONTRIBUTORS.md".
     - Run `git commit -m "Test commit"`.
       - This will record your changes in git's local history, so you can restore from backup if you make a mistake.
       - If you do not include the `-m "Test commit"` you will be transported to ~~the shadow realm~~ vim, the worst good text editor.
       - In vim normal mode, press `i` to enter insert mode. Type your commit message. Press `escape` to reenter normal mode.
       - Then type `:wq` (colon, which is `shift + ;` followed by `wq`). Press enter. This should save and exit.
     - Run `git pull` to get changes from the remote. This is important if other people have made changes to your files, since you can resolve the conflicts locally before pushing.
     - Run `git push`. This is the step where you may have problems with credentials, but I guess on Windows git-scm includes something to deal with it automagically? idk. If it doesn't work for you, please figure it out and document your solution here.
     - Go to https://github.com/RidhaChowdhury/MiniRadioTelescope/blob/master/CONTRIBUTORS.md and your name should appear.






