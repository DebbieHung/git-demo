# GIT-DEMO
### 版本號檢視
-  git --version

### 建立全域端使用者
-  git config --global user.name XXX
- git config --global user.email XXX@mail

### 檢視git config
- git config --list

### VSCODE
- ctrl+shift+p (開啟設定)
  - 選擇Default
    - Terminal: select Default Profile
      - command promt

### 控管專案
-  git init

### ctrl+z 回上一動

### 檔案加入控管
- git add filename
   - Untrack(U)=>Add(A)=>Modified(M)=>Deleted

### 檢視控管狀態
- git status

### 檢查物件內容
-  git cat-file -t sha1(2+4 目錄兩個字元+檔案前四碼)=>看型態
- git cat-file -p sha1(2+4 目錄兩個字元+檔案前四碼)=>看內容

### Added=>Modified
       - git status
       - git add filename(確認修改)
   -git add .(所有)

### 反悔修改
   -git restore filename
   -git restore .(所有)


### 檢視暫存區目前控管的內容
   - git ls-files -s 

### 記錄到倉庫區
   - git commit -m 'message' =>寫一行字
   - git commit -am "message" =>added & m  兩動做一動add和commit一起做

### 檢視目前commit
  - git log
  - git log --oneline
  - 離開打q

### git commit 輸入較多文字:開啟vum編輯器
  - 進入編輯器，要按 i 進入insert模式寫字
  - 完成後按 esc鍵 並打 :wq 儲存並離開(write & quit) / :q! 不儲存離開

### 合併上一次的commit
  - git commit --amend =>不會新增一條新的commit，會合併到上一條，或是編修上次的commit內容

### 指令刪除
  - git rm -f filename(強制刪除檔案)
  - git restore --staged filename(恢復檔案)

### 將檔案移出暫存區/倉庫區(A->U)  =>非移除，檔案還是存在只是移出變成Untrack
  - git rm --cached filename

### 檢視分支
  - git branch =>預設為master分支(需有commit才會出現)

### 新增分支
  - git branch 分支名稱 =>接一個新的分支名稱，就會新增分支

### 切換分支
  - git checkout 分支名稱 =>要看星號在哪裡就是在哪個branch

### 同時新增並切換分支
  - git checkout -b 分支名稱

### 合併分支
         先在新增的分支修改/測試程式後，把它合併回原本master程式
  - git merge 分支名稱 =>需要先切回master分支(git checkout master)再merge

### 刪除分支
  - git branch -D 分支名稱

### 切換commit
  - git checkout commit-sha1=>回到過去看當時的程式碼
    *如果回到過去要修改，務必要新增分支!修改完再回來master and merge
  - git checkout master=>回到最新當下
  =>> 因此要適時commit產生斷點，才有機會回去檢查

### 合併衝突
    在不同分支修改了相同的檔案，且都有在各自分支commit檔案，合併時會產生衝突，
    可以選擇保留分支1 、 保留分支2 或是兩者內容都保留
    - git merge --abort =>反悔合併，用ctrl+z同樣效果

### 重置指令reset
 -  git reset commit-sha1 =>會回到過去的檔案，後面的檔案會變成untrack(預設是mixed模式)，檔案不會消失
 -  git reset --hard commit-sha1 =>檔案會真的刪掉
 -  git reset ORIG_HEAD(恢復) 
 -  git reset --hard HEAD(重置到最新commit)
 -  git reset --hard HEAD~1(重置到最新commit的前一個)


### 檢視所有歷程
 - git reflog=>可以觀察commit-sha1 進行reset

### github 資訊
- echo "# git-demo" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/DebbieHung/git-demo.git
- git push -u origin master

### 綁定github雲端的倉庫 repository
- git remote add origin https://github.com/DebbieHung/git-demo.git
- git remote -v =>檢視當下本地專案綁定哪個雲端倉庫url

### 本地同步到雲端
- git push
- git push --set-upstream origin master =>第一次推送要建立分支
- git push -u origin master =>和上面第二條一樣意思 簡化版

### 複製專案
-  git clone https://github.com/DebbieHung/git-demo.git
(在資料夾按右鍵 open git bash here，跳出畫面後輸入上面指令，會把該專案複製下來，含.git)